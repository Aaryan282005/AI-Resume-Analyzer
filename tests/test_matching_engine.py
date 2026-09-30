from app.job_processor.matching_engine import (
    analyze_resume_job_match
)


def test_matching_engine_returns_report():
    resume_text = """
    I have experience with Python, Java, SQL,
    Machine Learning and Docker.
    """

    job_description = """
    We are looking for a Software Engineer
    with Python, SQL, Machine Learning and Docker.
    """

    resume_skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "docker"
    ]

    job_skills = [
        "python",
        "sql",
        "machine learning",
        "docker"
    ]

    result = analyze_resume_job_match(
        resume_text,
        job_description,
        resume_skills,
        job_skills
    )

    assert result is not None
    assert isinstance(result, dict)


def test_matching_engine_contains_expected_fields():
    resume_text = """
    Python Java SQL Machine Learning Docker
    """

    job_description = """
    Python SQL Machine Learning Docker
    """

    resume_skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "docker"
    ]

    job_skills = [
        "python",
        "sql",
        "machine learning",
        "docker"
    ]

    result = analyze_resume_job_match(
        resume_text,
        job_description,
        resume_skills,
        job_skills
    )

    expected_fields = [
        "matched_skills",
        "missing_skills",
        "total_required_skills",
        "matched_skill_count",
        "missing_skill_count",
        "skill_match_percentage",
        "tfidf_similarity_percentage",
        "semantic_similarity_percentage"
    ]

    for field in expected_fields:
        assert field in result


def test_matching_engine_identifies_missing_skills():
    resume_text = """
    I know Python and SQL.
    """

    job_description = """
    We require Python, SQL, Docker and AWS.
    """

    resume_skills = [
        "python",
        "sql"
    ]

    job_skills = [
        "python",
        "sql",
        "docker",
        "aws"
    ]

    result = analyze_resume_job_match(
        resume_text,
        job_description,
        resume_skills,
        job_skills
    )

    assert "python" in result["matched_skills"]
    assert "sql" in result["matched_skills"]

    assert "docker" in result["missing_skills"]
    assert "aws" in result["missing_skills"]

    assert result["matched_skill_count"] == 2
    assert result["missing_skill_count"] == 2


def test_matching_engine_skill_percentage():
    resume_text = """
    Python SQL
    """

    job_description = """
    Python SQL Docker AWS
    """

    resume_skills = [
        "python",
        "sql"
    ]

    job_skills = [
        "python",
        "sql",
        "docker",
        "aws"
    ]

    result = analyze_resume_job_match(
        resume_text,
        job_description,
        resume_skills,
        job_skills
    )

    assert result["skill_match_percentage"] == 50.0