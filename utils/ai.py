
from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def ask_ai(system_prompt, user_prompt, model="gpt-4.1-mini"):
    """
    Sends a prompt to OpenAI and returns the response.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content
