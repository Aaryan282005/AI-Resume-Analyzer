from app.resume_parser.section_detector import extract_sections


resume_text = """
Aaryan Thopate
Computer Science - Data Science

SKILLS:
Python
Java
SQL
Machine Learning

EDUCATION:
B.E. Computer Science
XYZ College

PROJECTS:
AI Resume Analyzer
Placement Management System

CERTIFICATIONS:
Google Cloud
"""


sections = extract_sections(resume_text)


print("========== EXTRACTED SECTIONS ==========")

for section, content in sections.items():

    print("\nSECTION:", section)

    for item in content:
        print("-", item)