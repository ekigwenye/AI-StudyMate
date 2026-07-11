import streamlit as st
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

            except Exception as e:
                st.error(f"Error: {e}")