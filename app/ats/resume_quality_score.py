def calculate_resume_quality_score(
    resume_profile,
    max_points=20
):

    checks = {
        "contact_information": False,
        "education": False,
        "experience": False,
        "projects": False,
        "skills": False
    }


    # Contact information

    if resume_profile.get("personal_info"):
        checks["contact_information"] = True


    # Education

    if resume_profile.get("education"):
        checks["education"] = True


    # Experience

    if resume_profile.get("experience"):
        checks["experience"] = True


    # Projects

    if resume_profile.get("projects"):
        checks["projects"] = True


    # Skills

    if resume_profile.get("skills"):
        checks["skills"] = True


    passed_checks = sum(
        checks.values()
    )


    total_checks = len(
        checks
    )


    quality_percentage = (
        passed_checks
        / total_checks
    ) * 100


    score = (
        quality_percentage
        / 100
    ) * max_points


    return {
        "quality_percentage": round(
            quality_percentage,
            2
        ),

        "score": round(
            score,
            2
        ),

        "max_points": max_points,

        "checks": checks
    }