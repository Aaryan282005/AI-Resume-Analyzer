from semantic_score import (
    calculate_semantic_skill_score
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


result = calculate_semantic_skill_score(
    resume_skills,
    job_skills
)


print(
    "========== SEMANTIC SKILL SCORE =========="
)


print(
    "Semantic Match:",
    result["semantic_match_percentage"],
    "%"
)


print(
    "ATS Score:",
    result["score"],
    "/",
    result["max_points"]
)


print(
    "\nSkill Similarities:"
)


for item in result["skill_scores"]:

    print(
        item["job_skill"],
        "→",
        item["resume_skill"],
        "(",
        item["similarity"],
        "%)"
    )