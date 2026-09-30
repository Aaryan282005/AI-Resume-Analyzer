import os
import json
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. "
        "Check your .env file."
    )


client = genai.Client(
    api_key=api_key
)


def analyze_resume_with_gemini(resume_text, max_retries=3, base_delay=5):

    prompt = f"""
You are an AI resume analysis assistant.

Analyze the following resume.

RESUME:
{resume_text}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "overall_assessment": "Brief overall assessment of the resume",

    "strengths": [
        "specific resume strength"
    ],

    "weaknesses": [
    "specific weakness supported by the resume"
    ],

    "technical_skills": [
        "skill or observation"
    ],

    "experience": [
        "experience-related observation"
    ],

    "projects": [
        "project-related observation"
    ],

    "improvement_areas": [
        "specific  and actionable improvement suggestion"
    ]
}}

Rules:
- Use only information present in the resume.
- Do not invent skills, experience, projects, education, or achievements.
- Keep observations concise and professional.
- Do not include Markdown.
- Do not include ```json or ``` around the response.
For "strengths":
- Identify genuine strengths supported by the resume.
- Focus on technical skills, projects, experience, achievements,
  and relevant practical exposure.
- Do not invent achievements.
- Keep each strength concise.
For "weaknesses":
- Identify genuine weaknesses supported by the resume.
- Focus on missing information, weak descriptions,
  lack of measurable achievements, technical gaps,
  project weaknesses, and resume clarity.
- Do not invent missing experience or achievements.
- Do not assume the candidate lacks a skill simply because
  it is not explicitly mentioned unless the resume context supports it.
- Keep each weakness concise and specific.
For "improvement_areas":
- Convert identified weaknesses into practical actions.
- Give specific and actionable suggestions.
- Prioritize improvements that would make the resume stronger
  for software engineering, data science, and AI-related roles.
- Do not invent achievements, metrics, certifications,
  projects, skills, or experience.
- If a measurable achievement is recommended, tell the candidate
  to add it only if the real information is available.
- Avoid generic advice such as "improve your resume".
- Keep each suggestion concise.
"""

    last_error = None

    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            response_text = response.text.strip()

            # Safety net: strip markdown fences even if Gemini adds them despite instructions
            if response_text.startswith("```"):
                response_text = response_text.strip("`")
                response_text = response_text.replace("json", "", 1).strip()

            return json.loads(response_text)

        except errors.ServerError as e:
            last_error = e
            print(f"⚠️ Gemini server busy (attempt {attempt}/{max_retries}): {e}")
            if attempt < max_retries:
                wait_time = base_delay * attempt   # 5s, 10s, 15s
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

        except json.JSONDecodeError as e:
            print(f"⚠️ Gemini returned invalid JSON (attempt {attempt}/{max_retries}): {e}")
            print(f"Raw response was:\n{response_text}")
            last_error = e
            if attempt < max_retries:
                time.sleep(base_delay)

    print("❌ Max retries reached. Analysis failed.")
    raise last_error