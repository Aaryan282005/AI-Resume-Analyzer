import re
from app.resume_parser.section_detector import is_section_heading

EXPERIENCE_KEYWORDS = [
    "intern",
    "internship",
    "developer",
    "engineer",
    "software engineer",
    "data scientist",
    "data analyst",
    "machine learning engineer",
    "web developer",
    "backend developer",
    "frontend developer",
    "full stack developer"
]


COMPANY_KEYWORDS = [
    "pvt",
    "private",
    "ltd",
    "limited",
    "technologies",
    "technology",
    "solutions",
    "systems",
    "services",
    "inc",
    "corp",
    "corporation"
]


def is_job_title(line):
    normalized_line = line.strip().lower()

    for keyword in EXPERIENCE_KEYWORDS:
        if keyword in normalized_line:
            return True

    return False


def extract_date_range(text):
    date_pattern = (
        r"\b("
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
        r"[a-z]*\s+\d{4}"
        r")"
        r"\s*[-–]\s*"
        r"\b("
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
        r"[a-z]*\s+\d{4}|"
        r"Present"
        r")\b"
    )

    match = re.search(
        date_pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return None


def extract_company(lines):
    for line in lines:
        normalized_line = line.strip().lower()

        for keyword in COMPANY_KEYWORDS:
            if keyword in normalized_line:
                return line.strip()

    return None


def extract_description(lines, job_title, company, duration):
    description = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if is_section_heading(line):
            continue

        if line == job_title:
            continue

        if company and line == company:
            continue

        if duration and line == duration:
            continue

        description.append(line)

    return description


def extract_experience(text):
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    job_title = None

    for line in cleaned_lines:
        if is_job_title(line):
            job_title = line
            break

    company = extract_company(cleaned_lines)

    duration = extract_date_range(text)

    description = extract_description(
        cleaned_lines,
        job_title,
        company,
        duration
    )

    experience = {
        "job_title": job_title,
        "company": company,
        "duration": duration,
        "description": description
    }

    return experience