import os
import json

from dotenv import load_dotenv
from google import genai


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


def generate_job_recommendations(
    resume_text,
    job_description
):

    prompt = f"""
You are an AI career and resume analysis assistant.

Analyze the candidate's resume against the provided job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "job_alignment_summary": "Brief explanation of how the resume aligns with the job",

    "matching_strengths": [
        "resume strength that directly matches the job"
    ],

    "skill_gaps": [
        "important job requirement that is not clearly demonstrated in the resume"
    ],

    "priority_improvements": [
        "specific improvement the candidate should make for this job"
    ],

    "resume_customization_tips": [
        "specific suggestion for tailoring the resume to this job"
    ]
}}

Rules:
- Use only information present in the resume and job description.
- Do not invent skills, experience, projects, certifications,
  achievements, or metrics.
- Do not make hiring predictions.
- Do not claim that the candidate has a skill unless the resume
  provides evidence for it.
- Distinguish between skills that are present and skills that are
  missing or not clearly demonstrated.
- Focus on the most important job requirements.
- Recommendations must be practical and specific.
- Keep each item concise.
- Do not include Markdown.
- Do not include ```json or ``` around the response.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    response_text = response.text.strip()

    return json.loads(response_text)