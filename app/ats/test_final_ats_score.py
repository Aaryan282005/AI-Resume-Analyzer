from final_ats_score import (
    calculate_final_ats_score
)


exact_skill_result = {
    "score": 18.0,
    "match_percentage": 60.0,
    "max_points": 30
}


semantic_skill_result = {
    "score": 22.0,
    "semantic_match_percentage": 73.33,
    "max_points": 30
}


keyword_result = {
    "score": 14.0,
    "coverage_percentage": 70.0,
    "max_points": 20
}


resume_quality_result = {
    "score": 16.0,
    "quality_percentage": 80.0,
    "max_points": 20
}


result = calculate_final_ats_score(
    exact_skill_result,
    semantic_skill_result,
    keyword_result,
    resume_quality_result
)


print(
    "========== FINAL ATS SCORE =========="
)

print(
    "Exact Skill Score:",
    result["exact_skill_score"],
    "/ 30"
)

print(
    "Semantic Skill Score:",
    result["semantic_skill_score"],
    "/ 30"
)

print(
    "Keyword Score:",
    result["keyword_score"],
    "/ 20"
)

print(
    "Resume Quality Score:",
    result["resume_quality_score"],
    "/ 20"
)

print(
    "\nFINAL ATS SCORE:",
    result["final_ats_score"],
    "/",
    result["max_score"]
)