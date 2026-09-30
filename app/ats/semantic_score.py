from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_semantic_skill_score(
    resume_skills,
    job_skills,
    max_points=30
):

    if not resume_skills or not job_skills:
        return {
            "semantic_match_percentage": 0.0,
            "score": 0.0,
            "max_points": max_points,
            "skill_scores": []
        }


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


    skill_scores = []


    for job_index, job_skill in enumerate(
        job_skills
    ):

        best_resume_index = (
            similarity_matrix[job_index].argmax()
        )

        best_similarity = (
            similarity_matrix[
                job_index
            ][
                best_resume_index
            ]
        )

        best_resume_skill = (
            resume_skills[
                best_resume_index
            ]
        )


        similarity_percentage = (
            float(best_similarity) * 100
        )


        skill_scores.append(
            {
                "job_skill": job_skill,
                "resume_skill": best_resume_skill,
                "similarity": round(
                    similarity_percentage,
                    2
                )
            }
        )


    total_similarity = sum(
        item["similarity"]
        for item in skill_scores
    )


    semantic_match_percentage = (
        total_similarity
        / len(skill_scores)
    )


    score = (
        semantic_match_percentage
        / 100
    ) * max_points


    return {
        "semantic_match_percentage": round(
            semantic_match_percentage,
            2
        ),

        "score": round(
            score,
            2
        ),

        "max_points": max_points,

        "skill_scores": skill_scores
    }