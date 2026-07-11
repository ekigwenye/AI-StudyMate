import streamlit as st
from pypdf import PdfReader
from docx import Document


def show_error(message):
    st.error(message)


def show_success(message):
    st.success(message)


def show_info(message):
    st.info(message)


def extract_text(uploaded_file):
    """
    Extract text from TXT, PDF, or DOCX files.
    """
    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    elif filename.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)

    else:
        return ""