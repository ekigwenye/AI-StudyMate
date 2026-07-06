from PyPDF2 import PdfReader
from docx import Document


def read_pdf(uploaded_file):
    """Extract text from a PDF file."""
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text


def read_docx(uploaded_file):
    """Extract text from a Word document."""
    document = Document(uploaded_file)
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def read_txt(uploaded_file):
    """Extract text from a plain text file."""
    return uploaded_file.read().decode("utf-8")
