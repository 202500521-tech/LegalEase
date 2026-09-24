# LegalEase: AI-Powered Legal Document Generator

## Phase 3: Project Design

## 1. System Overview

LegalEase consists of a frontend, backend, AI generation component,
and document export functionality.

The user interacts with the Streamlit frontend. The frontend sends
the document-generation request to the FastAPI backend. The backend
processes the request and uses the document-generation component
to generate the document.

The generated document is then displayed to the user for review
and editing and can be downloaded in supported formats.

---

## 2. System Architecture

The main components of the system are:

### Frontend

Technology: Streamlit

Responsibilities:

- Display the user interface.
- Collect document information.
- Send generation requests.
- Display the generated document.
- Allow document editing.
- Provide download options.

### Backend

Technology: FastAPI

Responsibilities:

- Receive requests from the frontend.
- Validate user input.
- Process document-generation requests.
- Return the generated document.

### AI Generation Component

Responsibilities:

- Generate document content based on the provided information.
- Structure the generated content into a legal-document format.

### Document Export Component

Responsibilities:

- Convert the generated document into supported formats.
- Generate TXT, DOCX, and PDF files.

---

## 3. System Architecture Flow

User
  |
  v
Streamlit Frontend
  |
  | Document Type
  | Parties
  | Terms
  | Effective Date
  |
  v
FastAPI Backend
  |
  v
Document Generation Component
  |
  v
Generated Legal Document
  |
  v
Editable Preview
  |
  +---------> TXT
  |
  +---------> DOCX
  |
  +---------> PDF

---

## 4. Data Flow

### Step 1: User Input

The user enters:

- Document type
- Parties
- Terms and conditions
- Effective date

### Step 2: Request Submission

The frontend sends the information to the backend through the
document-generation API.

### Step 3: Input Validation

The backend validates the required information.

### Step 4: Document Generation

The document-generation component creates the legal document
based on the provided information.

### Step 5: Preview

The generated document is displayed to the user.

### Step 6: Editing

The user can review and modify the generated document.

### Step 7: Export

The final document can be downloaded as:

- TXT
- DOCX
- PDF

---

## 5. API Design

### Endpoint

POST /generate

### Request Fields

| Field | Type | Description |
|---|---|---|
| document_type | String | Type of legal document |
| parties | String | Parties involved |
| terms | String | Terms and conditions |
| effective_date | String | Effective date |

### Response

The API returns the generated document.

---

## 6. Component Design

### Frontend Component

The Streamlit application provides the user interface.

### Backend Component

The FastAPI application provides the API endpoint and handles
requests from the frontend.

### Generation Component

The generation module creates the document content.

### Export Component

The export functions create downloadable document files.

---

## 7. User Interface Design

The user interface contains:

1. Application title
2. Document type selection
3. Parties input
4. Terms and conditions input
5. Effective date input
6. Generate button
7. Generated document preview
8. Editable document area
9. Download buttons

---

## 8. Security Design

Sensitive information such as API credentials should be stored
in environment variables and should not be included directly
inside source code.

The `.env` file should not be uploaded to GitHub.

---

## 9. Design Summary

The LegalEase architecture separates the application into
independent components for frontend interaction, backend
processing, document generation, and document export.

This modular structure makes the system easier to maintain,
test, and extend in the future.