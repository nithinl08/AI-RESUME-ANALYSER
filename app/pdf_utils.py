import io
import fitz

def extract_pdf_text(data: bytes) -> str:
    document = fitz.open(stream=io.BytesIO(data), filetype="pdf")
    try:
        return "\n".join(page.get_text("text") for page in document).strip()
    finally:
        document.close()
