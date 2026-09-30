from app.ats.skill_score import (
    calculate_exact_skill_score
)

from app.ats.semantic_score import (
    calculate_semantic_skill_score
)

from app.ats.resume_quality_score import (
    calculate_resume_quality_score
)

from app.ats.keyword_score import (
    calculate_keyword_coverage_score
)

from app.ats.final_ats_score import (
    calculate_final_ats_score
)

from app.ats.skill_gap_report import (
    generate_skill_gap_report
)

from app.ats.skill_gap_priority import (
    prioritize_skill_gaps
)


def analyze_ats(
    resume_text,
    job_description,
    resume_profile,
    resume_skills,
    job_skills,
    high_priority_skills,
    medium_priority_skills,
    low_priority_skills
):

    exact_skill_result = (
        calculate_exact_skill_score(
            resume_skills,
            job_skills
        )
    )

    semantic_skill_result = (
        calculate_semantic_skill_score(
            resume_skills,
            job_skills
        )
    )

    keyword_result = (
        calculate_keyword_coverage_score(
            resume_text,
            job_description
        )
    )

    resume_quality_result = (
        calculate_resume_quality_score(
            resume_profile
        )
    )

    final_score = calculate_final_ats_score(
        exact_skill_result,
        semantic_skill_result,
        keyword_result,
        resume_quality_result
    )

    skill_gap_result = (
        generate_skill_gap_report(
            resume_skills,
            job_skills
        )
    )

    prioritized_gaps = (
        prioritize_skill_gaps(
            skill_gap_result["missing_skills"],
            high_priority_skills,
            medium_priority_skills,
            low_priority_skills
        )
    )

    return {
        "final_ats_score": final_score,
        "exact_skill_analysis": exact_skill_result,
        "semantic_skill_analysis": semantic_skill_result,
        "keyword_analysis": keyword_result,
        "resume_quality_analysis": resume_quality_result,
        "skill_gap_analysis": skill_gap_result,
        "prioritized_skill_gaps": prioritized_gaps
    }