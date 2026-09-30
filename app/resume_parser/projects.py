import re


TECHNOLOGY_KEYWORDS = [
    "python",
    "java",
    "c++",
    "c",
    "javascript",
    "typescript",
    "html",
    "css",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "spring boot",
    "hibernate",
    "django",
    "flask",
    "fastapi",
    "react",
    "angular",
    "node.js",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "opencv",
    "streamlit",
    "langchain",
    "faiss",
    "docker",
    "aws",
    "azure",
    "google cloud"
]


def extract_technologies(text):

    technologies = []

    normalized_text = text.lower()

    for technology in TECHNOLOGY_KEYWORDS:

        pattern = r"\b" + re.escape(technology.lower()) + r"\b"

        if re.search(pattern, normalized_text):

            technologies.append(technology)

    return technologies


def is_technology_line(line):

    technologies = extract_technologies(line)

    return len(technologies) > 0


def looks_like_project_name(line):

    words = line.split()

    if len(words) > 8:
        return False

    if line.endswith("."):
        return False

    return True


def extract_projects(text):

    lines = text.splitlines()

    projects = []

    current_project = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.lower() == "projects":
            continue

        if current_project is None:

            current_project = {
                "name": line,
                "technologies": [],
                "description": []
            }

            continue

        if is_technology_line(line):

            technologies = extract_technologies(line)

            for technology in technologies:

                if technology not in current_project["technologies"]:
                    current_project["technologies"].append(technology)

            continue

        if looks_like_project_name(line):

            projects.append(current_project)

            current_project = {
                "name": line,
                "technologies": [],
                "description": []
            }

            continue

        current_project["description"].append(line)

    if current_project:
        projects.append(current_project)

    return projects