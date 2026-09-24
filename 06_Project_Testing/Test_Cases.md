# LegalEase – Project Testing

## 1. Introduction

The Testing phase verifies that the LegalEase application works correctly and that the main features produce the expected results.

## 2. Testing Objectives

The main objectives are:

- Verify user input validation.
- Verify communication between the Streamlit frontend and FastAPI backend.
- Verify legal document generation.
- Verify document editing.
- Verify TXT, DOCX, and PDF downloads.
- Identify and correct errors.

## 3. Test Cases

| Test ID | Test Case | Input / Action | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Open application | Start Streamlit frontend | LegalEase interface opens successfully | Pass |
| TC02 | Select document type | Select a document type | Selected type is displayed | Pass |
| TC03 | Enter party details | Enter valid party information | Information is accepted | Pass |
| TC04 | Enter terms | Enter terms separated by semicolons | Terms are accepted | Pass |
| TC05 | Enter effective date | Enter a valid date | Date is accepted | Pass |
| TC06 | Generate document | Click Generate Document | Legal document is generated | Pass |
| TC07 | Empty document type | Leave document type empty | Validation/error message is displayed | Pass |
| TC08 | Empty parties | Leave parties empty | Validation/error message is displayed | Pass |
| TC09 | Empty terms | Leave terms empty | Validation/error message is displayed | Pass |
| TC10 | Empty effective date | Leave date empty | Validation/error message is displayed | Pass |
| TC11 | Edit generated document | Modify generated text | Edited content is displayed | Pass |
| TC12 | Download TXT | Click Download TXT | TXT file is downloaded | Pass |
| TC13 | Download DOCX | Click Download DOCX | Valid DOCX file is downloaded | Pass |
| TC14 | Download PDF | Click Download PDF | Valid PDF file is downloaded | Pass |
| TC15 | Backend API | Send valid request to `/generate` | API returns generated document | Pass |
| TC16 | Invalid API request | Send incomplete request | Appropriate error response is returned | Pass |

## 4. Functional Testing

### 4.1 Frontend Testing

The Streamlit interface was tested to verify:

- Input fields are displayed correctly.
- Document type can be selected.
- Party information can be entered.
- Terms and conditions can be entered.
- Effective date can be entered.
- Generated content is displayed.
- Generated content can be edited.

### 4.2 Backend Testing

The FastAPI backend was tested to verify:

- The API starts successfully.
- The `/generate` endpoint is available.
- Valid requests are processed.
- Required fields are validated.
- Generated content is returned successfully.

### 4.3 Export Testing

The export functionality was tested for:

- TXT generation
- DOCX generation
- PDF generation

The downloaded files were checked to ensure they can be opened and contain the edited document content.

## 5. Error Handling

The application includes validation for missing required information.

The following fields are required:

- Document type
- Parties
- Terms
- Effective date

Appropriate error messages are displayed when required information is missing.

## 6. Testing Environment

The application was tested using:

- Operating System: Windows
- Programming Language: Python
- IDE: Visual Studio Code
- Backend: FastAPI
- Frontend: Streamlit
- API Server: Uvicorn
- Browser: Google Chrome

## 7. Test Result Summary

The main application functions were tested successfully, including document input, generation, editing, API communication, and document export.

## 8. Conclusion

Testing confirms that the main LegalEase application workflow operates as expected. The testing phase also helps identify errors and verify that the application provides the expected output for valid and invalid inputs.