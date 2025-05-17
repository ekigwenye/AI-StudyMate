import streamlit as st
import openai
import time

# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
            prompt = f"Please summarize the following text:\n{text_input}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            summary = response['choices'][0]['message']['content']
            st.subheader("Summary:")
            st.success(summary)

# --- Feature: AI Chatbot ---
elif option == "AI Chatbot":
    st.header("Ask AI StudyMate")
    question = st.text_input("Ask any study-related question:")
    if st.button("Ask") and question:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful tutor for secondary and university students."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response['choices'][0]['message']['content']
            st.subheader("Answer:")
            st.info(answer)

# --- Feature: Generate Quiz ---
elif option == "Generate Quiz":
    st.header("Quiz Generator")
    topic = st.text_input("Enter a topic or paste content:")
    if st.button("Generate Quiz") and topic:
        with st.spinner("Creating questions..."):
            quiz_prompt = f"Create 3 multiple-choice questions with options and answers based on:\n{topic}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": quiz_prompt}]
            )
            quiz = response['choices'][0]['message']['content']
            st.subheader("Quiz:")
            st.write(quiz)

# --- Feature: Study Tracker ---
elif option == "Study Tracker":
    st.header("Study Tracker")
    if 'study_time' not in st.session_state:
        st.session_state.study_time = 0

    if st.button("Start 25-Minute Study Session"):
        st.success("Timer started! Simulating 25 minutes...")
        time.sleep(2)  # Short delay for demo
        st.session_state.study_time += 25
        st.success("25 minutes added to your study log!")

    st.metric("Total Study Time (min)", st.session_state.study_time)
    if st.session_state.study_time >= 100:
        st.balloons()
        st.success("Great job! You're staying consistent with your studies!")
