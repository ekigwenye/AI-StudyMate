import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-3.5-flash")


def generate_summary(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"Actual Gemini Error:\n\n{e}")
        return None