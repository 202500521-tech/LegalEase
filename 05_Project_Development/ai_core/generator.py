def generate_sample_document(
    document_type: str,
    parties: str,
    terms: str,
    effective_date: str
) -> str:

    # Convert semicolon-separated terms into numbered clauses
    term_list = [
        term.strip()
        for term in terms.split(";")
        if term.strip()
    ]

    clauses = ""

    for index, term in enumerate(term_list, start=1):
        clauses += f"{index}. {term}\n\n"

    document = f"""
{document_type.upper()}

This Agreement is entered into on {effective_date}.

PARTIES

{parties}

EFFECTIVE DATE

{effective_date}

TERMS AND CONDITIONS

{clauses}

GENERAL PROVISIONS

1. The parties agree to comply with the terms and conditions
   described in this document.

2. Any changes to this agreement should be made with the
   agreement of the parties.

3. The parties should retain a copy of this document for
   their records.

ACKNOWLEDGEMENT

By accepting this document, the parties acknowledge that they
have reviewed the terms and conditions stated above.

LEGAL REVIEW NOTICE

This document is an AI-assisted/sample legal document and is
provided for informational and drafting purposes only. It is
not a substitute for legal advice from a qualified legal
professional. The parties should review this document and
obtain appropriate legal advice before signing or using it.
"""

    return document.strip()