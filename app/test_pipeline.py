import json

from pipeline import process_resume


pdf_path = "data/resumes/sample_resume.pdf"

output_path = "output/resume_profile.json"


result = process_resume(
    pdf_path,
    output_path
)


print(
    "========== RESUME PROFILE =========="
)

print(
    json.dumps(
        result["resume_profile"],
        indent=4
    )
)


print(
    "\n========== VALIDATION REPORT =========="
)

print(
    json.dumps(
        result["validation_report"],
        indent=4
    )
)


print(
    "\n========== VALIDATION SCORE =========="
)

print(
    json.dumps(
        result["validation_score"],
        indent=4
    )
)


print(
    "\n========== PIPELINE STATUS =========="
)

print(
    "Resume processed successfully."
)