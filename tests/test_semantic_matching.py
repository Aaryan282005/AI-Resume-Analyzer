from app.job_processor.semantic_matcher import (
    calculate_semantic_similarity
)


def test_semantic_similarity_returns_number():
    resume_text = """
    I have experience with Python programming
    and machine learning.
    """

    job_description = """
    We need a developer with Python
    and machine learning experience.
    """

    similarity = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    assert similarity is not None
    assert isinstance(similarity, float)


def test_semantic_similarity_is_in_valid_range():
    resume_text = """
    Python SQL Machine Learning
    """

    job_description = """
    Python SQL Machine Learning
    """

    similarity = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    assert 0 <= similarity <= 100


def test_semantically_related_text_has_similarity():
    resume_text = """
    I develop software using Python
    and build machine learning models.
    """

    job_description = """
    The candidate should have experience
    in Python development and machine learning.
    """

    similarity = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    assert similarity > 40