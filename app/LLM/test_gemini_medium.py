import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")


print("Creating Gemini client...")

client = genai.Client(api_key=api_key)


prompt = """
Analyze the following student profile in simple terms.

Student:
A Computer Science student with experience in Python,
Java, SQL, Spring Boot, Hibernate, MySQL and Machine Learning.

Tasks:
1. List the student's technical skills.
2. List three strengths.
3. List three areas for improvement.

Return the answer as plain text.
"""


print("Sending medium-size request...")


response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)


print("Gemini responded.")
print(response.text)