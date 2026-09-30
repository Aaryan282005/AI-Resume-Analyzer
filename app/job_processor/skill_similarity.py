from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_skill_similarity(
    resume_skill,
    job_skill
):

    resume_embedding = model.encode(
        [resume_skill]
    )

    job_embedding = model.encode(
        [job_skill]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(float(similarity) * 100, 2)