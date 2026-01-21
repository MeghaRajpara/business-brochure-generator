import os
from fpdf import FPDF
from app.llm_client import generate_brochure_markdown
from app.website_scraper import collect_company_content


OUTPUT_DIR = "brochure_files"
FONT_PATH = "fonts/DejaVuSans.ttf"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_brochure_text(company_name: str, url: str) -> str:
    website_content = collect_company_content(url)

    user_prompt = f"""
    Company Name: {company_name}

    Use the following website content to create a professional business brochure:

    {website_content}
    """
    return generate_brochure_markdown(user_prompt)


def generate_pdf(company_name: str, content: str) -> str:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
    pdf.set_font("DejaVu", size=16)
    pdf.multi_cell(0, 10, company_name)

    pdf.ln(5)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 8, content)

    file_path = f"{OUTPUT_DIR}/{company_name.replace(' ', '_')}_brochure.pdf"
    pdf.output(file_path)

    return file_path
