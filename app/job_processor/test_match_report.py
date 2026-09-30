import json

from match_report import generate_match_report


resume_text = """
I am a Python developer with experience in SQL,
Java and Git. I have worked on machine learning projects.
"""


job_description = """
We are looking for a Python developer with experience
in SQL, Machine Learning, Docker and Git.
"""


resume_skills = [
    "python",
    "sql",
    "java",
    "git",
    "machine learning"
]


job_skills = [
    "python",
    "sql",
    "machine learning",
    "docker",
    "git"
]


report = generate_match_report(
    resume_text,
    job_description,
    resume_skills,
    job_skills
)


print("========== RESUME-JOB MATCHING REPORT ==========")

print(
    json.dumps(
        report,
        indent=4
    )
)