import streamlit as st

from utils.helpers import extract_text
from utils.prompts import tutor_prompt
from utils.gemini import generate_summary


# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="AI Tutor",
    page_icon="🤖"
)


# ------------------------------------
# TITLE
# ------------------------------------

st.title("🤖 AI Tutor")

st.write(
    "Your personal AI learning assistant. Upload your notes, ask questions, and get explanations based on your study material."
)


# ------------------------------------
# SESSION STATE INITIALIZATION
# ------------------------------------

if "study_material" not in st.session_state:
    st.session_state.study_material = ""

if "tutor_history" not in st.session_state:
    st.session_state.tutor_history = []

if "tutor_sessions" not in st.session_state:
    st.session_state.tutor_sessions = 0


# ------------------------------------
# STUDY MATERIAL INPUT
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


if input_type == "Paste Text":

    st.session_state.study_material = st.text_area(
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
            "Extracting study material..."
        ):

            st.session_state.study_material = extract_text(
                uploaded_file
            )

        st.success(
            "✅ File uploaded successfully!"
        )

        with st.expander(
            "Preview Material"
        ):

            st.write(
                st.session_state.study_material[:2000]
            )


# ------------------------------------
# LEARNING MODE
# ------------------------------------

st.subheader("🎓 Learning Mode")


learning_mode = st.selectbox(
    "How should AI Tutor help you?",
    [
        "Explain Concept",
        "Simplify Topic",
        "Exam Preparation",
        "Create Examples",
        "Solve Questions"
    ]
)


# ------------------------------------
# QUESTION INPUT
# ------------------------------------

question = st.text_input(
    "Ask AI Tutor a question:"
)


# ------------------------------------
# ASK AI
# ------------------------------------

if st.button(
    "🤖 Ask AI Tutor",
    use_container_width=True
):

    if not st.session_state.study_material.strip():

        st.warning(
            "Please add study material first."
        )


    elif not question.strip():

        st.warning(
            "Please enter a question."
        )


    else:

        with st.spinner(
            "AI Tutor is thinking..."
        ):

            prompt = tutor_prompt(
                st.session_state.study_material,
                question
            )

            prompt += f"""

Learning Mode:
{learning_mode}

Provide a clear educational explanation.
Use simple examples where necessary.
Help the student understand the concept rather than only giving an answer.

"""


            try:

                answer = generate_summary(
                    prompt
                )


                if answer:

                    st.session_state.tutor_sessions += 1


                    st.session_state.tutor_history.append(
                        {
                            "question": question,
                            "answer": answer
                        }
                    )


                    st.success(
                        "✅ Explanation Generated!"
                    )


                else:

                    st.warning(
                        "AI service did not return a response."
                    )


            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


# ------------------------------------
# CHAT HISTORY
# ------------------------------------

if st.session_state.tutor_history:

    st.divider()

    st.subheader(
        "📖 Tutor Conversation"
    )


    for chat in reversed(
        st.session_state.tutor_history
    ):

        st.markdown(
            f"### ❓ Question\n{chat['question']}"
        )

        st.markdown(
            f"### 🤖 Answer\n{chat['answer']}"
        )

        st.divider()


    # Download conversation

    conversation = ""


    for chat in st.session_state.tutor_history:

        conversation += (
            f"Question:\n{chat['question']}\n\n"
            f"Answer:\n{chat['answer']}\n\n"
            "-----------------------\n\n"
        )


    st.download_button(
        "📥 Download Tutor Notes",
        conversation,
        "AI_Tutor_Notes.txt",
        "text/plain"
    )


# ------------------------------------
# CLEAR CHAT
# ------------------------------------

if st.button(
    "🗑️ Clear Conversation"
):

    st.session_state.tutor_history = []

    st.success(
        "Conversation cleared!"
    )