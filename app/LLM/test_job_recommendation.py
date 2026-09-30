import json
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)

from app.LLM.job_recommendation import (
    generate_job_recommendations
)


resume_path = "data/resumes/sample_resume.pdf"

job_path = "data/jobs/sample_job.txt"


# Read resume

raw_resume_text = extract_text_from_pdf(
    resume_path
)

resume_text = clean_text(
    raw_resume_text
)


# Read job description

with open(
    job_path,
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()


job_description = job_description.strip()


print("========== ANALYZING RESUME AGAINST JOB ==========")


result = generate_job_recommendations(
    resume_text,
    job_description
)


print("\n========== JOB-SPECIFIC RECOMMENDATIONS ==========")


print(
    json.dumps(
        result,
        indent=4
    )
)