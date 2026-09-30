from matcher import (
    match_skills,
    calculate_skill_match_percentage,
    calculate_text_similarity
)


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


# Skill matching
result = match_skills(
    resume_skills,
    job_skills
)


matched_skills = result["matched_skills"]
missing_skills = result["missing_skills"]


# Skill percentage
skill_percentage = calculate_skill_match_percentage(
    matched_skills,
    job_skills
)


# Text similarity
text_similarity = calculate_text_similarity(
    resume_text,
    job_description
)


print("========== RESUME-JOB MATCH ==========")


print("\nMatched Skills:")

for skill in matched_skills:
    print("✅", skill)


print("\nMissing Skills:")

for skill in missing_skills:
    print("❌", skill)


print("\nSkill Match:")
print(skill_percentage, "%")


print("\nText Similarity:")
print(text_similarity, "%")