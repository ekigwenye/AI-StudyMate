import streamlit as st
import google.generativeai as genai


# ------------------------------------
# GEMINI API CONFIGURATION
# ------------------------------------

try:

    api_key = st.secrets["GEMINI_API_KEY"]

    genai.configure(
        api_key=api_key
    )


except Exception as error:

    st.error(
        f"Gemini API configuration failed: {error}"
    )



# ------------------------------------
# GEMINI MODEL
# ------------------------------------

model = genai.GenerativeModel(
    "models/gemini-3.5-flash"
)



# ------------------------------------
# GENERATE AI RESPONSE
# ------------------------------------

def generate_ai_response(prompt):
    """
    Sends a prompt to Gemini and returns the generated response.
    """

    try:

        response = model.generate_content(
            prompt
        )


        if response and hasattr(response, "text"):

            return response.text


        return None


    except Exception as error:

        st.error(
            f"Gemini Error: {error}"
        )

        return None



# ------------------------------------
# COMPATIBILITY FUNCTION
# ------------------------------------

def generate_summary(prompt):
    """
    Used by existing AI StudyMate pages.
    """

    return generate_ai_response(
        prompt
    )