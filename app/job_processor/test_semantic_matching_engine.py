import json

from semantic_matching_engine import (
    analyze_semantic_match
)


resume_skills = [
    "Python",
    "Predictive Modeling",
    "SQL",
    "Docker"
]


job_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Docker",
    "Kubernetes"
]


result = analyze_semantic_match(
    resume_skills,
    job_skills
)


print("========== SEMANTIC MATCHING RESULT ==========")

print(
    json.dumps(
        result,
        indent=4
    )
)