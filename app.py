import streamlit as st from transformers import pipeline import openai import time

App Title

st.set_page_config(page_title="AI StudyMate") st.title("AI StudyMate: Your Smart Learning Companion")

Load Summarizer

@st.cache_resource def load_summarizer(): return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

Set OpenAI API key

openai.api_key = st.secrets["OPENAI_API_KEY"]

Tabs for functionality

tabs = st.tabs(["Summarize Notes", "AI Chatbot", "Quiz Generator", "Study Timer"])

--- Summarize Notes ---

with tabs[0]: st.subheader("Summarize Notes") notes = st.text_area("Enter your study notes:") if st.button("Summarize") and notes: with st.spinner("Summarizing..."): summary = summarizer(notes, max_length=130, min_length=30, do_sample=False) st.success(summary[0]['summary_text'])

--- AI Chatbot ---

with tabs[1]: st.subheader("Ask the AI Chatbot") question = st.text_input("Ask a study question:") if st.button("Get Answer") and question: with st.spinner("Thinking..."): response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "system", "content": "You are a helpful academic assistant."}, {"role": "user", "content": question} ] ) answer = response["choices"][0]["message"]["content"] st.success(answer)

--- Quiz Generator ---

with tabs[2]: st.subheader("Quiz Generator") topic = st.text_input("Enter a topic to generate quiz questions:") if st.button("Generate Quiz") and topic: with st.spinner("Generating questions..."): quiz_prompt = f"Generate 3 multiple-choice questions with 4 options each on the topic: {topic}. Indicate the correct answer." quiz_response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": quiz_prompt} ] ) quiz = quiz_response["choices"][0]["message"]["content"] st.write(quiz)

--- Study Timer ---

with tabs[3]: st.subheader("Study Timer") minutes = st.number_input("Set timer (minutes):", min_value=1, max_value=120, value=25) if st.button("Start Timer"): seconds = minutes * 60 with st.empty(): for i in range(int(seconds), 0, -1): mins, secs = divmod(i, 60) timer_display = f"{mins:02d}:{secs:02d}" st.metric(label="Time Remaining", value=timer_display) time.sleep(1) st.success("Time's up! Take a short break.")

Footer

st.markdown("---") st.markdown( "<div style='text-align: center'>Made with ❤️ by Ekigwenye · <a href='https://github.com/ekigwenye/AI-StudyMate' target='_blank'>GitHub Repo</a></div>", unsafe_allow_html=True )



