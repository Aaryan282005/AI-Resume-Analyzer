import json

from matching_engine import (
    analyze_resume_job_match
)


resume_text = """
I am a Python developer with experience
in SQL, Java and Git.

I have worked on machine learning projects
and developed REST APIs using Spring Boot.
"""


job_description = """
We are looking for a Python developer with
experience in SQL, Machine Learning, Docker,
Git and Spring Boot.

The candidate should have experience
developing REST APIs.
"""


resume_skills = [
    "python",
    "sql",
    "java",
    "git",
    "machine learning",
    "spring boot"
]


job_skills = [
    "python",
    "sql",
    "machine learning",
    "docker",
    "git",
    "spring boot"
]


report = analyze_resume_job_match(
    resume_text,
    job_description,
    resume_skills,
    job_skills
)


print(
    "========== COMPLETE MATCHING REPORT =========="
)

print(
    json.dumps(
        report,
        indent=4
    )
)