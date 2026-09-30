KNOWN_SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "spring boot",
    "docker",
    "git",
    "mysql",
    "mongodb",
    "tensorflow",
    "pytorch",
    "javascript",
    "html",
    "css",
    "data science"
]
def extract_skills(text):
    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills