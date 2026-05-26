from google import genai
import json

# Create Gemini client
client = genai.Client(api_key="AIzaSyAZZ1O3p2WFusyXqLYqdAfI6NeJt6fL440")


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
    except json.JSONDecodeError:

        print("ERROR: AI returned invalid JSON.")

        return None

    except Exception as e:

        print("ERROR:", e)

        return None



# Get user input
issue = input("Enter support issue: ")

# Analyze issue
result = analyze_ticket(issue)

# Check result
if result:

    print("\nSeverity:")
    print(result["severity"])

    print("\nSummary:")
    print(result["summary"])

    print("\nPossible Causes:")
    for cause in result["possible_causes"]:
        print("-", cause)

    print("\nSuggested Fixes:")
    for fix in result["suggested_fixes"]:
        print("-", fix)