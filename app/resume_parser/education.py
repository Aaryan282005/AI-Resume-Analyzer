import re
DEGREE_KEYWORDS = [
    "b.e",
    "b.tech",
    "be",
    "btech",
    "m.e",
    "m.tech",
    "me",
    "mtech",
    "b.sc",
    "bca",
    "m.sc",
    "mca",
    "mba",
    "phd",
    "bachelor",
    "master"
]
def is_degree_line(line):
    normalized_line = line.strip().lower()

    for keyword in DEGREE_KEYWORDS:
        if keyword in normalized_line:
            return True

    return False

def extract_years(text):
    year_pattern = r"\b(?:19|20)\d{2}\b"

    return re.findall(year_pattern, text)

def extract_cgpa(text):
    cgpa_pattern = r"\b(?:cgpa|c\.g\.p\.a)\s*[:\-]?\s*(\d+(?:\.\d+)?)"

    match = re.search(cgpa_pattern, text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None

def extract_percentage(text):
    percentage_pattern = r"\b(?:percentage|percent|marks)\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*%?"

    match = re.search(
        percentage_pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None

def extract_institution(lines):
    institution_keywords = [
        "college",
        "university",
        "institute",
        "school"
    ]

    for line in lines:
        normalized_line = line.strip().lower()

        for keyword in institution_keywords:
            if keyword in normalized_line:
                return line.strip()

    return None

def extract_education(text):
    lines = text.splitlines()

    education = {
        "degree": None,
        "institution": extract_institution(lines),
        "years": extract_years(text),
        "cgpa": extract_cgpa(text),
        "percentage": extract_percentage(text)
    }

    for line in lines:
        if is_degree_line(line):
            education["degree"] = line.strip()
            break

    return education