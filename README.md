# LegalEase – AI-Powered Legal Document Generator

## Project Overview

LegalEase is an AI-powered legal document generation application designed to help users create structured legal documents from simple user-provided information.

The application allows users to enter document details such as document type, parties, terms, and effective date. The generated document can then be reviewed, edited, and downloaded.

## Project Objectives

- Generate structured legal documents.
- Provide a simple and user-friendly interface.
- Allow users to edit generated documents.
- Support TXT, DOCX, and PDF exports.
- Provide a modular frontend and backend architecture.
- Demonstrate the use of AI-assisted document generation.

## Key Features

- Legal document generation
- Multiple document types
- Party and term input
- Effective date input
- Editable document preview
- TXT download
- DOCX download
- PDF download
- FastAPI backend
- Streamlit frontend
- Input validation

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Streamlit
- Google Gemini API
- Python-docx
- FPDF
- Requests
- Pillow

## Project Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Document Generation
  ↓
Generated Legal Document
  ↓
Editable Preview
  ↓
TXT / DOCX / PDF