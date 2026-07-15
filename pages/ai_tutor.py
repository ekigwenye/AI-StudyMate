import streamlit as st

from utils.helpers import extract_text
from utils.prompts import tutor_prompt
from utils.gemini import generate_summary

st.title("🤖 AI Tutor")

st.write(
    "Upload your notes or paste text, then ask AI StudyMate questions about the content."
)

if "study_material" not in st.session_state:
    st.session_state.study_material = ""

if "tutor_response" not in st.session_state:
    st.session_state.tutor_response = ""

option = st.radio(
    "Choose input type",
    ["Paste Text", "Upload File"]
)

if option == "Paste Text":

    st.session_state.study_material = st.text_area(
        "Paste your study material",
        height=250
    )

else:

    uploaded_file = st.file_uploader(
        "Upload PDF, DOCX or TXT",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:

        st.session_state.study_material = extract_text(uploaded_file)

        st.success("✅ File uploaded successfully!")

question = st.text_input(
    "Ask a question about your study material"
)

if st.button("🤖 Ask AI Tutor"):

    if not st.session_state.study_material.strip():

        st.warning("Please upload or paste some study material first.")

    elif not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            prompt = tutor_prompt(
                st.session_state.study_material,
                question
            )

            answer = generate_summary(prompt)

            if answer:

                st.session_state.tutor_response = answer

                st.success("✅ Answer Generated!")

            else:

                st.warning(
                    "⚠️ AI service is temporarily unavailable. Please try again later."
                )

if st.session_state.tutor_response:

    st.markdown("---")

    st.subheader("📖 AI Tutor Response")

    st.markdown(st.session_state.tutor_response)

    st.download_button(
        "📥 Download Answer",
        st.session_state.tutor_response,
        "AI_Tutor_Response.txt",
        "text/plain"
    )