def normalize_text(text):

    if not text:
        return ""

    text = text.strip()

    text = text.lower()

    return text

def normalize_skill(skill):

    if not skill:
        return ""

    skill = skill.strip()

    skill = skill.lower()

    return skill

def normalize_skills(skills):

    normalized = []

    for skill in skills:

        canonical_skill = canonicalize_skill(
            skill
        )

        if (
            canonical_skill
            and canonical_skill not in normalized
        ):
            normalized.append(
                canonical_skill
            )

    return normalized

SKILL_CANONICAL_NAMES = {

    "python": "Python",

    "java": "Java",

    "sql": "SQL",

    "machine learning": "Machine Learning",

    "deep learning": "Deep Learning",

    "spring boot": "Spring Boot",

    "javascript": "JavaScript",

    "html": "HTML",

    "css": "CSS",

    "c++": "C++",

    "c#": "C#",

    "mysql": "MySQL",

    "mongodb": "MongoDB",

    "tensorflow": "TensorFlow",

    "pytorch": "PyTorch",

    "langchain": "LangChain"
}

def canonicalize_skill(skill):

    normalized = normalize_skill(skill)

    if normalized in SKILL_CANONICAL_NAMES:

        return SKILL_CANONICAL_NAMES[
            normalized
        ]

    return skill.strip()

def normalize_resume_profile(resume_profile):

    normalized_profile = resume_profile.copy()

    skills = resume_profile.get(
        "skills",
        []
    )

    normalized_profile["skills"] = (
        normalize_skills(skills)
    )

    return normalized_profile