import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils.prompts import summary_prompt
from utils.gemini import generate_summary
from utils.helpers import extract_text

# ------------------------------------
# PAGE TITLE
# ------------------------------------

st.title("📚 Smart Summarizer")
st.write("Turn long study materials into clear, structured study notes.")

# ------------------------------------
# SESSION STATE
# ------------------------------------

if "summary" not in st.session_state:
    st.session_state.summary = ""

# ------------------------------------
# INPUT TYPE
# ------------------------------------

option = st.radio(
    "Choose input type:",
    ["Paste Text", "Upload File"]
)

text = ""

# ------------------------------------
# PASTE TEXT
# ------------------------------------

if option == "Paste Text":

    text = st.text_area(
        "Paste your study material here",
        height=250,
        placeholder="Paste notes, articles or textbook content..."
    )

# ------------------------------------
# UPLOAD FILE
# ------------------------------------

else:

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        text = extract_text(uploaded_file)

        st.success("✅ File uploaded successfully!")

# ------------------------------------
# SUMMARY SETTINGS
# ------------------------------------

st.subheader("⚙️ Summary Settings")

length = st.selectbox(
    "Summary Length",
    ["Short", "Medium", "Detailed"]
)

style = st.selectbox(
    "Summary Style",
    ["Simple", "Academic", "Bullet Points"]
)

# ------------------------------------
# GENERATE SUMMARY
# ------------------------------------

if st.button("🚀 Generate Summary"):

    if not text.strip():

        st.warning("Please paste some text or upload a file.")

    else:

        with st.spinner("Generating summary..."):

            prompt = summary_prompt(
                text,
                length,
                style
            )

            summary = generate_summary(prompt)

            if summary:

                st.session_state.summary = summary

                st.success("✅ Summary Generated!")

            else:

                st.session_state.summary = ""

                st.warning(
                    "⚠️ AI service is temporarily unavailable. Please wait a minute and try again."
                )

# ------------------------------------
# DISPLAY SUMMARY
# ------------------------------------

if st.session_state.summary:

    st.markdown("---")

    st.subheader("📖 Your Summary")

    st.markdown(st.session_state.summary)

    # --------------------------------
    # DOWNLOAD AS TXT
    # --------------------------------

    st.download_button(
        label="📥 Download Summary (.txt)",
        data=st.session_state.summary,
        file_name="AI_StudyMate_Summary.txt",
        mime="text/plain"
    )

    # --------------------------------
    # DOWNLOAD AS PDF
    # --------------------------------

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(pdf_buffer)

    styles = getSampleStyleSheet()

    story = [
        Paragraph(
            "<b>AI StudyMate Summary</b>",
            styles["Heading1"]
        ),
        Paragraph(
            st.session_state.summary.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    ]

    doc.build(story)

    pdf_buffer.seek(0)

    st.download_button(
        label="📄 Download Summary (.pdf)",
        data=pdf_buffer,
        file_name="AI_StudyMate_Summary.pdf",
        mime="application/pdf"
    )