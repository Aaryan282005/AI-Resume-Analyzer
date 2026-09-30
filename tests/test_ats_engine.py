from app.api.ats_api import run_ats_analysis


def create_test_resume_profile():
    return {
        "personal_info": {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "9876543210"
        },
        "education": {
            "degree": "Computer Science",
            "institution": "Test University",
            "years": ["2023", "2027"],
            "cgpa": 8.5
        },
        "experience": {
            "job_title": "Software Developer",
            "company": "Test Company",
            "duration": "6 months",
            "description": [
                "Developed backend applications using Python and Java."
            ]
        },
        "projects": [
            {
                "name": "Test Project",
                "description": "Built a software application."
            }
        ],
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Docker"
        ]
    }


def test_ats_engine_returns_result():
    resume_text = """
    Test User is a Computer Science student.
    Skills: Python, Java, SQL and Docker.
    Experience developing backend applications.
    """

    job_description = """
    We are looking for a Software Engineer
    with Python, Java, SQL and Docker skills.
    """

    resume_profile = create_test_resume_profile()

    resume_skills = [
        "python",
        "java",
        "sql",
        "docker"
    ]

    job_skills = [
        "python",
        "java",
        "sql",
        "docker"
    ]

    result = run_ats_analysis(
        resume_text,
        job_description,
        resume_profile,
        resume_skills,
        job_skills
    )

    assert result is not None
    assert isinstance(result, dict)


def test_ats_engine_contains_required_sections():
    resume_text = """
    Test User is a Computer Science student.
    Skills: Python, Java, SQL and Docker.
    Experience developing backend applications.
    """

    job_description = """
    We are looking for a Software Engineer
    with Python, Java, SQL and Docker skills.
    """

    resume_profile = create_test_resume_profile()

    resume_skills = [
        "python",
        "java",
        "sql",
        "docker"
    ]

    job_skills = [
        "python",
        "java",
        "sql",
        "docker"
    ]

    result = run_ats_analysis(
        resume_text,
        job_description,
        resume_profile,
        resume_skills,
        job_skills
    )

    assert "final_ats_score" in result
    assert "exact_skill_analysis" in result
    assert "semantic_skill_analysis" in result
    assert "keyword_analysis" in result
    assert "resume_quality_analysis" in result
    assert "skill_gap_analysis" in result
    assert "prioritized_skill_gaps" in result


def test_ats_score_has_valid_range():
    resume_text = """
    Test User is a Computer Science student.
    Skills: Python, Java, SQL and Docker.
    Experience developing backend applications.
    """

    job_description = """
    We are looking for a Software Engineer
    with Python, Java, SQL and Docker skills.
    """

    resume_profile = create_test_resume_profile()

    resume_skills = [
        "python",
        "java",
        "sql",
        "docker"
    ]

    job_skills = [
        "python",
        "java",
        "sql",
        "docker"
    ]

    result = run_ats_analysis(
        resume_text,
        job_description,
        resume_profile,
        resume_skills,
        job_skills
    )

    final_score_data = result["final_ats_score"]

    final_score = final_score_data["final_ats_score"]
    max_score = final_score_data["max_score"]

    assert 0 <= final_score <= max_score
    assert max_score == 100


def test_ats_engine_identifies_skill_gaps():
    resume_text = """
    Test User has experience with Python and SQL.
    """

    job_description = """
    We need a developer with Python, SQL,
    Docker and AWS.
    """

    resume_profile = create_test_resume_profile()

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

    result = run_ats_analysis(
        resume_text,
        job_description,
        resume_profile,
        resume_skills,
        job_skills
    )

    skill_gap_analysis = result["skill_gap_analysis"]

    assert "python" in skill_gap_analysis["matched_skills"]
    assert "sql" in skill_gap_analysis["matched_skills"]

    assert "docker" in skill_gap_analysis["missing_skills"]
    assert "aws" in skill_gap_analysis["missing_skills"]