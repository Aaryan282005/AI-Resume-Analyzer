from skill_score import (
    calculate_exact_skill_score
)


resume_skills = [
    "Python",
    "SQL",
    "Docker",
    "AWS",
    "Kubernetes"
]


job_skills = [
    "Python",
    "SQL",
    "Docker",
    "AWS",
    "Kubernetes"
]


result = calculate_exact_skill_score(
    resume_skills,
    job_skills
)


print(
    "========== EXACT SKILL SCORE =========="
)


print(
    "Match Percentage:",
    result["match_percentage"],
    "%"
)


print(
    "ATS Score:",
    result["score"],
    "/",
    result["max_points"]
)


print(
    "\nMatched Skills:"
)


for skill in result["matched_skills"]:
    print(
        "  ✅",
        skill
    )


print(
    "\nMissing Skills:"
)


for skill in result["missing_skills"]:
    print(
        "  ❌",
        skill
    )