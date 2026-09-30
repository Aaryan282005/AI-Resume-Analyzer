from app.resume_parser.section_detector import is_section_heading


test_lines = [
    "SKILLS",
    "Education",
    "PROJECTS",
    "Python",
    "Aaryan Thopate",
    "Java"
]


for line in test_lines:

    result = is_section_heading(line)

    print(line, "→", result)