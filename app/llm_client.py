import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL_LINK_SELECTION = "gpt-5-nano"
MODEL_BROCHURE = "gpt-4.1-mini"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LINK_SYSTEM_PROMPT = """
You are given a list of links from a company website.
Select only the links useful for creating a business brochure.

Return JSON in the following format:
{
  "links": [
    {"type": "about page", "url": "https://example.com/about"}
  ]
}
Exclude privacy, terms, and email links.
"""

BROCHURE_SYSTEM_PROMPT = """
You analyze company website content and create a short business brochure
for customers, investors, and job seekers.

Respond in markdown without code blocks.
Include culture, products, customers, and careers if available.
"""


def select_relevant_links(links_text: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL_LINK_SELECTION,
        messages=[
            {"role": "system", "content": LINK_SYSTEM_PROMPT},
            {"role": "user", "content": links_text}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)


def generate_brochure_markdown(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_BROCHURE,
        messages=[
            {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
