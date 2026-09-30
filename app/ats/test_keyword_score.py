from keyword_score import (
    calculate_keyword_coverage_score
)


resume_text = """
Software developer with experience in
Python, SQL, Docker and Java.

Built backend applications using
Spring Boot and REST APIs.
"""


job_description = """
We are looking for a software engineer
with experience in Python, SQL, Docker,
AWS and Kubernetes.

Experience with REST APIs and Spring Boot
is preferred.
"""


result = calculate_keyword_coverage_score(
    resume_text,
    job_description
)


print(
    "========== KEYWORD ATS SCORE =========="
)

print(
    "Coverage Percentage:",
    result["coverage_percentage"],
    "%"
)

print(
    "ATS Score:",
    result["score"],
    "/",
    result["max_points"]
)


print("\nJob Keywords:")

for keyword in result["job_keywords"]:
    print("  •", keyword)


print("\nMatched Keywords:")

for keyword in result["matched_keywords"]:
    print("  ✅", keyword)


print("\nMissing Keywords:")

for keyword in result["missing_keywords"]:
    print("  ❌", keyword)