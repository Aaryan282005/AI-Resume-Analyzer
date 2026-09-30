from semantic_skill_matcher import (
    semantic_skill_matching
)


def analyze_semantic_match(
    resume_skills,
    job_skills
):
    semantic_result = semantic_skill_matching(
        resume_skills,
        job_skills
    )

    matched_skills = semantic_result["matched_skills"]
    related_skills = semantic_result["related_skills"]
    missing_skills = semantic_result["missing_skills"]

    total_job_skills = len(job_skills)

    if total_job_skills == 0:
        semantic_match_percentage = 0.0
    else:
        semantic_match_percentage = (
            len(matched_skills) / total_job_skills
        ) * 100

    return {
        "semantic_match_percentage":
            round(semantic_match_percentage, 2),

        "matched_skills":
            matched_skills,

        "related_skills":
            related_skills,

        "missing_skills":
            missing_skills
    }