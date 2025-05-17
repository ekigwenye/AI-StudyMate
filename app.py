import streamlit as st from transformers import pipeline import openai import time

Set your OpenAI API key

openai.api_key = st.secrets["OPENAI_API_KEY"]

Load summarizer once using caching

@st.cache_resource def load_summarizer(): return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

Page config and title

st.set_page_config(page_title="AI StudyMate", page_icon="🎓", layout="centered") st.title("AI StudyMate: Your Smart Learning Companion") st.markdown("Your smart learning companion for summarizing, chatting, quizzing, and staying productive.")

Tabs for each feature

tab1, tab2, tab3, tab4 = st.tabs(["📚 Summarize", "💬 Chat", "❓ Quiz", "⏱ Study Timer"])

--- Tab 1: Summarize ---

with tab1: st.subheader("Summarize Notes") text_input = st.text_area("Paste your notes or study content here:", height=300) if st.button("Summarize") and text_input: with st.spinner("Summarizing..."): summary = summarizer(text_input, max_length=120, min_length=30, do_sample=False)[0]['summary_text'] st.subheader("Summary:") st.success(summary)

--- Tab 2: Chat ---

with tab2: st.subheader("AI Chat") user_question = st.text_input("Ask any study-related question:") if st.button("Ask") and user_question: with st.spinner("Thinking..."): response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "system", "content": "You are a helpful tutor for secondary and university students."}, {"role": "user", "content": user_question} ] ) answer = response['choices'][0]['message']['content'] st.subheader("Answer:") st.info(answer)

--- Tab 3: Quiz ---

with tab3: st.subheader("Quiz Generator") topic = st.text_input("Enter a topic or paste some text:") if st.button("Generate Quiz") and topic: with st.spinner("Creating questions..."): quiz_prompt = f"Generate 3 multiple-choice questions (with options and correct answers) based on the following topic or content:\n{topic}" response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[{"role": "user", "content": quiz_prompt}] ) quiz = response['choices'][0]['message']['content'] st.subheader("Quiz:") st.write(quiz)

--- Tab 4: Study Timer ---

with tab4: st.subheader("Study Timer") if 'study_time' not in st.session_state: st.session_state.study_time = 0

if st.button("Start 25-Minute Study Session"):
    st.success("Timer started! Simulating 25 minutes...")
    time.sleep(2)  # Short delay for demo
    st.session_state.study_time += 25
    st.success("25 minutes added to your study log!")

st.metric("Total Study Time (min)", st.session_state.study_time)
if st.session_state.study_time >= 100:
    st.balloons()
    st.success("Great job! You're staying consistent with your studies!")

Footer

st.markdown("---") st.markdown( "<div style='text-align: center'>Made with ❤️ by Ekigwenye · <a href='https://github.com/ekigwenye/AI-StudyMate' target='_blank'>GitHub Repo</a></div>", unsafe_allow_html=True )

