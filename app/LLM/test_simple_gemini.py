import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")


print("Creating Gemini client...")

client = genai.Client(
    api_key=api_key
)

print("Sending request to Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Say hello in one short sentence."
)

print("Gemini responded.")
print(response.text)