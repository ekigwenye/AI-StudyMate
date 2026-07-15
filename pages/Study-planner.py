import streamlit as st

from utils.prompts import study_plan_prompt
from utils.gemini import generate_summary

st.title("📅 AI Study Planner")

st.write(
    "Generate a personalized study plan for any subject."
)

if "study_plan" not in st.session_state:
    st.session_state.study_plan = ""

subject = st.text_input(
    "📚 Subject"
)

days = st.selectbox(
    "📅 Number of Days",
    [3, 5, 7, 10, 14, 21, 30]
)

hours = st.selectbox(
    "⏰ Study Hours per Day",
    [1, 2, 3, 4, 5, 6]
)

goal = st.selectbox(
    "🎯 Goal",
    [
        "Exam Preparation",
        "Revision",
        "Learn New Topic",
        "Assignment"
    ]
)

if st.button("🚀 Generate Study Plan"):

    if subject.strip() == "":

        st.warning("Please enter a subject.")

    else:

        with st.spinner("Creating your study plan..."):

            prompt = study_plan_prompt(
                subject,
                days,
                hours,
                goal
            )

            plan = generate_summary(prompt)

            if plan:

                st.session_state.study_plan = plan

                st.success("✅ Study Plan Generated!")

            else:

                st.warning(
                    "⚠️ AI service is temporarily unavailable. Please try again later."
                )

if st.session_state.study_plan:

    st.markdown("---")

    st.markdown(st.session_state.study_plan)

    st.download_button(
        "📥 Download Study Plan",
        st.session_state.study_plan,
        "Study_Plan.txt",
        "text/plain"
    )