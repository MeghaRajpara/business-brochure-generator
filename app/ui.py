import gradio as gr
from app.brochure_generator import create_brochure_text, generate_pdf


def generate_brochure(company_name: str, url: str):
    brochure_text = create_brochure_text(company_name, url)
    return generate_pdf(company_name, brochure_text)


def launch_ui():
    interface = gr.Interface(
        fn=generate_brochure,
        inputs=[
            gr.Textbox(label="Company Name"),
            gr.Textbox(label="Website URL")
        ],
        outputs=gr.File(label="Download Brochure PDF"),
        title="AI Business Brochure Generator",
        examples=[
            ["Hugging Face", "https://huggingface.co"],
            ["Gradio", "https://www.gradio.app"]
        ],
        flagging_mode="never"
    )

    interface.launch()
