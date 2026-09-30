import json

from improved_matching_engine import (
    analyze_improved_match
)


resume_text = """
I am a Python developer with experience in SQL,
Java and Docker.

I have worked on predictive modeling projects
using Python and machine learning techniques.
"""


job_description = """
We are looking for a Python developer with experience
in SQL, Machine Learning and Docker.

The candidate should understand predictive modeling
and software development.
"""


resume_skills = [
    "Python",
    "SQL",
    "Java",
    "Docker",
    "Predictive Modeling"
]


job_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Docker"
]


result = analyze_improved_match(
    resume_text,
    job_description,
    resume_skills,
    job_skills
)


print("========== IMPROVED MATCHING ENGINE ==========")

print(
    json.dumps(
        result,
        indent=4
    )
)