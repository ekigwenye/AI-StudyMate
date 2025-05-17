import streamlit as st
from transformers import pipeline
import openai
import time

# Page setup
st.set_page_config(page_title="AI StudyMate", page_icon="🎓", layout="centered")
st.title("AI StudyMate")
st.markdown("Your smart learning companion for summarizing notes, asking questions, generating quizzes, and staying productive.")

# Load summarizer with specific model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Sidebar for navigation
st.sidebar.title("Features")
option = st.sidebar.radio("Select a feature:", ["📚 Summarize Notes", "💬 Ask AI", "❓ Quiz Generator", "⏱ Study Timer"])

# --- Feature: Summarize Notes ---
if option == "📚 Summarize Notes":
    st.header("Summarize Your Notes")
    text_input = st.text_area("Paste your notes or study content below:", height=300)
    if st.button("Summarize") and text_input:
        with st.spinner("Summarizing..."):
            try:
                summary = summarizer(text_input, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
                st.subheader("Summary:")
                st.success(summary)
            except Exception as e:
                st.error(f"Error during summarization: {e}")

# --- Feature: AI Chatbot ---
elif option == "💬 Ask AI":
    st.header("Ask AI StudyMate")
    user_question = st.text_input("Ask any academic or study-related question:")
    if st.button("Ask") and user_question:
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful AI study assistant for students."},
                        {"role": "user", "content": user_question}
                    ]
                )
                answer = response['choices'][0]['message']['content']
                st.subheader("Answer:")
                st.info(answer)
            except Exception as e:
                st.error(f"Error getting answer: {e}")

# --- Feature: Quiz Generator ---
elif option == "❓ Quiz Generator":
    st.header("Quiz Generator")
    topic = st.text_area("Enter a topic or paste some study text:")
    if st.button("Generate Quiz") and topic:
        with st.spinner("Creating questions..."):
            try:
                prompt = f"Generate 3 multiple-choice questions (with 4 options and correct answers) based on:\n\n{topic}"
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                quiz = response['choices'][0]['message']['content']
                st.subheader("Quiz:")
                st.write(quiz)
            except Exception as e:
                st.error(f"Error generating quiz: {e}")

# --- Feature: Study Timer ---
elif option == "⏱ Study Timer":
    st.header("Study Tracker")
    if 'study_time' not in st.session_state:
        st.session_state.study_time = 0

    if st.button("Start 25-Minute Study Session"):
        with st.spinner("Simulating 25-minute session..."):
            time.sleep(2)  # For demo purposes
            st.session_state.study_time += 25
        st.success("Session complete! 25 minutes added.")

    st.metric("Total Study Time (minutes)", st.session_state.study_time)

    if st.session_state.study_time >= 100:
        st.balloons()
        st.success("Awesome work! You're staying consistent!")
