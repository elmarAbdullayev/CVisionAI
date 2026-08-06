from PyPDF2 import PdfReader
from io import BytesIO

def pdf_to_text(pdf_bytes: bytes):
    reader = PdfReader(BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text

    return {"Lebenslauf Inhalt":text}