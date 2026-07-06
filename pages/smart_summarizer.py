
import streamlit as st
from utils.prompts import summary_prompt

# If you already have a file handler, we’ll plug it in later
# from utils.file_handler import extract_text_from_file

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
    text = st.text_area("Paste your content here", height=250)

elif option == "Upload File":
    uploaded_file = st.file_uploader("Upload PDF, DOCX, or TXT")

    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]

        if file_type == "txt":
            text = uploaded_file.read().decode("utf-8")

        else:
            st.warning("File extraction for PDF/DOCX will be added next step.")

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
# GENERATE BUTTON
# ---------------------------

if st.button("🚀 Generate Summary"):

    if not text.strip():
        st.error("Please provide some text first.")
    else:
        with st.spinner("Generating summary..."):

            prompt = summary_prompt(text, length, style)

            # TEMP MOCK OUTPUT (we'll replace with AI next step)
            st.success("Summary Generated!")

            st.subheader("📝 Summary")
            st.write("This is where the AI summary will appear.")

            st.subheader("🔑 Key Takeaways")
            st.write("- Point 1\n- Point 2\n- Point 3")

            st.subheader("📌 Important Terms")
            st.write("- Term 1: Definition\n- Term 2: Definition")

            st.subheader("❓ Practice Questions")
            st.write("1. Question one?\n2. Question two?\n3. Question three?")

            st.subheader("💡 Study Tip")
            st.write("Review this summary daily for better retention.")
