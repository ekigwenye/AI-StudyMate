import streamlit as st


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="📚",
    layout="wide"
)


# -------------------------------------------------
# Initialize Session State
# -------------------------------------------------

stats = {
    "summaries_generated": 0,
    "quizzes_generated": 0,
    "flashcards_generated": 0,
    "tutor_sessions": 0,
    "study_plans_created": 0
}


for key, value in stats.items():

    if key not in st.session_state:
        st.session_state[key] = value



# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("📚 AI StudyMate")

st.subheader(
    "Learn Smarter. Study Better. Powered by AI."
)

st.markdown("---")



# -------------------------------------------------
# Welcome
# -------------------------------------------------

st.markdown("""
Welcome to **AI StudyMate**, your personal AI-powered learning companion.

AI StudyMate helps students understand difficult topics, summarize learning materials,
create revision resources, and organize their study plans using Artificial Intelligence.

Whether you are preparing for exams, revising lecture notes, or learning new concepts,
AI StudyMate provides tools to make studying more effective.
""")


st.info(
    "👈 Use the navigation menu on the left to access your AI learning tools."
)



# -------------------------------------------------
# Learning Statistics
# -------------------------------------------------

st.header("📊 Your Learning Activity")


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



# -------------------------------------------------
# Features
# -------------------------------------------------

st.header("✨ AI StudyMate Features")


col1, col2 = st.columns(2)


with col1:

    st.markdown("""
### 📝 Smart Note Summarizer

Transform long study materials into clear summaries, key points, and revision notes.


### 🤖 AI Study Tutor

Ask questions and receive explanations based on your learning materials.


### 🃏 AI Flashcards

Generate flashcards automatically for active recall and revision.
""")


with col2:

    st.markdown("""
### 📝 AI Quiz Generator

Create personalized quizzes to test your understanding.


### 📅 AI Study Planner

Generate personalized study schedules based on your goals and available time.


### 📊 Learning Dashboard

Track your AI StudyMate activities and progress.
""")


st.markdown("---")



# -------------------------------------------------
# Study Tip
# -------------------------------------------------

st.header("💡 Study Tip")


st.success(
    "Use active recall and practice testing instead of only rereading notes. "
    "Creating quizzes and flashcards helps strengthen memory and understanding."
)



# -------------------------------------------------
# Quote
# -------------------------------------------------

st.header("📖 Quote of the Day")


st.info(
    "\"Education is the passport to the future, for tomorrow belongs to those who prepare for it today.\" "
    "— Malcolm X"
)


st.markdown("---")



# -------------------------------------------------
# About
# -------------------------------------------------

st.header("👨‍💻 About AI StudyMate")


st.write("""
AI StudyMate was developed by **Treasure Ekigwenye** as an AI-powered learning platform
designed to make studying smarter, faster, and more interactive.

The project combines Python, Streamlit, and Google Gemini AI to provide intelligent
learning tools including summarization, tutoring, flashcards, quizzes, and study planning.
""")


st.markdown("---")



# -------------------------------------------------
# Footer
# -------------------------------------------------

st.caption(
    "Built with ❤️ by Treasure Ekigwenye | AI StudyMate v2"
)