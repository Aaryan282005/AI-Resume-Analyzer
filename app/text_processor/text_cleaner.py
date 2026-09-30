import re


def clean_lines(text):
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    return cleaned_text


def remove_extra_spaces(line):
    words = line.split()
    cleaned_line = " ".join(words)

    return cleaned_line


def extract_emails(text):
    email_pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"

    emails = re.findall(email_pattern, text)

    return emails


def extract_phone_numbers(text):
    phone_pattern = r"\b[6-9]\d{9}\b"

    phone_numbers = re.findall(phone_pattern, text)

    return phone_numbers


def normalize_text(text):
    return text.lower()


def remove_duplicates(items):
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

def preprocess_resume(text):
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        line = remove_extra_spaces(line)

        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    return cleaned_text