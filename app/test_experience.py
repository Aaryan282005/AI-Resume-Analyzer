from app.resume_parser.experience import extract_experience


resume_text = """
EXPERIENCE

Java Full Stack Intern
ABC Technologies
June 2026 - August 2026

Worked on Spring Boot backend development.
Developed REST APIs using Java and MySQL.
Implemented database operations using Hibernate.
"""


experience = extract_experience(resume_text)


print("========== EXPERIENCE ==========")

print("Job Title:", experience["job_title"])
print("Company:", experience["company"])
print("Duration:", experience["duration"])

print("\nDescription:")

for item in experience["description"]:
    print("-", item)