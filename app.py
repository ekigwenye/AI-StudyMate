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
# Header
# -------------------------------------------------
st.title("📚 AI StudyMate")
st.subheader("Learn Smarter. Study Better. Powered by AI.")

st.markdown("---")




# -------------------------------------------------
# Welcome
# -------------------------------------------------
st.markdown("""
Welcome to **AI StudyMate**, your AI-powered learning companion.

This application is designed to help students study more effectively using Artificial Intelligence.

Whether you're preparing for an exam, revising class notes, or trying to understand a difficult topic, AI StudyMate provides practical tools to support your learning journey.
""")

st.info("👈 Use the navigation menu on the left to explore the available features.")




# -------------------------------------------------
# Features
# -------------------------------------------------
st.header("✨ What You Can Do")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### 📝 Smart Note Summarizer
Convert lengthy notes into concise summaries.

### 🤖 AI Study Tutor
Ask questions and receive AI-powered explanations.

### 📚 Quiz Generator
Create multiple-choice quizzes from your notes.
""")

with col2:
    st.markdown("""
### ⏱️ Study Tracker
Monitor your study sessions and stay productive.

### 📈 Learning Dashboard
Track your progress.
*(Coming Soon)*

### 🧠 Flashcards
Generate revision flashcards.
*(Coming Soon)*
""")

st.markdown("---")





# -------------------------------------------------
# Study Tip
# -------------------------------------------------
st.header("💡 Study Tip")

st.success(
    "Instead of reading the same notes repeatedly, "
    "test yourself using quizzes and active recall. "
    "Research shows this improves long-term memory."
)




# -------------------------------------------------
# Quote
# -------------------------------------------------
st.header("📖 Quote of the Day")

st.info(
    "\"Education is the passport to the future, for tomorrow belongs to those who prepare for it today.\" — Malcolm X"
)

st.markdown("---")



# -------------------------------------------------
# About
# -------------------------------------------------
st.header("👨‍💻 About AI StudyMate")

st.write("""
AI StudyMate was developed by **Treasure Ekigwenye** as a practical demonstration of how Artificial Intelligence can improve education through intelligent learning tools.

The project combines Python, Streamlit, OpenAI, and Hugging Face technologies to make studying more accessible, engaging, and effective.
""")

st.markdown("---")



# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption(
    "Built with ❤️ by Treasure Ekigwenye | AI StudyMate v2"
)
