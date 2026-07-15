import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("models/gemini-3.5-flash")


def generate_ai_response(prompt):
    """
    Sends a prompt to Gemini and returns the AI response.
    Returns None if an error occurs.
    """
    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text

        return None

    except Exception as e:
        st.error(f"Gemini Error: {e}")
        return None


# Backward compatibility
def generate_summary(prompt):
    return generate_ai_response(prompt)