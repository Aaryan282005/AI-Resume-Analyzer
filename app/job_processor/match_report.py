from matcher import (
    match_skills,
    calculate_skill_match_percentage,
    calculate_text_similarity
)


def generate_match_report(
    resume_text,
    job_description,
    resume_skills,
    job_skills
):

    skill_result = match_skills(
        resume_skills,
        job_skills
    )

    matched_skills = skill_result["matched_skills"]

    missing_skills = skill_result["missing_skills"]

    skill_percentage = calculate_skill_match_percentage(
        matched_skills,
        job_skills
    )

    text_similarity = calculate_text_similarity(
        resume_text,
        job_description
    )

    report = {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required_skills": len(job_skills),
        "matched_skill_count": len(matched_skills),
        "missing_skill_count": len(missing_skills),
        "skill_match_percentage": skill_percentage,
        "text_similarity_percentage": text_similarity
    }

    return report