import json

from final_ats_engine import (
    analyze_ats
)


resume_text = """
Software developer with experience in
Python, SQL, Docker, Java and Spring Boot.

Built backend applications using REST APIs.
"""


job_description = """
We are looking for a software engineer
with experience in Python, SQL, Docker,
AWS, Kubernetes and Machine Learning.

Experience with Spring Boot and REST APIs
is preferred.
"""


resume_profile = {
    "personal_info": {
        "name": "Sample Candidate",
        "email": "sample@example.com"
    },

    "education": [
        {
            "degree": "B.E. Computer Science"
        }
    ],

    "experience": [
        {
            "role": "Software Developer"
        }
    ],

    "projects": [
        {
            "name": "Backend Application"
        }
    ],

    "skills": [
        "Python",
        "SQL",
        "Docker",
        "Java",
        "Spring Boot"
    ]
}


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
    "Machine Learning",
    "Spring Boot",
    "REST API"
]


high_priority_skills = [
    "Python",
    "SQL",
    "Machine Learning"
]


medium_priority_skills = [
    "Docker",
    "Spring Boot",
    "REST API"
]


low_priority_skills = [
    "AWS",
    "Kubernetes"
]


result = analyze_ats(
    resume_text,
    job_description,
    resume_profile,
    resume_skills,
    job_skills,
    high_priority_skills,
    medium_priority_skills,
    low_priority_skills
)


print(
    "========== FINAL ATS ANALYSIS =========="
)


print(
    "\nFINAL ATS SCORE:",
    result["final_ats_score"]["final_ats_score"],
    "/ 100"
)


print("\n========== SCORE BREAKDOWN ==========")

print(
    "Exact Skill:",
    result["final_ats_score"]["exact_skill_score"],
    "/ 30"
)

print(
    "Semantic Skill:",
    result["final_ats_score"]["semantic_skill_score"],
    "/ 30"
)

print(
    "Keyword Coverage:",
    result["final_ats_score"]["keyword_score"],
    "/ 20"
)

print(
    "Resume Quality:",
    result["final_ats_score"]["resume_quality_score"],
    "/ 20"
)


print("\n========== SKILL GAPS ==========")

for skill in result[
    "skill_gap_analysis"
]["missing_skills"]:

    print(
        "❌",
        skill
    )


print("\n========== PRIORITIZED SKILL GAPS ==========")

for item in result[
    "prioritized_skill_gaps"
]:

    print(
        item["priority"],
        "→",
        item["skill"]
    )


print("\n========== COMPLETE ATS REPORT ==========")

print(
    json.dumps(
        result,
        indent=4
    )
)