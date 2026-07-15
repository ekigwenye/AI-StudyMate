import streamlit as st

from utils.prompts import study_plan_prompt
from utils.gemini import generate_summary


# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📅"
)


# ------------------------------------
# TITLE
# ------------------------------------

st.title("📅 AI Study Planner")

st.write(
    "Create a personalized AI-powered study schedule based on your goals, available time, and learning needs."
)


# ------------------------------------
# SESSION STATE
# ------------------------------------

if "study_plan" not in st.session_state:
    st.session_state.study_plan = ""

if "study_plans_created" not in st.session_state:
    st.session_state.study_plans_created = 0


# ------------------------------------
# STUDY DETAILS
# ------------------------------------

st.subheader("📚 Study Information")


subject = st.text_input(
    "Subject or Course Name",
    placeholder="Example: Biology, Python Programming, Mathematics"
)


topics = st.text_area(
    "Topics to Cover (Optional)",
    placeholder="List specific topics you want included..."
)


col1, col2 = st.columns(2)


with col1:

    days = st.selectbox(
        "📅 Study Duration (Days)",
        [
            3,
            5,
            7,
            10,
            14,
            21,
            30
        ]
    )


with col2:

    hours = st.selectbox(
        "⏰ Study Hours Per Day",
        [
            1,
            2,
            3,
            4,
            5,
            6
        ]
    )


goal = st.selectbox(
    "🎯 Study Goal",
    [
        "Exam Preparation",
        "Revision",
        "Learn New Topic",
        "Assignment Completion"
    ]
)


learning_style = st.selectbox(
    "🧠 Learning Style",
    [
        "Balanced",
        "Practice Focused",
        "Theory Focused",
        "Revision Focused"
    ]
)


# ------------------------------------
# GENERATE STUDY PLAN
# ------------------------------------

if st.button(
    "🚀 Generate Study Plan",
    use_container_width=True
):

    if not subject.strip():

        st.warning(
            "Please enter a subject."
        )


    else:

        with st.spinner(
            "Creating your personalized study plan..."
        ):

            try:

                prompt = study_plan_prompt(
                    subject,
                    days,
                    hours,
                    goal
                )


                prompt += f"""

Additional Requirements:

Topics:
{topics}

Learning Style:
{learning_style}

Create a practical study schedule.

Include:

1. Daily study timetable
2. Topics to study each day
3. Revision sessions
4. Practice activities
5. Exam preparation tips

Make the plan realistic and easy to follow.

"""


                plan = generate_summary(
                    prompt
                )


                if plan:

                    st.session_state.study_plan = plan

                    st.session_state.study_plans_created += 1


                    st.success(
                        "✅ Study Plan Generated Successfully!"
                    )


                else:

                    st.warning(
                        "AI service did not return a study plan."
                    )


            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


# ------------------------------------
# DISPLAY PLAN
# ------------------------------------

if st.session_state.study_plan:

    st.divider()

    st.subheader(
        "📅 Your Personalized Study Plan"
    )


    st.markdown(
        st.session_state.study_plan
    )


    st.download_button(
        "📥 Download Study Plan",
        st.session_state.study_plan,
        "AI_Study_Plan.txt",
        "text/plain"
    )


# ------------------------------------
# CLEAR PLAN
# ------------------------------------

if st.button(
    "🗑️ Clear Study Plan"
):

    st.session_state.study_plan = ""

    st.success(
        "Study plan cleared!"
    )