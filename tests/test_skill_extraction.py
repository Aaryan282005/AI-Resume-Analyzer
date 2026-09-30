from app.job_processor.skill_extractor import (
    extract_skills
)


def test_extract_known_skills():
    text = """
    I have experience with Python, Java, SQL,
    Docker and MySQL.
    """

    skills = extract_skills(
        text.lower()
    )

    assert "python" in skills
    assert "java" in skills
    assert "sql" in skills
    assert "docker" in skills
    assert "mysql" in skills


def test_extract_multiple_skills():
    text = """
    Python SQL Machine Learning
    Spring Boot Docker Git MySQL
    """

    skills = extract_skills(
        text.lower()
    )

    expected_skills = [
        "python",
        "sql",
        "machine learning",
        "spring boot",
        "docker",
        "git",
        "mysql"
    ]

    for skill in expected_skills:
        assert skill in skills


def test_unknown_skills_are_not_added():
    text = """
    I have experience with Python,
    Quantum Computing and Rocket Engineering.
    """

    skills = extract_skills(
        text.lower()
    )

    assert "python" in skills
    assert "quantum computing" not in skills
    assert "rocket engineering" not in skills