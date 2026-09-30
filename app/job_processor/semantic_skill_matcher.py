from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_skill_matching(
    resume_skills,
    job_skills,
    strong_threshold=0.75,
    related_threshold=0.50
):

    resume_embeddings = model.encode(
        resume_skills
    )

    job_embeddings = model.encode(
        job_skills
    )

    similarity_matrix = cosine_similarity(
        job_embeddings,
        resume_embeddings
    )

    matched_skills = []
    related_skills = []
    missing_skills = []

    for job_index, job_skill in enumerate(job_skills):

        best_resume_index = similarity_matrix[
            job_index
        ].argmax()

        best_similarity = similarity_matrix[
            job_index
        ][best_resume_index]

        best_resume_skill = resume_skills[
            best_resume_index
        ]

        similarity_percentage = round(
            float(best_similarity) * 100,
            2
        )

        if best_similarity >= strong_threshold:

            matched_skills.append({
                "job_skill": job_skill,
                "resume_skill": best_resume_skill,
                "similarity": similarity_percentage
            })

        elif best_similarity >= related_threshold:

            related_skills.append({
                "job_skill": job_skill,
                "resume_skill": best_resume_skill,
                "similarity": similarity_percentage
            })

        else:

            missing_skills.append({
                "job_skill": job_skill,
                "similarity": similarity_percentage
            })

    return {
        "matched_skills": matched_skills,
        "related_skills": related_skills,
        "missing_skills": missing_skills
    }