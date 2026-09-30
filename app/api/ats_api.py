from app.ats.final_ats_engine import analyze_ats


def run_ats_analysis(
    resume_text,
    job_description,
    resume_profile,
    resume_skills,
    job_skills
):
    high_priority_skills = [
        "python",
        "sql",
        "machine learning"
    ]

    medium_priority_skills = [
        "docker",
        "spring boot",
        "rest api"
    ]

    low_priority_skills = [
        "aws",
        "kubernetes"
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

    return result