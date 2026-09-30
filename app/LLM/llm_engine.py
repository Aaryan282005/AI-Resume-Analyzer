from app.LLM.resume_analyzer import (
    analyze_resume_with_gemini
)

from app.LLM.job_recommendation import (
    generate_job_recommendations
)


def generate_llm_analysis(
    resume_text,
    job_description=None
):

    resume_analysis = analyze_resume_with_gemini(
        resume_text
    )

    result = {
        "resume_analysis": resume_analysis
    }

    if job_description:

        job_recommendations = (
            generate_job_recommendations(
                resume_text,
                job_description
            )
        )

        result["job_recommendations"] = (
            job_recommendations
        )

    return result