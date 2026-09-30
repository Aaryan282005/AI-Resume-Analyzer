import re


def validate_email(email):

    if not email:
        return False

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.fullmatch(pattern, email))


def validate_phone(phone):

    if not phone:
        return False

    digits = re.sub(r"\D", "", phone)

    pattern = r"^[6-9]\d{9}$"

    return bool(re.fullmatch(pattern, digits))


def validate_name(name):

    if not name:
        return False

    if len(name.strip()) < 2:
        return False

    return True


def validate_education(education):

    if not education:
        return False

    if not isinstance(education, dict):
        return False

    return len(education) > 0


def validate_experience(experience):

    if not experience:
        return False

    if not isinstance(experience, dict):
        return False

    return len(experience) > 0


def validate_projects(projects):

    if not projects:
        return False

    if not isinstance(projects, list):
        return False

    return len(projects) > 0


def validate_skills(skills):

    if not skills:
        return False

    if not isinstance(skills, list):
        return False

    return len(skills) > 0


def validate_resume(resume_profile):

    personal_info = resume_profile.get(
        "personal_info",
        {}
    )

    education = resume_profile.get(
        "education",
        {}
    )

    experience = resume_profile.get(
        "experience",
        {}
    )

    projects = resume_profile.get(
        "projects",
        []
    )

    skills = resume_profile.get(
        "skills",
        []
    )

    name_valid = validate_name(
        personal_info.get("name")
    )

    email_valid = validate_email(
        personal_info.get("email")
    )

    phone_valid = validate_phone(
        personal_info.get("phone")
    )

    education_valid = validate_education(
        education
    )

    experience_valid = validate_experience(
        experience
    )

    projects_valid = validate_projects(
        projects
    )

    skills_valid = validate_skills(
        skills
    )

    validation_report = {

        "personal_info": {
            "name": name_valid,
            "email": email_valid,
            "phone": phone_valid
        },

        "education": education_valid,

        "experience": experience_valid,

        "projects": projects_valid,

        "skills": skills_valid
    }

    return validation_report

def calculate_validation_score(validation_report):

    total = 0
    passed = 0

    personal_info = validation_report["personal_info"]

    for value in personal_info.values():

        total += 1

        if value:
            passed += 1

    sections = [
        "education",
        "experience",
        "projects",
        "skills"
    ]

    for section in sections:

        total += 1

        if validation_report[section]:
            passed += 1

    percentage = (passed / total) * 100

    return {
        "passed": passed,
        "total": total,
        "percentage": round(percentage, 2)
    }