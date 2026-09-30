def calculate_final_ats_score(
    exact_skill_result,
    semantic_skill_result,
    keyword_result,
    resume_quality_result
):
    exact_skill_score = exact_skill_result["score"]

    semantic_skill_score = (
        semantic_skill_result["score"]
    )

    keyword_score = keyword_result["score"]

    resume_quality_score = (
        resume_quality_result["score"]
    )

    final_score = (
        exact_skill_score
        + semantic_skill_score
        + keyword_score
        + resume_quality_score
    )

    return {
        "exact_skill_score": round(
            exact_skill_score,
            2
        ),
        "semantic_skill_score": round(
            semantic_skill_score,
            2
        ),
        "keyword_score": round(
            keyword_score,
            2
        ),
        "resume_quality_score": round(
            resume_quality_score,
            2
        ),
        "final_ats_score": round(
            final_score,
            2
        ),
        "max_score": 100
    }