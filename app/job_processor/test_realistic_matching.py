import sys
import os

# Add project root so "data.jobs..." can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from improved_matching_engine import (
    analyze_improved_match
)

from data.jobs.matching_test_cases import (
    TEST_CASES
)


for case in TEST_CASES:

    print("\n")
    print("=" * 60)
    print(case["name"])
    print("=" * 60)

    result = analyze_improved_match(
        case["resume_text"],
        case["job_description"],
        case["resume_skills"],
        case["job_skills"]
    )


    exact_result = result["exact_matching"]

    semantic_result = result[
        "semantic_matching"
    ]


    print("\nExact Skill Match:")
    print(
        exact_result["percentage"],
        "%"
    )


    print("\nExact Matched Skills:")

    for skill in exact_result[
        "matched_skills"
    ]:
        print("  ✅", skill)


    print("\nExact Missing Skills:")

    for skill in exact_result[
        "missing_skills"
    ]:
        print("  ❌", skill)


    print("\nTF-IDF Similarity:")
    print(
        result[
            "tfidf_similarity_percentage"
        ],
        "%"
    )


    print("\nSemantic Matching:")

    for match in semantic_result[
        "matched_skills"
    ]:
        print(
            "  🟢",
            match["job_skill"],
            "→",
            match["resume_skill"],
            "(",
            match["similarity"],
            "%)"
        )


    for related in semantic_result[
        "related_skills"
    ]:
        print(
            "  🟡",
            related["job_skill"],
            "→",
            related["resume_skill"],
            "(",
            related["similarity"],
            "%)"
        )


    for missing in semantic_result[
        "missing_skills"
    ]:
        print(
            "  🔴",
            missing["job_skill"],
            "(",
            missing["similarity"],
            "%)"
        )