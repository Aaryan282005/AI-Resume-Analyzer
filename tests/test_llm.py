from app.LLM.llm_engine import (
    generate_llm_analysis
)


MOCK_RESUME_ANALYSIS = {
    "overall_assessment": "The resume shows a solid technical foundation.",
    "strengths": [
        "Python",
        "Java",
        "Spring Boot"
    ],
    "weaknesses": [
        "Limited cloud experience"
    ],
    "technical_skills": [
        "Python",
        "Java",
        "SQL",
        "Spring Boot"
    ],
    "experience": [
        "Backend development using Spring Boot"
    ],
    "projects": [
        "Backend application using Spring Boot and MySQL"
    ],
    "improvement_areas": [
        "Gain cloud experience"
    ]
}


MOCK_JOB_RECOMMENDATIONS = {
    "job_alignment_summary": (
        "The resume matches several technical requirements."
    ),
    "matching_strengths": [
        "Python",
        "SQL",
        "Spring Boot"
    ],
    "skill_gaps": [
        "Docker",
        "AWS"
    ],
    "priority_improvements": [
        "Learn Docker and AWS"
    ],
    "resume_customization_tips": [
        "Highlight backend development experience"
    ]
}


def test_llm_engine_returns_result(mocker):

    mocker.patch(
        "app.LLM.llm_engine.analyze_resume_with_gemini",
        return_value=MOCK_RESUME_ANALYSIS
    )

    result = generate_llm_analysis(
        "A Computer Science student with Python and Java."
    )

    assert result is not None
    assert isinstance(result, dict)


def test_llm_engine_contains_resume_analysis(mocker):

    mocker.patch(
        "app.LLM.llm_engine.analyze_resume_with_gemini",
        return_value=MOCK_RESUME_ANALYSIS
    )

    result = generate_llm_analysis(
        "A Computer Science student with Python and Java."
    )

    assert "resume_analysis" in result

    resume_analysis = result[
        "resume_analysis"
    ]

    assert isinstance(
        resume_analysis,
        dict
    )


def test_llm_engine_resume_analysis_has_expected_fields(
    mocker
):

    mocker.patch(
        "app.LLM.llm_engine.analyze_resume_with_gemini",
        return_value=MOCK_RESUME_ANALYSIS
    )

    result = generate_llm_analysis(
        "A Computer Science student with Python and Java."
    )

    resume_analysis = result[
        "resume_analysis"
    ]

    expected_fields = [
        "overall_assessment",
        "strengths",
        "weaknesses",
        "technical_skills",
        "experience",
        "projects",
        "improvement_areas"
    ]

    for field in expected_fields:
        assert field in resume_analysis


def test_llm_engine_with_job_description(mocker):

    mocker.patch(
        "app.LLM.llm_engine.analyze_resume_with_gemini",
        return_value=MOCK_RESUME_ANALYSIS
    )

    mocker.patch(
        "app.LLM.llm_engine.generate_job_recommendations",
        return_value=MOCK_JOB_RECOMMENDATIONS
    )

    resume_text = """
    A Computer Science student with experience
    in Python, Java, SQL and Spring Boot.
    """

    job_description = """
    We are looking for a Software Engineer with
    Python, SQL, Docker and AWS experience.
    """

    result = generate_llm_analysis(
        resume_text,
        job_description
    )

    assert "resume_analysis" in result
    assert "job_recommendations" in result

    recommendations = result[
        "job_recommendations"
    ]

    assert isinstance(
        recommendations,
        dict
    )


def test_llm_engine_job_recommendation_fields(
    mocker
):

    mocker.patch(
        "app.LLM.llm_engine.analyze_resume_with_gemini",
        return_value=MOCK_RESUME_ANALYSIS
    )

    mocker.patch(
        "app.LLM.llm_engine.generate_job_recommendations",
        return_value=MOCK_JOB_RECOMMENDATIONS
    )

    resume_text = """
    A Computer Science student with experience
    in Python, Java, SQL and Spring Boot.
    """

    job_description = """
    We are looking for a Software Engineer with
    Python, SQL, Docker and AWS experience.
    """

    result = generate_llm_analysis(
        resume_text,
        job_description
    )

    recommendations = result[
        "job_recommendations"
    ]

    expected_fields = [
        "job_alignment_summary",
        "matching_strengths",
        "skill_gaps",
        "priority_improvements",
        "resume_customization_tips"
    ]

    for field in expected_fields:
        assert field in recommendations