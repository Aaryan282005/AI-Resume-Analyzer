from app.resume_parser.resume_builder import (
    build_resume_profile
)

from app.resume_parser.normalizer import (
    normalize_resume_profile
)


resume_text = """
Aaryan Thopate
aaryan@example.com
9876543210

EDUCATION

B.E. Computer Science

SKILLS

Python
python
PYTHON
Java
java
SQL
sql
Spring Boot
spring boot
"""


resume_profile = build_resume_profile(
    resume_text
)


print("========== ORIGINAL PROFILE ==========")

print(resume_profile)


normalized_profile = (
    normalize_resume_profile(
        resume_profile
    )
)


print(
    "\n========== NORMALIZED PROFILE =========="
)

print(normalized_profile)