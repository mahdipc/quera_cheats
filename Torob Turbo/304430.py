from openai import OpenAI
import requests
import json

PROMPT = """You are an expert at writing robust XPath queries for product pages.
Return a JSON object with EXACTLY these keys: name_xpath, final_price_xpath, availability_xpath.
Rules:
- Use ONLY the provided HTML contents (do NOT fetch anything yourself).
- XPaths must select ELEMENT NODES (avoid /text()) unless absolutely required by the structure.
- name_xpath: must match EXACTLY ONE element in BOTH pages and contain the product name.
- final_price_xpath: must match EXACTLY ONE element in the AVAILABLE page and ZERO in the UNAVAILABLE page; it should be the final/actual price (not crossed/old/discount percent).
- availability_xpath: must match AT LEAST ONE element in the AVAILABLE page and ZERO in the UNAVAILABLE page (e.g., 'in stock' flag, 'available' badge).
- Prefer short, stable XPaths based on unique ids/classes/labels; avoid brittle deep absolute paths if a concise unique path exists.
- Do NOT include explanations—return ONLY valid JSON with the three XPaths as strings."""


class XPathExtractor:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://turbo.torob.com/v1")
        self.model = "gpt-4.1-mini"

    def _fetch(self, url: str) -> str:
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        txt = r.text
        return " ".join(txt.split())

    def run(self, available_link, unavailable_link):
        avail_html = self._fetch(available_link)
        unavail_html = self._fetch(unavailable_link)

        user_prompt = (
            "Here are two product pages:\n\n"
            "=== AVAILABLE_PAGE_HTML ===\n"
            f"{avail_html}\n"
            "=== UNAVAILABLE_PAGE_HTML ===\n"
            f"{unavail_html}\n\n"
            "Based on ONLY these two HTML pages, produce the JSON with the three XPaths."
        )

        resp = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            max_tokens=300,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": user_prompt},
            ],
        )

        try:
            data = json.loads(resp.choices[0].message.content)
        except Exception:
            resp2 = self.client.chat.completions.create(
                model=self.model,
                temperature=0,
                max_tokens=300,
                messages=[
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
            data = {}
            txt = resp2.choices[0].message.content
            for key in ("name_xpath", "final_price_xpath", "availability_xpath"):
                import re

                m = re.search(rf'"?{key}"?\s*:\s*"([^"]+)"', txt)
                if m:
                    data[key] = m.group(1)

        return {
            "name_xpath": data.get("name_xpath", "//h1"),
            "final_price_xpath": data.get(
                "final_price_xpath",
                "//span[contains(@class,'final') or contains(@class,'price')]",
            ),
            "availability_xpath": data.get(
                "availability_xpath",
                "//*[contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'available') or contains(.,'موجود')]",
            ),
        }
