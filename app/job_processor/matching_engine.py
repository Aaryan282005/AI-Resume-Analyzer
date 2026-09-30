from app.job_processor.matcher import (
    match_skills,
    calculate_skill_match_percentage,
    calculate_text_similarity
)

from app.job_processor.semantic_matcher import (
    calculate_semantic_similarity
)


def analyze_resume_job_match(
    resume_text,
    job_description,
    resume_skills,
    job_skills
):

    # -----------------------------
    # 1. Skill Matching
    # -----------------------------

    skill_result = match_skills(
        resume_skills,
        job_skills
    )

    matched_skills = skill_result[
        "matched_skills"
    ]

    missing_skills = skill_result[
        "missing_skills"
    ]


    # -----------------------------
    # 2. Skill Match Percentage
    # -----------------------------

    skill_match_percentage = (
        calculate_skill_match_percentage(
            matched_skills,
            job_skills
        )
    )


    # -----------------------------
    # 3. TF-IDF Similarity
    # -----------------------------

    tfidf_similarity = (
        calculate_text_similarity(
            resume_text,
            job_description
        )
    )


    # -----------------------------
    # 4. Semantic Similarity
    # -----------------------------

    semantic_similarity = (
        calculate_semantic_similarity(
            resume_text,
            job_description
        )
    )


    # -----------------------------
    # 5. Final Report
    # -----------------------------

    report = {

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "total_required_skills": len(
            job_skills
        ),

        "matched_skill_count": len(
            matched_skills
        ),

        "missing_skill_count": len(
            missing_skills
        ),

        "skill_match_percentage":
            skill_match_percentage,

        "tfidf_similarity_percentage":
            tfidf_similarity,

        "semantic_similarity_percentage":
            semantic_similarity
    }


    return report