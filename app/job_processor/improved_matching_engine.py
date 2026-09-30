from matcher import (
    match_skills,
    calculate_skill_match_percentage,
    calculate_text_similarity
)

from semantic_skill_matcher import (
    semantic_skill_matching
)


def analyze_improved_match(
    resume_text,
    job_description,
    resume_skills,
    job_skills
):

    # --------------------------------
    # 1. Exact Skill Matching
    # --------------------------------

    exact_result = match_skills(
        resume_skills,
        job_skills
    )

    exact_matched = exact_result[
        "matched_skills"
    ]

    exact_missing = exact_result[
        "missing_skills"
    ]

    exact_percentage = (
        calculate_skill_match_percentage(
            exact_matched,
            job_skills
        )
    )


    # --------------------------------
    # 2. TF-IDF Similarity
    # --------------------------------

    tfidf_similarity = (
        calculate_text_similarity(
            resume_text,
            job_description
        )
    )


    # --------------------------------
    # 3. Semantic Skill Matching
    # --------------------------------

    semantic_result = semantic_skill_matching(
        resume_skills,
        job_skills
    )


    # --------------------------------
    # 4. Return Combined Analysis
    # --------------------------------

    return {
        "exact_matching": {
            "matched_skills": exact_matched,
            "missing_skills": exact_missing,
            "percentage": exact_percentage
        },

        "tfidf_similarity_percentage":
            tfidf_similarity,

        "semantic_matching":
            semantic_result
    }