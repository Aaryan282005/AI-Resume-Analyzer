from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_skills(resume_skills, job_skills):
    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    return {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }


def calculate_skill_match_percentage(
    matched_skills,
    job_skills
):
    if not job_skills:
        return 0.0

    percentage = (
        len(matched_skills) / len(job_skills)
    ) * 100

    return round(percentage, 2)


def calculate_text_similarity(
    resume_text,
    job_description
):
    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    similarity_score = similarity_matrix[0][1]

    return round(similarity_score * 100, 2)