import re, json
from openai import OpenAI


class ThreatScore:
    def __init__(self, api_token):
        self.client = OpenAI(api_key=api_token, base_url="https://turbo.torob.com/v1")
        self.model = "gpt-4.1-mini"

    # ---------- utils ----------
    def _norm(self, s):
        if s is None:
            return ""
        s = str(s).replace("ي", "ی").replace("ك", "ک").replace("ـ", "")
        s = re.sub(r"\s+", " ", s).strip()
        return s

    def _to_ascii_digits(self, s):
        p = "۰۱۲۳۴۵۶۷۸۹"
        a = "٠١٢٣٤٥٦٧٨٩"
        t = {ord(p[i]): ord(str(i)) for i in range(10)}
        t.update({ord(a[i]): ord(str(i)) for i in range(10)})
        return s.translate(t)

    # ---------- rule ingestion ----------
    def _naive_rules(self, rules):
        rules = self._norm(rules)
        parts = re.split(r"\s*[,\u060C;؛]\s*", rules) if rules else []
        out = []
        for p in parts:
            if ":" not in p:
                continue
            k, v = p.split(":", 1)
            k = self._norm(k)
            v = self._to_ascii_digits(v)
            v = re.sub(r"[^\d\-+]", "", v)
            try:
                w = int(v)
                if 0 < w < 10000:
                    out.append({"keyword": k, "weight": w})
            except:
                pass
        return {"rules": out}

    def _ai_compile_rules(self, rules):
        sys = (
            "Convert Persian scoring rules into STRICT JSON with optional conditions.\n"
            'Return ONLY JSON: {"rules":[{"keyword":"...","weight":N,'
            '"conditions":{"co":[],"not_co":[],"window":6,"count_mode":"per_occurrence|once_per_doc"}}...]}'
        )
        usr = (
            "Rules:\n" + self._norm(rules) + "\n"
            "If no conditions exist, set conditions to {}. Always include integer weight."
        )
        try:
            r = self.client.chat.completions.create(
                model=self.model,
                temperature=0,
                max_tokens=600,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": sys},
                    {"role": "user", "content": usr},
                ],
            )
            j = json.loads(r.choices[0].message.content)
            if (
                isinstance(j, dict)
                and "rules" in j
                and isinstance(j["rules"], list)
                and j["rules"]
            ):
                return j
        except:
            pass
        return self._naive_rules(rules)

    # ---------- pattern builders ----------
    def _token_pat(self, tok):
        Z = "\u200c"
        if not tok:
            return ""
        # allow ا/آ at start
        if tok[0] in ("ا", "آ"):
            head = "(?:ا|آ)"
            tok = tok[1:]
        else:
            head = ""
        core = []
        for ch in tok:
            if ch in "-" + Z:
                core.append(r"[-\u200c]?")
            else:
                core.append(re.escape(ch))
        base = head + "".join(core)
        # optional plural/ezafe on EACH token
        suffix = r"(?:\u200c?(?:ها(?:ی)?|ی))?"
        return base + suffix

    def _phrase_regex(self, phrase):
        phrase = self._norm(phrase)
        if not phrase:
            return re.compile(r"(?!x)")
        tokens = phrase.split()
        mid = r"(?:\s+|\u200c+)"
        inner = mid.join(self._token_pat(t) for t in tokens)
        pat = rf"(?<!\w){inner}(?!\w)"
        return re.compile(pat, flags=re.UNICODE)

    # ---------- tokenization for windows ----------
    def _tokenize_with_spans(self, text):
        words = []
        spans = []
        for m in re.finditer(r"[A-Za-z\u0600-\u06FF]+", text):
            words.append(m.group(0))
            spans.append((m.start(), m.end()))
        return words, spans

    def _match_to_word_range(self, spans, s, e):
        if not spans:
            return (0, -1)
        si = 0
        while si < len(spans) and spans[si][1] <= s:
            si += 1
        ei = len(spans) - 1
        while ei >= 0 and spans[ei][0] >= e:
            ei -= 1
        return (si, ei) if si <= ei else (0, -1)

    def _cond_ok(self, words, L, R, cond):
        if not cond:
            return True
        co = cond.get("co") or []
        not_co = cond.get("not_co") or []
        window = int(cond.get("window") or 6)
        a = max(0, L - window)
        b = min(len(words) - 1, R + window)
        seg = " ".join(words[a : b + 1])
        for t in co:
            if not self._phrase_regex(t).search(seg):
                return False
        for t in not_co:
            if self._phrase_regex(t).search(seg):
                return False
        return True

    # ---------- counting ----------
    def _count_for_rule(self, text, rule):
        kw = rule.get("keyword", "").strip()
        if not kw:
            return 0
        mode = (rule.get("conditions") or {}).get("count_mode") or "per_occurrence"
        rx = self._phrase_regex(kw)
        words, spans = self._tokenize_with_spans(text)
        used_ranges = []
        count = 0
        for m in rx.finditer(text):
            s, e = m.start(), m.end()
            # avoid overlap double-count
            if any(not (e <= a or b <= s) for a, b in used_ranges):
                continue
            L, R = self._match_to_word_range(spans, s, e)
            if R < L:
                continue
            if not self._cond_ok(words, L, R, rule.get("conditions")):
                continue
            count += 1
            used_ranges.append((s, e))
            if mode == "once_per_doc":
                return 1
        return count

    # ---------- main ----------
    def run(self, text, rules):
        text = self._norm(text)
        if not text:
            return 0
        compiled = self._ai_compile_rules(rules)
        total = 0
        for r in compiled.get("rules", []):
            try:
                total += self._count_for_rule(text, r) * int(r["weight"])
            except:
                pass
        # last-resort: if nothing matched but LLM hinted conditions wrongly, ask LLM for final integer
        if total == 0:
            try:
                prompt = f"متن:\n{text}\n\nقوانین:\n{self._norm(rules)}\nفقط عدد امتیاز تهدید را بده."
                resp = self.client.chat.completions.create(
                    model=self.model,
                    temperature=0,
                    max_tokens=10,
                    messages=[{"role": "user", "content": prompt}],
                )
                nums = re.findall(r"\d+", resp.choices[0].message.content or "")
                if nums:
                    return int(nums[-1])
            except:
                pass
        return int(total)
