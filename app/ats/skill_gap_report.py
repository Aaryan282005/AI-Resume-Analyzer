def generate_skill_gap_report(
    resume_skills,
    job_skills
):
    resume_skills_normalized = set(
        skill.lower().strip()
        for skill in resume_skills
    )

    job_skills_normalized = set(
        skill.lower().strip()
        for skill in job_skills
    )

    matched_skills = (
        resume_skills_normalized
        .intersection(job_skills_normalized)
    )

    missing_skills = (
        job_skills_normalized
        .difference(resume_skills_normalized)
    )

    return {
        "matched_skills": sorted(
            matched_skills
        ),
        "missing_skills": sorted(
            missing_skills
        ),
        "total_job_skills": len(
            job_skills_normalized
        ),
        "matched_skill_count": len(
            matched_skills
        ),
        "missing_skill_count": len(
            missing_skills
        )
    }