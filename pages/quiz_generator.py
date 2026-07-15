import streamlit as st
from utils.gemini import generate_summary

st.set_page_config(page_title="AI Quiz Generator", page_icon="📝")

st.title("📝 AI Quiz Generator")
st.write("Generate quiz questions from your study materials.")

text = st.text_area(
    "Paste your study notes here",
    height=250,
    placeholder="Paste your notes..."
)

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
Create {num_questions} {difficulty} {question_type} questions from the following notes.

Include the correct answer after each question.

Notes:
{text}
"""

        with st.spinner("Generating quiz..."):
            quiz = generate_summary(prompt)

        st.success("Quiz Generated!")
        st.write(quiz)

    else:
        st.warning("Please paste some notes first.")