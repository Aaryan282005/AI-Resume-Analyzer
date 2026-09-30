from skill_gap_report import (
    generate_skill_gap_report
)


resume_skills = [
    "Python",
    "SQL",
    "Docker",
    "Java",
    "Spring Boot"
]


job_skills = [
    "Python",
    "SQL",
    "Docker",
    "AWS",
    "Kubernetes",
    "Machine Learning"
]


result = generate_skill_gap_report(
    resume_skills,
    job_skills
)


print(
    "========== SKILL GAP REPORT =========="
)


print("\nMatched Skills:")

for skill in result["matched_skills"]:
    print(
        "  ✅",
        skill
    )


print("\nMissing Skills:")

for skill in result["missing_skills"]:
    print(
        "  ❌",
        skill
    )


print(
    "\nTotal Job Skills:",
    result["total_job_skills"]
)

print(
    "Matched Skill Count:",
    result["matched_skill_count"]
)

print(
    "Missing Skill Count:",
    result["missing_skill_count"]
)