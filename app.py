import streamlit as st
import requests
import json

server_location = st.secrets["backend_server"]

st.title("AI Interview Chat Bot 🚀")

with st.form("Details"):

    topic = st.text_input("Enter Language Topic")
    level = st.selectbox("Choose Level", ["Easy", "Medium", "Hard", "Advanced"])
    qtype = st.multiselect("Choose type", ["MCQS", "Theory", "Coding"])

    submit = st.form_submit_button("Generate")

if submit:

    prompt = f"""
Generate 10 {level} interview questions on {topic}.

Return ONLY a JSON array of objects:

[
  {{
    "question": "What is Python?",
    "answer": "Python is a high-level programming language..."
  }}
]

Rules:
- No markdown
- No explanation
- Only valid JSON
"""

    response = requests.post(
        f"{server_location}/generate",
        json={"prompt": prompt}
    )

    st.write("Status:", response.status_code)

    res = response.json()

    data = json.loads(res["object"])   # now safe

    st.subheader("Interview Q&A")

    for i, item in enumerate(data, start=1):
        with st.expander(f"Q{i}: {item['question']}"):
            st.write(item["answer"])