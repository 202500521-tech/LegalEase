# LegalEase – Project Development

## 1. Project Overview

LegalEase is an AI-powered legal document generation application designed to help users create structured legal documents from user-provided information.

The application accepts details such as document type, parties, terms, and effective date and generates a legal document that can be reviewed, edited, and exported.

## 2. Technology Stack

- Python
- FastAPI
- Uvicorn
- Streamlit
- Google Gemini API
- Python-docx
- FPDF
- Requests
- Pillow

## 3. Project Structure

```text
05_Project_Development/
├── ai_core/
│   ├── __init__.py
│   ├── gemini_generator.py
│   └── generator.py
│
├── frontend/
│   └── app.py
│
├── legalEaseAPI/
│   ├── __init__.py
│   ├── main.py
│   └── routes.py
│
├── Image/
│   ├── inverseLogo.png
│   └── Logo.png
│
├── requirements.txt
└── README.md