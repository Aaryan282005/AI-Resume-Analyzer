from app.resume_parser.resume_builder import build_resume_profile


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
Developed REST APIs using Java and MySQL.

PROJECTS

AI Resume Analyzer
Python, Streamlit, LangChain

Built an AI-based system to analyze resumes.
Extracted skills from resumes.

SKILLS

Python
Java
SQL
Machine Learning
"""


resume_profile = build_resume_profile(resume_text)


print("========== RESUME PROFILE ==========")

print("\nPERSONAL INFORMATION")
print(resume_profile["personal_info"])


print("\nEDUCATION")
print(resume_profile["education"])


print("\nEXPERIENCE")
print(resume_profile["experience"])


print("\nPROJECTS")
print(resume_profile["projects"])


print("\nSKILLS")
print(resume_profile["skills"])