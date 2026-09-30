import string


def read_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def clean_job_description(text):
    text = text.strip()
    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    return text