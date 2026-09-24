from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai_core.generator import generate_sample_document

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str


@router.post("/generate")
def generate_document(request: DocumentRequest):

    # Validate input
    if not request.document_type.strip():
        raise HTTPException(
            status_code=400,
            detail="Document type is required."
        )

    if not request.parties.strip():
        raise HTTPException(
            status_code=400,
            detail="Parties information is required."
        )

    if not request.terms.strip():
        raise HTTPException(
            status_code=400,
            detail="Terms and conditions are required."
        )

    if not request.effective_date.strip():
        raise HTTPException(
            status_code=400,
            detail="Effective date is required."
        )

    try:
        # Generate the document locally
        document = generate_sample_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date
        )

        return {
            "success": True,
            "document": document
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Document generation error: {error}"
        )