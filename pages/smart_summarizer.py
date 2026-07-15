import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils.prompts import summary_prompt
from utils.gemini import generate_summary
from utils.helpers import extract_text

st.title("📚 Smart Summarizer")
st.write("Turn long study materials into clean, structured summaries.")

# ---------------------------
# INPUT SECTION
# ---------------------------

option = st.radio(
    "Choose input type:",
    ["Paste Text", "Upload File"]
)

text = ""

if option == "Paste Text":
    text = st.text_area(
        "Paste your study material here",
        height=250
    )

elif option == "Upload File":

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:
        text = extract_text(uploaded_file)
        st.success("✅ File uploaded successfully!")

# ---------------------------
# SETTINGS
# ---------------------------

st.subheader("⚙️ Summary Settings")

length = st.selectbox(
    "Summary Length",
    ["Short", "Medium", "Detailed"]
)

style = st.selectbox(
    "Summary Style",
    ["Simple", "Academic", "Bullet Points"]
)

# ---------------------------
# GENERATE SUMMARY
# ---------------------------

if st.button("🚀 Generate Summary"):

    if not text.strip():
        st.error("Please provide some text or upload a file.")

    else:

        with st.spinner("Generating summary..."):

            try:

                prompt = summary_prompt(text, length, style)

                summary = generate_summary(prompt)

                st.success("✅ Summary Generated!")

                st.markdown(summary)

                # ---------------------------
                # CREATE PDF
                # ---------------------------

                pdf_buffer = BytesIO()

                doc = SimpleDocTemplate(pdf_buffer)

                styles = getSampleStyleSheet()

                story = []

                story.append(Paragraph("<b>AI StudyMate Summary</b>", styles["Heading1"]))
                story.append(Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"]))

                doc.build(story)

                pdf_buffer.seek(0)

                st.download_button(
                    label="📥 Download Summary as PDF",
                    data=pdf_buffer,
                    file_name="AI_StudyMate_Summary.pdf",
                    mime="application/pdf"
                )

            except Exception:
                st.warning(
                    "⚠️ The AI service is temporarily busy or you've reached the free usage limit. Please wait a minute and try again."
                )