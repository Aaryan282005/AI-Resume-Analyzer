def calculate_exact_skill_score(
    resume_skills,
    job_skills,
    max_points=30
):

    if not job_skills:
        return {
            "match_percentage": 0.0,
            "score": 0.0,
            "max_points": max_points,
            "matched_skills": [],
            "missing_skills": []
        }

    resume_skills_set = set(
        skill.lower().strip()
        for skill in resume_skills
    )

    job_skills_set = set(
        skill.lower().strip()
        for skill in job_skills
    )

    matched_skills = (
        resume_skills_set
        .intersection(job_skills_set)
    )

    missing_skills = (
        job_skills_set
        .difference(resume_skills_set)
    )

    match_percentage = (
        len(matched_skills)
        / len(job_skills_set)
    ) * 100

    score = (
        match_percentage
        / 100
    ) * max_points

    return {
        "match_percentage": round(
            match_percentage,
            2
        ),

        "score": round(
            score,
            2
        ),

        "max_points": max_points,

        "matched_skills": sorted(
            matched_skills
        ),

        "missing_skills": sorted(
            missing_skills
        )
    }