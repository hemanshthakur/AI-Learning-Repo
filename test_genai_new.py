from google import genai

# Create Gemini client
client = genai.Client(api_key="AIzaSyAZZ1O3p2WFusyXqLYqdAfI6NeJt6fL440")


def analyze_ticket(issue):

    prompt = f"""
    You are a senior support engineer.

    Analyze the following support issue carefully.

    Return your answer STRICTLY in this format:

    Severity: <Low/Medium/High/Critical>

    Summary:
    <short summary>

    Possible Causes:
    - cause 1
    - cause 2
    - cause 3

    Suggested Fixes:
    - fix 1
    - fix 2
    - fix 3

    Issue:
    {issue}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


# Get user input
issue = input("Enter support issue: ")

# Analyze issue
result = analyze_ticket(issue)

# Print output
print("\nAI ANALYSIS:\n")
print(result)