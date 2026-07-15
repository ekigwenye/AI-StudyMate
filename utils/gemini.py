import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-3.5-flash")


def generate_summary(prompt):
    response = model.generate_content(prompt)
    return response.text