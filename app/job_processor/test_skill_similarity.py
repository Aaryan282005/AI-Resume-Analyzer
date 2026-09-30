from skill_similarity import (
    calculate_skill_similarity
)


resume_skill = "Python"
job_skill = "HTML"

similarity = calculate_skill_similarity(
    resume_skill,
    job_skill
)


print("========== SKILL SEMANTIC SIMILARITY ==========")

print("Resume Skill:")
print(resume_skill)

print("\nJob Skill:")
print(job_skill)

print("\nSimilarity:")
print(similarity, "%")