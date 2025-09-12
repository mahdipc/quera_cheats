from openai import OpenAI

PROMPT = """You are a strict product categorizer.
Possible categories: SMARTPHONE, LAPTOP, WATCH, FLOWER, CLOTH, UNKNOWN.
Rules:
- If product category is not confidently identifiable from product_name, return UNKNOWN.
- If shop_name meaning conflicts with the product (e.g., flower shop selling iPhone), return UNKNOWN.
- Output ONLY one of: SMARTPHONE|LAPTOP|WATCH|FLOWER|CLOTH|UNKNOWN (no extra text).

Hints (not exhaustive):
SMARTPHONE: iPhone, Galaxy, Xiaomi/Redmi/Poco, OnePlus, Pixel, Huawei/Honor, Oppo/Vivo, Nokia, Infinix, Tecno, smartphone, phone, موبایل, گوشی
LAPTOP: Laptop, Notebook, Ultrabook, MacBook, Surface, ThinkPad, IdeaPad, Legion, ROG, TUF, MSI, Dell, HP, Lenovo, Asus, Acer, لپ‌تاپ
WATCH: Watch, Smartwatch, Galaxy Watch, Apple Watch, Amazfit, Garmin, Mi Band, ساعت, مچ‌بند
FLOWER: گل, گلفروشی, سبد گل, دسته گل, رز, ارکیده
CLOTH: لباس, پوشاک, پیراهن, مانتو, شلوار, تیشرت, کفش, بوت, مزون

Shop intent hints:
- دیجیتال/موبایل/گوشی -> likely SMARTPHONE/WATCH/LAPTOP
- لپ‌تاپ/کامپیوتر -> LAPTOP
- گالری ساعت -> WATCH
- گلفروشی -> FLOWER
- پوشاک/بوتیک/مزون -> CLOTH
- قالیشویی/کافه/رستوران/... -> UNKNOWN for electronics

Examples:
shop_name: موبایل پارسا
product_name: Xiaomi 12
=> SMARTPHONE

shop_name: قالی‌شویی عباس‌آقا
product_name: Apple iPhone 13
=> UNKNOWN
"""


class Solution:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://turbo.torob.com/v1")
        self.model = "gpt-4.1-mini"

    def run(self, text_input: str) -> str:
        msg = f"{text_input.strip()}\n=>"
        resp = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            max_tokens=8,
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": msg},
            ],
        )
        return resp.choices[0].message.content.strip().split()[0]
