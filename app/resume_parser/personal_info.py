import re


def extract_email(text):
    email_pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"

    match = re.search(email_pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):
    phone_pattern = r"\b[6-9]\d{9}\b"

    match = re.search(phone_pattern, text)

    if match:
        return match.group()

    return None


def extract_name(text):
    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if "@" in line:
            continue

        if re.search(r"\d", line):
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            return line

    return None


def extract_personal_info(text):
    personal_info = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text)
    }

    return personal_info