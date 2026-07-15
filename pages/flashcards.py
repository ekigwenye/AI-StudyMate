import streamlit as st

from utils.helpers import extract_text
from utils.prompts import flashcard_prompt
from utils.gemini import generate_summary

st.title("🃏 AI Flashcards")

st.write("Create study flashcards from your notes.")

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

else:

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        st.success("✅ File uploaded successfully!")

num_cards = st.slider(
    "Number of Flashcards",
    min_value=5,
    max_value=30,
    value=10
)

if st.button("🃏 Generate Flashcards"):

    if not text.strip():

        st.warning("Please paste text or upload a file.")

    else:

        prompt = flashcard_prompt(
            text,
            num_cards
        )

        cards = generate_summary(prompt)

        if cards:

            st.success("✅ Flashcards Generated!")

            st.markdown(cards)