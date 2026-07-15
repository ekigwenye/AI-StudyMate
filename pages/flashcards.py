import streamlit as st

from utils.helpers import extract_text
from utils.prompts import flashcard_prompt
from utils.gemini import generate_summary

st.set_page_config(
    page_title="AI Flashcards",
    page_icon="🃏"
)

st.title("🃏 AI Flashcards")

st.write(
    "Generate interactive study flashcards from your notes."
)

if "flashcards" not in st.session_state:
    st.session_state.flashcards = ""

option = st.radio(
    "Choose input type",
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
        "Upload PDF, DOCX or TXT",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        st.success("✅ File uploaded successfully!")

num_cards = st.slider(
    "Number of Flashcards",
    5,
    30,
    10
)

if st.button("🃏 Generate Flashcards"):

    if text.strip() == "":

        st.warning("Please enter study material.")

    else:

        with st.spinner("Generating flashcards..."):

            prompt = flashcard_prompt(
                text,
                num_cards
            )

            cards = generate_summary(prompt)

            if cards:

                st.session_state.flashcards = cards

                st.success("✅ Flashcards Generated!")

            else:

                st.warning(
                    "⚠️ AI service is temporarily unavailable. Please try again later."
                )

if st.session_state.flashcards:

    st.markdown("---")

    st.subheader("📚 Your Flashcards")

    st.markdown(st.session_state.flashcards)

    st.download_button(
        "📥 Download Flashcards",
        st.session_state.flashcards,
        "flashcards.txt",
        "text/plain"
    )