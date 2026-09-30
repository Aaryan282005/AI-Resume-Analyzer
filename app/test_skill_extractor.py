from app.resume_parser.skill_extractor import analyze_skills


resume_text = """
SKILLS

Python
Java
SQL
Machine Learning

PROJECTS

AI Resume Analyzer
Python, Pandas, NumPy, Streamlit, LangChain

EXPERIENCE

Java Full Stack Intern
Spring Boot
Hibernate
MySQL
Docker
"""


skills = analyze_skills(resume_text)


print("========== EXTRACTED SKILLS ==========")

for skill in skills:
    print("-", skill)