from app.resume_parser.personal_info import extract_personal_info


resume_text = """
Aaryan Thopate
Computer Science - Data Science

Email: aaryan@gmail.com
Phone: 9876543210

SKILLS:
Python
Java
SQL
"""


personal_info = extract_personal_info(resume_text)


print("========== PERSONAL INFORMATION ==========")

print("Name:", personal_info["name"])
print("Email:", personal_info["email"])
print("Phone:", personal_info["phone"])