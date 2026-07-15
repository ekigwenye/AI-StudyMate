import streamlit as st

from utils.helpers import extract_text
from utils.prompts import flashcard_prompt
from utils.gemini import generate_summary


# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="AI Flashcards",
    page_icon="🃏"
)


# ------------------------------------
# TITLE
# ------------------------------------

st.title("🃏 AI Flashcards")

st.write(
    "Convert your study materials into smart AI-generated flashcards for faster revision."
)


# ------------------------------------
# SESSION STATE
# ------------------------------------

if "flashcards" not in st.session_state:
    st.session_state.flashcards = ""

if "flashcards_generated" not in st.session_state:
    st.session_state.flashcards_generated = 0


# ------------------------------------
# INPUT MATERIAL
# ------------------------------------

st.subheader("📚 Add Study Material")


input_type = st.radio(
    "Choose input method:",
    [
        "Paste Text",
        "Upload File"
    ],
    horizontal=True
)


study_text = ""


if input_type == "Paste Text":

    study_text = st.text_area(
        "Paste your study notes:",
        height=300,
        placeholder="Paste lecture notes, textbook content, or revision materials..."
    )


else:

    uploaded_file = st.file_uploader(
        "Upload PDF, DOCX or TXT",
        type=[
            "pdf",
            "docx",
            "txt"
        ]
    )


    if uploaded_file:

        with st.spinner(
            "Extracting text..."
        ):

            study_text = extract_text(
                uploaded_file
            )


        st.success(
            "✅ File uploaded successfully!"
        )


        with st.expander(
            "Preview Extracted Text"
        ):

            st.write(
                study_text[:2000]
            )


# ------------------------------------
# FLASHCARD SETTINGS
# ------------------------------------

st.subheader("⚙️ Flashcard Settings")


col1, col2 = st.columns(2)


with col1:

    number_cards = st.slider(
        "Number of Flashcards",
        5,
        30,
        10
    )


with col2:

    difficulty = st.selectbox(
        "Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )


# ------------------------------------
# GENERATE FLASHCARDS
# ------------------------------------

if st.button(
    "🃏 Generate Flashcards",
    use_container_width=True
):

    if not study_text.strip():

        st.warning(
            "Please add study material first."
        )


    else:

        with st.spinner(
            "AI is creating flashcards..."
        ):


            prompt = flashcard_prompt(
                study_text,
                number_cards
            )


            prompt += f"""

Difficulty Level:
{difficulty}

Create high-quality study flashcards.

Format each card as:

Flashcard 1

Question:
...

Answer:
...

Make answers concise but complete.
Focus on important concepts and exam preparation.

"""


            try:

                cards = generate_summary(
                    prompt
                )


                if cards:

                    st.session_state.flashcards = cards

                    st.session_state.flashcards_generated += 1


                    st.success(
                        "✅ Flashcards Generated Successfully!"
                    )


                else:

                    st.warning(
                        "AI service did not return flashcards."
                    )


            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


# ------------------------------------
# DISPLAY FLASHCARDS
# ------------------------------------

if st.session_state.flashcards:

    st.divider()

    st.subheader(
        "📚 Generated Flashcards"
    )


    st.markdown(
        st.session_state.flashcards
    )


    st.download_button(
        "📥 Download Flashcards",
        st.session_state.flashcards,
        "AI_Flashcards.txt",
        "text/plain"
    )


# ------------------------------------
# CLEAR BUTTON
# ------------------------------------

if st.button(
    "🗑️ Clear Flashcards"
):

    st.session_state.flashcards = ""

    st.success(
        "Flashcards cleared!"
    )