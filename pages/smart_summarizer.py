import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils.prompts import summary_prompt
from utils.gemini import generate_summary
from utils.helpers import extract_text

st.title("📚 Smart Summarizer")
st.write("Turn long study materials into clear, structured study notes.")

# -------------------------
# Session State
# -------------------------
if "summary" not in st.session_state:
    st.session_state.summary = ""

# -------------------------
# Input
# -------------------------
option = st.radio(
    "Choose input type:",
    ["Paste Text", "Upload File"]
)

text = ""

if option == "Paste Text":

    text = st.text_area(
        "Paste your study material",
        height=250
    )

else:

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:
        text = extract_text(uploaded_file)
        st.success("✅ File uploaded successfully!")

# -------------------------
# Settings
# -------------------------

st.subheader("⚙️ Summary Settings")

length = st.selectbox(
    "Summary Length",
    ["Short", "Medium", "Detailed"]
)

style = st.selectbox(
    "Summary Style",
    ["Simple", "Academic", "Bullet Points"]
)

# -------------------------
# Generate
# -------------------------

if st.button("🚀 Generate Summary"):

    if not text.strip():

        st.warning("Please paste text or upload a file.")

    else:

        with st.spinner("Generating summary..."):

            try:

                prompt = summary_prompt(
                    text,
                    length,
                    style
                )

                summary = generate_summary(prompt)

                st.session_state.summary = summary

                st.success("✅ Summary Generated!")

            except Exception:

                st.warning(
                    "⚠️ AI service is temporarily busy or you've reached the free usage limit. Please wait a minute and try again."
                )

# -------------------------
# Display Summary
# -------------------------

if st.session_state.summary:

    st.markdown("---")
    st.markdown(st.session_state.summary)

    # -------------------------
    # TXT Download
    # -------------------------

    st.download_button(
        label="📥 Download Summary (.txt)",
        data=st.session_state.summary,
        file_name="AI_StudyMate_Summary.txt",
        mime="text/plain"
    )

    # -------------------------
    # PDF Download
    # -------------------------

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