import json


def save_resume_profile(resume_profile, file_path):

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            resume_profile,
            file,
            indent=4
        )


def load_resume_profile(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        resume_profile = json.load(file)

    return resume_profile