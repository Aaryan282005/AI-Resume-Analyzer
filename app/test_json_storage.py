from app.resume_parser.resume_builder import build_resume_profile

from app.resume_parser.validator import validate_resume

from app.resume_parser.json_storage import (
    save_resume_profile,
    load_resume_profile
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

PROJECTS

AI Resume Analyzer
Python, Streamlit, LangChain

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


print("========== VALIDATION ==========")

print(validation_report)


file_path = "output/resume_profile.json"


save_resume_profile(
    resume_profile,
    file_path
)


print("\nResume profile saved successfully.")


loaded_profile = load_resume_profile(
    file_path
)


print("\n========== LOADED RESUME ==========")

print(loaded_profile)