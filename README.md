# AI Business Brochure Generator

An AI-powered application that generates professional business brochures
in PDF format by analyzing a company’s website using Large Language Models.

## Features
- Automatically selects relevant website pages
- Generates concise business-focused brochure content
- Exports high-quality PDF brochures
- Simple Gradio web interface

## Tech Stack
- Python
- OpenAI API
- Gradio
- FPDF
- BeautifulSoup

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/business-brochure-generator.git
cd business-brochure-generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
```
Add your OpenAI API key to .env.

### 5. Run Application
```bash
python main.py
```

### 6. Open Browser
Gradio will start locally at:
```bash
http://127.0.0.1:7860
```
Or Your local URL