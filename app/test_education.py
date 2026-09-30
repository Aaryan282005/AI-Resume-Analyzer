from app.resume_parser.education import extract_education


resume_text = """
Aaryan Thopate

EDUCATION

B.E. Computer Science and Engineering
XYZ College of Engineering
2023 - 2027
CGPA: 8.2
"""


education = extract_education(resume_text)


print("========== EDUCATION ==========")

print("Degree:", education["degree"])
print("Institution:", education["institution"])
print("Years:", education["years"])
print("CGPA:", education["cgpa"])
print("Percentage:", education["percentage"])