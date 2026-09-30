from app.resume_parser.personal_info import extract_personal_info
from app.resume_parser.education import extract_education
from app.resume_parser.experience import extract_experience
from app.resume_parser.projects import extract_projects
from app.resume_parser.skill_extractor import analyze_skills


def build_resume_profile(text):

    personal_info = extract_personal_info(text)

    education = extract_education(text)

    experience = extract_experience(text)

    projects = extract_projects(text)

    skills = analyze_skills(text)

    resume_profile = {
        "personal_info": personal_info,
        "education": education,
        "experience": experience,
        "projects": projects,
        "skills": skills
    }

    return resume_profile