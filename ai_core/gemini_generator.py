import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class GeminiDocumentGenerator:

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        )

        if not self.api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is missing from the .env file."
            )

        self.client = genai.Client(
            api_key=self.api_key
        )

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str
    ) -> str:

        prompt = f"""
You are a professional legal document drafting assistant.

Create a professional draft legal document based on the
information provided below.

Document Type:
{document_type}

Parties:
{parties}

Effective Date:
{effective_date}

Terms and Conditions:
{terms}

Requirements:
1. Give the document a clear title.
2. Identify the parties clearly.
3. Include the effective date.
4. Organize the document into appropriate sections.
5. Convert semicolon-separated terms into clear clauses.
6. Use professional legal-document formatting.
7. Do not invent missing personal information.
8. If important information is missing, use a clear placeholder
   such as [MISSING INFORMATION].
9. Add a final note stating that the document is AI-generated,
   should be reviewed by a qualified legal professional,
   and is not a substitute for legal advice.

Generate only the legal document and the review note.
"""

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            generated_text = response.text

            if not generated_text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return generated_text

        except Exception as error:
            raise RuntimeError(
                f"Gemini API error: {error}"
            )