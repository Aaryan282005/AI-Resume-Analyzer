SECTION_HEADINGS = [
    "skills",
    "technical skills",
    "education",
    "experience",
    "work experience",
    "projects",
    "certifications",
    "achievements",
    "summary",
    "profile"
]

def is_section_heading(line):
    normalized_line = line.strip().lower()

    normalized_line = normalized_line.rstrip(":")

    if normalized_line in SECTION_HEADINGS:
        return True

    return False

def get_section_name(line):
    normalized_line = line.strip().lower()
    normalized_line = normalized_line.rstrip(":")

    if normalized_line in SECTION_HEADINGS:
        return normalized_line

    return None

def extract_sections(text):
    lines = text.splitlines()

    sections = {}

    current_section = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        section_name = get_section_name(line)

        if section_name:
            current_section = section_name

            if current_section not in sections:
                sections[current_section] = []

            continue

        if current_section:
            sections[current_section].append(line)

    return sections