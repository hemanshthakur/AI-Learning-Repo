from google import genai
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


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
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        data = json.loads(response.text)

        return data

    except json.JSONDecodeError:

        return {
            "error": "Invalid JSON returned by AI."
        }

    except Exception as e:

        return {
            "error": str(e)
        }