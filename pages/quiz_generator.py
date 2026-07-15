import streamlit as st
from utils.gemini import generate_summary
from utils.helpers import extract_text

st.set_page_config(page_title="AI Quiz Generator", page_icon="📝")

st.title("📝 AI Quiz Generator")
st.write("Generate quiz questions from your study materials.")

input_type = st.radio(
    "Choose input type:",
    ["Paste Text", "Upload File"]
)

text = ""

if input_type == "Paste Text":
    text = st.text_area(
        "Paste your study notes here",
        height=250,
        placeholder="Paste your notes..."
    )

else:
    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:
        text = extract_text(uploaded_file)
        st.success("File uploaded successfully!")

num_questions = st.selectbox(
    "Number of Questions",
    [5, 10, 15]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

question_type = st.selectbox(
    "Question Type",
    ["Multiple Choice", "True/False", "Short Answer"]
)

if st.button("Generate Quiz"):
    if text.strip():
        prompt = f"""
Generate {num_questions} {difficulty} {question_type} quiz questions from the study material below.

Requirements:
- Number each question.
- If Multiple Choice, provide four options (A-D).
- After each question, provide the correct answer.
- Keep the questions clear and relevant.

Study Material:

{text}
"""

        with st.spinner("Generating quiz..."):
            quiz = generate_summary(prompt)

        st.success("Quiz Generated Successfully!")
        st.markdown(quiz)

    else:
        st.warning("Please paste text or upload a file.")