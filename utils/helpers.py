import streamlit as st

from pypdf import PdfReader
from docx import Document



# ------------------------------------
# MESSAGE HELPERS
# ------------------------------------

def show_error(message):

    st.error(message)



def show_success(message):

    st.success(message)



def show_info(message):

    st.info(message)



# ------------------------------------
# TEXT EXTRACTION
# ------------------------------------

def extract_text(uploaded_file):
    """
    Extract text from TXT, PDF, or DOCX files.
    """

    try:

        filename = uploaded_file.name.lower()


        # -----------------------------
        # TXT FILE
        # -----------------------------

        if filename.endswith(".txt"):

            return uploaded_file.read().decode(
                "utf-8"
            )


        # -----------------------------
        # PDF FILE
        # -----------------------------

        elif filename.endswith(".pdf"):

            reader = PdfReader(
                uploaded_file
            )

            text = ""


            for page in reader.pages:

                page_text = page.extract_text()


                if page_text:

                    text += page_text + "\n"


            if not text.strip():

                return (
                    "No readable text was found "
                    "in this PDF."
                )


            return text



        # -----------------------------
        # DOCX FILE
        # -----------------------------

        elif filename.endswith(".docx"):

            document = Document(
                uploaded_file
            )


            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            )


            if not text.strip():

                return (
                    "No readable text was found "
                    "in this document."
                )


            return text



        # -----------------------------
        # UNSUPPORTED FILE
        # -----------------------------

        else:

            return (
                "Unsupported file format."
            )


    except UnicodeDecodeError:

        return (
            "Unable to read this text file. "
            "Please upload a UTF-8 encoded file."
        )


    except Exception as error:

        return (
            f"Error extracting file content: {error}"
        )