import streamlit as st



from dotenv import load_dotenv
import os

load_dotenv()

print("KEY =", os.getenv("GROQ_API_KEY"))

from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
st.set_page_config(page_title="AI Group Discussion Evaluator")

st.title("🎤 AI Group Discussion Evaluator")

topic = st.text_input(
    "Enter GD Topic",
    "Artificial Intelligence in Education"
)

response_text = st.text_area(
    "Enter Your GD Response",
    height=250
)

if st.button("Evaluate Response"):

    if response_text.strip() == "":
        st.warning("Please enter your response.")
    else:

        prompt = f"""
        You are an expert Group Discussion evaluator.

        Topic:
        {topic}

        Candidate Response:
        {response_text}

        Evaluate:

        1. Communication Skills (out of 10)
        2. Clarity (out of 10)
        3. Relevance (out of 10)
        4. Confidence (out of 10)
        5. Grammar (out of 10)

        Also provide:

        Strengths
        Weaknesses
        Suggestions for Improvement
        Overall Score
        """

        result = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("Evaluation Report")

        st.write(
            result.choices[0].message.content
        )