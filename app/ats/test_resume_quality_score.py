from resume_quality_score import (
    calculate_resume_quality_score
)


resume_profile = {

    "personal_info": {
        "name": "Sample Candidate",
        "email": "sample@example.com"
    },

    "education": [
        {
            "degree": "B.E. Computer Science"
        }
    ],

    "experience": [
        {
            "role": "Software Developer"
        }
    ],

    "projects": [
        {
            "name": "AI Resume Analyzer"
        }
    ],

    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}


result = calculate_resume_quality_score(
    resume_profile
)


print(
    "========== RESUME QUALITY SCORE =========="
)


print(
    "Quality Percentage:",
    result["quality_percentage"],
    "%"
)


print(
    "ATS Score:",
    result["score"],
    "/",
    result["max_points"]
)


print(
    "\nQuality Checks:"
)


for check, passed in result["checks"].items():

    if passed:

        print(
            "  ✅",
            check
        )

    else:

        print(
            "  ❌",
            check
        )