
import streamlit as st
from utils.ai import ask_ai

st.set_page_config(
    page_title="Smart Note Summarizer",
    page_icon="📝"
)

st.title("📝 Smart Note Summarizer")

st.write(
    "Paste your study notes below and let AI create a clear summary."
)

summary_type = st.selectbox(
    "Summary Length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)

text = st.text_area(
    "Paste your notes here",
    height=300,
    placeholder="Paste lecture notes, textbook content, or study material..."
)

col1, col2 = st.columns(2)

generate = col1.button("Generate Summary")
clear = col2.button("Clear")

if clear:
    st.rerun()

if generate:

    if not text.strip():
        st.warning("Please enter some study notes.")
        st.stop()

    with st.spinner("Generating summary..."):

        prompt = f"""
Summarize the following study material.

Summary style: {summary_type}

Requirements:
- Keep the important concepts.
- Use simple language.
- Organize with bullet points where appropriate.
- Make it useful for revision.

Study material:

{text}
"""

        try:

            summary = ask_ai(
                "You are an expert educational assistant.",
                prompt
            )

            st.success("Summary generated successfully!")

            st.subheader("Summary")

            st.write(summary)

            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")
