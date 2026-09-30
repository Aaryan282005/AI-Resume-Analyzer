from skill_gap_priority import (
    prioritize_skill_gaps
)


missing_skills = [
    "AWS",
    "Kubernetes",
    "Machine Learning"
]


high_priority_skills = [
    "Machine Learning"
]


medium_priority_skills = [
    "AWS"
]


low_priority_skills = [
    "Kubernetes"
]


result = prioritize_skill_gaps(
    missing_skills,
    high_priority_skills,
    medium_priority_skills,
    low_priority_skills
)


print(
    "========== PRIORITIZED SKILL GAPS =========="
)


for item in result:

    print(
        item["priority"],
        "→",
        item["skill"]
    )