import streamlit as st
import time
from transformers import pipeline
from openai import OpenAI

# Load OpenAI API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Load summarizer (lightweight model)
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="Falconsai/text_summarization")

summarizer = load_summarizer()

# Page config
st.set_page_config(page_title="AI StudyMate", layout="centered")
st.title("AI StudyMate: Your Smart Learning Companion")

# Sidebar navigation
st.sidebar.title("Features")
option = st.sidebar.radio("Select a feature:", ["Summarize Text", "AI Chatbot", "Generate Quiz", "Study Tracker"])

# --- Feature: Summarize Text ---
if option == "Summarize Text":
    st.header("Summarize Your Notes")
    text_input = st.text_area("Paste your notes or study content here:", height=300)
    if st.button("Summarize") and text_input:
        with st.spinner("Summarizing..."):
            try:
                summary = summarizer(text_input, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
                st.subheader("Summary:")
                st.success(summary)
            except Exception as e:
                st.error(f"Summarization error: {e}")

# --- Feature: AI Chatbot ---
elif option == "AI Chatbot":
    st.header("Ask AI StudyMate")
    user_question = st.text_input("Ask any study-related question:")
    if st.button("Ask") and user_question:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful tutor for secondary and university students."},
                        {"role": "user", "content": user_question}
                    ]
                )
                answer = response.choices[0].message.content
                st.subheader("Answer:")
                st.info(answer)
            except Exception as e:
                st.error(f"Chatbot error: {e}")

# --- Feature: Generate Quiz ---
elif option == "Generate Quiz":
    st.header("Quiz Generator")
    topic = st.text_input("Enter a topic or paste some text:")
    if st.button("Generate Quiz") and topic:
        with st.spinner("Creating questions..."):
            try:
                prompt = f"Generate 3 multiple-choice questions (with options and correct answers) based on the following topic or content:\n{topic}"
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                quiz = response.choices[0].message.content
                st.subheader("Quiz:")
                st.write(quiz)
            except Exception as e:
                st.error(f"Quiz error: {e}")

# --- Feature: Study Tracker ---
elif option == "Study Tracker":
    st.header("Your Study Tracker")
    if 'study_time' not in st.session_state:
        st.session_state.study_time = 0

    if st.button("Start 25-Minute Study Session"):
        st.success("Timer started! Simulating 25 minutes...")
        time.sleep(2)  # Simulated delay
        st.session_state.study_time += 25
        st.success("25 minutes added to your study log!")

    st.metric("Total Study Time (min)", st.session_state.study_time)
    if st.session_state.study_time >= 100:
        st.balloons()
        st.success("Great job! You're staying consistent with your studies!")
