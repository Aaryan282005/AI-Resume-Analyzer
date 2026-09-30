from app.resume_parser.resume_builder import build_resume_profile

from app.resume_parser.validator import (
    validate_resume,
    calculate_validation_score
)


resume_text = """
Aaryan Thopate
aaryan@example.com
9876543210

EDUCATION

B.E. Computer Science
Savitribai Phule Pune University
2027

EXPERIENCE

Java Full Stack Intern
ABC Technologies
June 2026 - August 2026

Worked on Spring Boot backend development.

PROJECTS

AI Resume Analyzer
Python, Streamlit, LangChain

Built an AI-based system to analyze resumes.

SKILLS

Python
Java
SQL
Machine Learning
"""


resume_profile = build_resume_profile(
    resume_text
)


validation_report = validate_resume(
    resume_profile
)

validation_score = calculate_validation_score(
    validation_report
)


print("\n========== VALIDATION REPORT ==========")

print(validation_report)


print("\n========== VALIDATION SCORE ==========")

print(validation_score)