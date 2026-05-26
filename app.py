from dotenv import load_dotenv
import os
import streamlit as st
import json
from google import genai

load_dotenv()

# Configure Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Function to analyze ticket
def analyze_ticket(issue):

    prompt = f"""
    You are a senior support engineer.

    Analyze the issue and return ONLY valid JSON.

    Return this exact structure:

    {{
      "severity": "",
      "summary": "",
      "possible_causes": [],
      "suggested_fixes": []
    }}

    Issue:
    {issue}
    """

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        data = json.loads(response.text)

        return data

    except Exception as e:

        st.error(f"Error: {e}")

        return None


# App title
st.title("AI Support Ticket Assistant")


# User input
issue = st.text_area("Enter support issue")


# Analyze button
if st.button("Analyze Ticket"):

    if issue:

        with st.spinner("Analyzing issue..."):

            result = analyze_ticket(issue)

        if result:

            st.subheader("Severity")
            st.write(result["severity"])

            st.subheader("Summary")
            st.write(result["summary"])

            st.subheader("Possible Causes")

            for cause in result["possible_causes"]:
                st.write("-", cause)

            st.subheader("Suggested Fixes")

            for fix in result["suggested_fixes"]:
                st.write("-", fix)

    else:

        st.warning("Please enter a support issue.")