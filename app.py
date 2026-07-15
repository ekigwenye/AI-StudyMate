import streamlit as st


# ------------------------------------
# PAGE CONFIGURATION
# ------------------------------------

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="📚",
    layout="wide"
)


# ------------------------------------
# SESSION STATE INITIALIZATION
# ------------------------------------

default_stats = {
    "summaries_generated": 0,
    "quizzes_generated": 0,
    "flashcards_generated": 0,
    "tutor_sessions": 0,
    "study_plans_created": 0
}


for key, value in default_stats.items():

    if key not in st.session_state:
        st.session_state[key] = value



# ------------------------------------
# HEADER
# ------------------------------------

st.title("📚 AI StudyMate")

st.subheader(
    "Learn Smarter. Study Better. Powered by Artificial Intelligence."
)

st.markdown("---")



# ------------------------------------
# INTRODUCTION
# ------------------------------------

st.markdown(
"""
Welcome to **AI StudyMate**, your intelligent learning companion.

AI StudyMate helps students transform their learning experience by using
Artificial Intelligence to summarize notes, explain concepts, generate revision
materials, and create personalized study plans.

Navigate through the tools on the sidebar to begin learning.
"""
)


st.info(
    "👈 Select a tool from the sidebar to start using AI StudyMate."
)



# ------------------------------------
# ACTIVITY DASHBOARD
# ------------------------------------

st.header("📊 Learning Activity")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "📝 Summaries",
        st.session_state.summaries_generated
    )


with col2:

    st.metric(
        "📝 Quizzes",
        st.session_state.quizzes_generated
    )


with col3:

    st.metric(
        "🃏 Flashcards",
        st.session_state.flashcards_generated
    )


with col4:

    st.metric(
        "🤖 Tutor Sessions",
        st.session_state.tutor_sessions
    )


with col5:

    st.metric(
        "📅 Study Plans",
        st.session_state.study_plans_created
    )



st.markdown("---")



# ------------------------------------
# TOOLS OVERVIEW
# ------------------------------------

st.header("🚀 AI StudyMate Tools")


tools = [

    (
        "📝 Smart Summarizer",
        "Convert lengthy study materials into summaries, key points, important terms, and revision notes."
    ),

    (
        "🤖 AI Tutor",
        "Ask questions and receive AI explanations based on your study materials."
    ),

    (
        "🃏 AI Flashcards",
        "Create effective revision flashcards using your notes."
    ),

    (
        "📝 AI Quiz Generator",
        "Generate personalized quizzes to test your understanding."
    ),

    (
        "📅 AI Study Planner",
        "Create structured study schedules based on your goals."
    )

]


for title, description in tools:

    with st.container():

        st.markdown(
            f"### {title}"
        )

        st.write(
            description
        )

        st.markdown("---")



# ------------------------------------
# STUDY TIP
# ------------------------------------

st.header("💡 Study Tip")


st.success(
"""
Active learning improves memory.

Try combining:
- Flashcards for recall
- Quizzes for testing
- AI Tutor for understanding
- Study Planner for consistency
"""
)



# ------------------------------------
# PROJECT INFORMATION
# ------------------------------------

st.header("👨‍💻 About AI StudyMate")


st.write(
"""
AI StudyMate was created by **Treasure Ekigwenye** as an AI-powered educational
platform that helps students study more effectively.

The application combines:

- Python
- Streamlit
- Google Gemini AI
- Document processing tools

to provide intelligent learning features including summarization, tutoring,
flashcard generation, quizzes, and personalized study planning.
"""
)



# ------------------------------------
# FOOTER
# ------------------------------------

st.markdown("---")


st.caption(
    "Built with ❤️ by Treasure Ekigwenye | AI StudyMate v2"
)