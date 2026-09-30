import re


SKILL_KEYWORDS = [
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",

    "html",
    "css",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "spring boot",
    "spring",
    "hibernate",
    "django",
    "flask",
    "fastapi",

    "react",
    "angular",
    "node.js",

    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "opencv",

    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",

    "langchain",
    "faiss",

    "docker",
    "kubernetes",

    "aws",
    "azure",
    "google cloud",

    "git",
    "github"
]


SKILL_DISPLAY_NAMES = {
    "python": "Python",
    "java": "Java",
    "c++": "C++",
    "c#": "C#",
    "javascript": "JavaScript",
    "typescript": "TypeScript",

    "html": "HTML",
    "css": "CSS",

    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",

    "spring boot": "Spring Boot",
    "spring": "Spring",
    "hibernate": "Hibernate",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",

    "react": "React",
    "angular": "Angular",
    "node.js": "Node.js",

    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit-learn": "Scikit-learn",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "opencv": "OpenCV",

    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "natural language processing": "Natural Language Processing",
    "nlp": "NLP",

    "langchain": "LangChain",
    "faiss": "FAISS",

    "docker": "Docker",
    "kubernetes": "Kubernetes",

    "aws": "AWS",
    "azure": "Azure",
    "google cloud": "Google Cloud",

    "git": "Git",
    "github": "GitHub"
}


def extract_skills(text):

    found_skills = []

    normalized_text = text.lower()

    for skill in SKILL_KEYWORDS:

        if skill.lower() in ["c", "c++", "c#"]:

            pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        else:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, normalized_text):

            found_skills.append(skill)

    return found_skills


def remove_duplicate_skills(skills):

    unique_skills = []

    for skill in skills:

        if skill not in unique_skills:

            unique_skills.append(skill)

    return unique_skills


def normalize_skills(skills):

    normalized_skills = []

    for skill in skills:

        display_name = SKILL_DISPLAY_NAMES.get(
            skill.lower(),
            skill
        )

        if display_name not in normalized_skills:

            normalized_skills.append(display_name)

    return normalized_skills


def analyze_skills(text):

    found_skills = extract_skills(text)

    unique_skills = remove_duplicate_skills(found_skills)

    normalized_skills = normalize_skills(unique_skills)

    return normalized_skills