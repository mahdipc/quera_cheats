from openai import OpenAI
import re
import requests
import json

PROMPT = """You are a precise vision assistant.
Task: Read ONLY the digits embedded in the given image and return EXACTLY a 3-digit number with no extra text.
If anything is unclear, still return your best 3-digit guess. Output format: DDD (e.g., 123).
"""


class Solution:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://turbo.torob.com/v1")
        self.model = "gpt-4.1-mini"

    def room1_f(self, room1_url):
        room1_resp = requests.get(room1_url, timeout=300).text
        arr = json.loads(room1_resp)
        image_url = None
        for x in arr:
            if isinstance(x, str) and x.lower().startswith("http"):
                image_url = x.strip()
                break
        return image_url

    def room2_f(self, room2_url):
        room2_html = requests.get(room2_url, timeout=300).text

        m = re.search(r"<b>(.*?)</b>", room2_html, flags=re.DOTALL)
        expr = m.group(1).strip()

        try:
            if re.fullmatch(r"[()\d\*\+\-\s%/]+", expr):
                last2_val = eval(expr, {"__builtins__": {}}, {})
                last2 = f"{int(last2_val):02d}"
                return last2
        except Exception as e:
            print("Eval error:", e)

        return None

    def run(self, question: str) -> str:
        start_url = question.strip()
        start_txt = requests.get(start_url, timeout=300).text
        links = re.findall(r"https?://\S+", start_txt)

        room1_url = links[0].strip()
        room2_url = links[1].strip()
        image_url = self.room1_f(room1_url)

        resp = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            max_tokens=8,
            messages=[
                {"role": "system", "content": PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Read the 3-digit code in this image:",
                        },
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                },
            ],
        )
        first3 = re.sub(r"\D", "", resp.choices[0].message.content).strip()
        first3 = (first3[:3]) if len(first3) >= 3 else first3.zfill(3)

        last2 = self.room2_f(room2_url)

        return f"{first3}{last2}"
