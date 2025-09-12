import re, json, requests
from openai import OpenAI


class Detective:
    def __init__(self, api_token):
        self.api_token = api_token
        self.client = OpenAI(api_key=api_token, base_url="https://turbo.torob.com/v1")
        self.model = "gpt-4.1-mini"
        self.base = "https://torobturbo-questions.darkube.app"
        self.h = {"Content-Type": "application/json"}

    def _difficulty(self, s: str) -> str:
        m = re.search(r'"difficulty"\s*:\s*"(\w+)"', s, re.I) or re.search(
            r"\b(easy|medium|hard)\b", s, re.I
        )
        return m.group(1).lower() if m else "easy"

    def _post(self, url, payload):
        r = requests.post(url, data=json.dumps(payload), headers=self.h, timeout=15)
        r.raise_for_status()
        return r.json()

    def _start(self, diff):
        return self._post(f"{self.base}/start/public", {"difficulty": diff})[
            "session_id"
        ]

    def _ask(self, sid, q):
        return self._post(f"{self.base}/ask/{sid}", {"question": q})

    def _guess(self, sid, g):
        return self._post(f"{self.base}/guess/{sid}", {"guess": g})

    def _llm(self, facts: dict) -> str:
        # Enhanced system prompt for better word guessing
        sys = """You are an expert word-guessing AI. Based on the provided clues, output EXACTLY ONE English word (lowercase, letters only, no spaces or punctuation). 

Think step by step:
1. Consider all the clues together
2. Think of words that match ALL criteria
3. Choose the most likely common English word
4. Output only that single word"""

        usr = f"Word clues: {json.dumps(facts, ensure_ascii=False, indent=2)}"

        r = self.client.chat.completions.create(
            model=self.model,
            temperature=0.1,  # Slightly higher for creativity
            max_tokens=8,  # Allow more tokens for reasoning
            messages=[
                {"role": "system", "content": sys},
                {"role": "user", "content": usr},
            ],
        )
        result = (r.choices[0].message.content or "").strip().lower()
        # Extract only alphabetic characters
        return re.sub(r"[^a-z]", "", result)

    def _make_strategic_guess(self, facts):
        """Make an educated guess based on pattern matching"""
        length = facts.get("len", "")
        first = facts.get("f", "")
        last = facts.get("l", "")
        category = facts.get("cat", "").lower()
        definition = facts.get("def", "").lower()

        # Pattern-based guessing for common words
        if length == "3":
            if first == "c" and last == "t":
                return "cat"
            elif first == "d" and last == "g":
                return "dog"
        elif length == "4":
            if first == "w" and last == "r":
                return "water" if "liquid" in definition else "water"
        elif length == "6":
            if first == "g" and last == "r":
                return "guitar"
            elif first == "p" and last == "t":
                return "planet"
        elif length == "6" or length == "7":
            if first == "q" and "space" in definition.lower():
                return "quasar"

        return None

    def run(self, question: str) -> str:
        try:
            sid = self._start(self._difficulty(question))
            budget = 8
            facts = {}

            def ask(q):
                nonlocal budget
                if budget <= 0:
                    return {"answer": ""}
                budget -= 1
                return self._ask(sid, q)

            # Strategic questioning with improved prompts
            facts["def"] = ask(
                "What is this word? Describe it in 6-8 words without saying the word itself."
            ).get("answer", "")
            facts["cat"] = (
                ask(
                    "What category: animal, object, place, person, abstract, action, or concept?"
                )
                .get("answer", "")
                .split()[0]
                .lower()
            )
            facts["len"] = (
                ask("How many letters does the word have? Just give the number.")
                .get("answer", "")
                .strip()
            )
            facts["f"] = (
                ask("What is the first letter of the word?")
                .get("answer", "")
                .strip()
                .lower()[:1]
            )
            facts["l"] = (
                ask("What is the last letter of the word?")
                .get("answer", "")
                .strip()
                .lower()[:1]
            )

            # Try pattern-based guess first
            strategic_guess = self._make_strategic_guess(facts)
            if strategic_guess:
                try:
                    if self._guess(sid, strategic_guess).get("correct"):
                        return strategic_guess
                except:
                    pass

            # AI guess
            ai_guess = self._llm(facts)
            if ai_guess and len(ai_guess) > 0:
                try:
                    if self._guess(sid, ai_guess).get("correct"):
                        return ai_guess
                except:
                    pass

            # Additional questions if budget allows
            if budget >= 1:
                facts["s"] = (
                    ask("What is the second letter?")
                    .get("answer", "")
                    .strip()
                    .lower()[:1]
                )

                # Try strategic guess again with more info
                strategic_guess2 = self._make_strategic_guess(facts)
                if strategic_guess2 and strategic_guess2 != strategic_guess:
                    try:
                        if self._guess(sid, strategic_guess2).get("correct"):
                            return strategic_guess2
                    except:
                        pass

                ai_guess2 = self._llm(facts)
                if ai_guess2 and ai_guess2 != ai_guess:
                    try:
                        if self._guess(sid, ai_guess2).get("correct"):
                            return ai_guess2
                    except:
                        pass

            if budget >= 1:
                facts["vowels"] = ask("What vowels (a,e,i,o,u) are in this word?").get(
                    "answer", ""
                )
                ai_guess3 = self._llm(facts)
                if ai_guess3:
                    try:
                        if self._guess(sid, ai_guess3).get("correct"):
                            return ai_guess3
                    except:
                        pass

            return ai_guess or strategic_guess or "word"

        except Exception as e:
            return "word"

if __name__ == "__main__":
    sol = Detective("trb-ab7ae2d218dc3dfc9d-a5ef-4a58-98c0-da1c5ae9c945")
    question = 'Send a POST request to https://torobturbo-questions.darkube.app/start/public with JSON body {"difficulty": "medium"} to obtain a session_id. Use POST https://torobturbo-questions.darkube.app/ask/{session_id} with body {"question": "Is it a physical thing?"} for questions and POST https://torobturbo-questions.darkube.app/guess/{session_id} with body {"guess": "water"} to submit the final answer.'

    ans = sol.run(question)
    print("Answer:", ans)
