from app.resume_parser.projects import extract_projects


resume_text = """
PROJECTS

AI Resume Analyzer
Python, NLP, Streamlit
Built an AI-based system to analyze resumes.
Extracted skills and generated recommendations.

Placement Management System
Java, Spring Boot, Hibernate, MySQL
Developed a backend system for managing student placements.
Created REST APIs for students and companies.
"""


projects = extract_projects(resume_text)


print("========== PROJECTS ==========")


for project in projects:

    print("\nProject Name:", project["name"])

    print("Technologies:")

    for technology in project["technologies"]:
        print("-", technology)

    print("Description:")

    for description in project["description"]:
        print("-", description)