import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyAZZ1O3p2WFusyXqLYqdAfI6NeJt6fL440")

# Load model
model = genai.GenerativeModel("gemini-3.5-flash")

# Send prompt
response = model.generate_content(
    "Summarize this support issue: Database connection timeout after deployment"
)

# Print AI response
print(response.text)