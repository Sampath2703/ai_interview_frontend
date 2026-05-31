import streamlit as st
import requests
import pandas as pd
import ast
import json

server_location = st.secrets["backend_server"]

st.title("AI Interview Chat Bot")

with st.form("Details"):

    topic = st.text_input("Enter Language Topic")
    level = st.selectbox("Choose Level", ["Easy", "Medium", "Hard", "Advance"])
    q_type = st.multiselect("Choose", ["MCQS", "Theory", "Coding"])

    submit = st.form_submit_button("Generate")

    if submit:

        prompt = f"""


        Generate 10 {level} interview questions on {topic}.

        Return ONLY a JSON array.

        Example:


        [
        "What is Python?",
        "What is OOP?",
        "What is a decorator?"
        ]

        Do not add markdown, explanations, headings, or code blocks.
        """

        response = requests.post(
            f"{server_location}/generate",
            json={"prompt": prompt}
        )

        st.write("Status:", response.status_code)

        if response.status_code == 200:
            res=response.json()
            questions = json.loads(res["object"])

            st.subheader("Interview Questions")

            for i, q in enumerate(questions, start=1):
                st.write(f"{i}. {q}")