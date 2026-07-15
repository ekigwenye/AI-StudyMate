import streamlit as st

from utils.gemini import generate_summary
from utils.helpers import extract_text


# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="📝"
)


# ------------------------------------
# TITLE
# ------------------------------------

st.title("📝 AI Quiz Generator")

st.write(
    "Generate AI-powered quizzes from your study materials and test your understanding."
)


# ------------------------------------
# SESSION STATE
# ------------------------------------

if "quiz" not in st.session_state:
    st.session_state.quiz = ""

if "quizzes_generated" not in st.session_state:
    st.session_state.quizzes_generated = 0


# ------------------------------------
# STUDY MATERIAL
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
        "Upload PDF, DOCX or TXT file",
        type=[
            "pdf",
            "docx",
            "txt"
        ]
    )


    if uploaded_file:

        with st.spinner(
            "Extracting document text..."
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
# QUIZ SETTINGS
# ------------------------------------

st.subheader("⚙️ Quiz Settings")


col1, col2, col3 = st.columns(3)


with col1:

    number_questions = st.selectbox(
        "Number of Questions",
        [
            5,
            10,
            15,
            20
        ]
    )


with col2:

    difficulty = st.selectbox(
        "Difficulty Level",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )


with col3:

    question_type = st.selectbox(
        "Question Type",
        [
            "Multiple Choice",
            "True/False",
            "Short Answer",
            "Mixed Quiz"
        ]
    )


# ------------------------------------
# GENERATE QUIZ
# ------------------------------------

if st.button(
    "🚀 Generate Quiz",
    use_container_width=True
):

    if not study_text.strip():

        st.warning(
            "Please add study material first."
        )


    else:

        prompt = f"""

You are an expert educational quiz creator.

Generate {number_questions} {difficulty} level quiz questions.

Question Format:
{question_type}


Instructions:

- Number each question clearly.
- Test understanding of the topic.
- Avoid unnecessary repetition.

For Multiple Choice questions:
- Provide four options:
A.
B.
C.
D.
- Clearly identify the correct answer.

For True/False questions:
- Provide the statement.
- Provide the correct answer.

For Short Answer questions:
- Provide a model answer.

After the quiz, include:

1. Answer Summary
2. Key Concepts Tested
3. Revision Tips


Study Material:

{study_text}

"""


        with st.spinner(
            "AI is generating your quiz..."
        ):

            try:

                quiz = generate_summary(
                    prompt
                )


                if quiz:

                    st.session_state.quiz = quiz

                    st.session_state.quizzes_generated += 1


                    st.success(
                        "✅ Quiz Generated Successfully!"
                    )


                else:

                    st.warning(
                        "AI service did not return a quiz."
                    )


            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


# ------------------------------------
# DISPLAY QUIZ
# ------------------------------------

if st.session_state.quiz:

    st.divider()

    st.subheader(
        "📝 Your AI Generated Quiz"
    )


    st.markdown(
        st.session_state.quiz
    )


    st.download_button(
        "📥 Download Quiz",
        st.session_state.quiz,
        "AI_Generated_Quiz.txt",
        "text/plain"
    )


# ------------------------------------
# CLEAR QUIZ
# ------------------------------------

if st.button(
    "🗑️ Clear Quiz"
):

    st.session_state.quiz = ""

    st.success(
        "Quiz cleared!"
    )