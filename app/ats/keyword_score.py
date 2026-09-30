def calculate_keyword_coverage_score(
    resume_text,
    job_description,
    max_points=20
):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    important_keywords = [
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
        "data science",
        "rest api",
        "aws",
        "kubernetes"
    ]

    job_keywords = []

    for keyword in important_keywords:
        if keyword in job_description:
            job_keywords.append(keyword)

    matched_keywords = []

    for keyword in job_keywords:
        if keyword in resume_text:
            matched_keywords.append(keyword)

    missing_keywords = []

    for keyword in job_keywords:
        if keyword not in resume_text:
            missing_keywords.append(keyword)

    if not job_keywords:
        coverage_percentage = 0.0
    else:
        coverage_percentage = (
            len(matched_keywords)
            / len(job_keywords)
        ) * 100

    score = (
        coverage_percentage
        / 100
    ) * max_points

    return {
        "coverage_percentage": round(
            coverage_percentage,
            2
        ),
        "score": round(
            score,
            2
        ),
        "max_points": max_points,
        "job_keywords": job_keywords,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords
    }