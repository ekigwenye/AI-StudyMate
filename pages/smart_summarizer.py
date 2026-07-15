import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils.prompts import summary_prompt
from utils.gemini import generate_ai_response
from utils.helpers import extract_text

# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("📚 Smart Summarizer")
st.write("Turn long study materials into clear, structured study notes powered by AI.")

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "summaries" not in st.session_state:
    st.session_state.summaries = 0

# --------------------------------------------------
# INPUT TYPE
# --------------------------------------------------

option = st.radio(
    "Choose input type:",
    ["Paste Text", "Upload File"]
)

text = ""

# --------------------------------------------------
# PASTE TEXT
# --------------------------------------------------

if option == "Paste Text":

    text = st.text_area(
        "Paste your study material",
        height=250,
        placeholder="Paste lecture notes, textbook content, articles or study materials..."
    )

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

else:

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        text = extract_text(uploaded_file)

        st.success("✅ File uploaded successfully!")

# --------------------------------------------------
# SUMMARY SETTINGS
# --------------------------------------------------

st.subheader("⚙️ Summary Settings")

length = st.selectbox(
    "Summary Length",
    ["Short", "Medium", "Detailed"]
)

style = st.selectbox(
    "Summary Style",
    ["Simple", "Academic", "Bullet Points"]
)

# --------------------------------------------------
# GENERATE SUMMARY
# --------------------------------------------------

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

            summary = generate_ai_response(prompt)

            if summary:

                st.session_state.summary = summary
                st.session_state.summaries += 1

                st.success("✅ Summary Generated Successfully!")

            else:

                st.session_state.summary = ""

                st.warning(
                    "⚠️ AI service is temporarily unavailable or you've reached your Gemini quota. Please try again later."
                )

# --------------------------------------------------
# DISPLAY SUMMARY
# --------------------------------------------------

if st.session_state.summary:

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Summary Length", length)

    with col2:
        st.metric(
            "Word Count",
            len(st.session_state.summary.split())
        )

    with st.expander("📖 View Summary", expanded=True):

        st.markdown(st.session_state.summary)

    # --------------------------------------------------
    # COPY SECTION
    # --------------------------------------------------

    st.subheader("📋 Copy Summary")

    st.code(
        st.session_state.summary,
        language="text"
    )

    # --------------------------------------------------
    # DOWNLOAD TXT
    # --------------------------------------------------

    st.download_button(
        label="📥 Download Summary (.txt)",
        data=st.session_state.summary,
        file_name="AI_StudyMate_Summary.txt",
        mime="text/plain"
    )

    # --------------------------------------------------
    # CREATE PDF
    # --------------------------------------------------

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

    st.success("🎉 Your summary is ready to download.")