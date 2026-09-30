import json

from semantic_skill_matcher import (
    semantic_skill_matching
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
    "HTML"
]


result = semantic_skill_matching(
    resume_skills,
    job_skills
)


print("========== MATCHED SKILLS ==========")

for skill in result["matched_skills"]:
    print(
        "Job:",
        skill["job_skill"],
        "| Resume:",
        skill["resume_skill"],
        "| Similarity:",
        skill["similarity"],
        "%"
    )


print("\n========== RELATED SKILLS ==========")

for skill in result["related_skills"]:
    print(
        "Job:",
        skill["job_skill"],
        "| Resume:",
        skill["resume_skill"],
        "| Similarity:",
        skill["similarity"],
        "%"
    )


print("\n========== MISSING SKILLS ==========")

for skill in result["missing_skills"]:
    print(
        "Job:",
        skill["job_skill"],
        "| Similarity:",
        skill["similarity"],
        "%"
    )


print("\n========== COMPLETE RESULT ==========")

print(
    json.dumps(
        result,
        indent=4
    )
)