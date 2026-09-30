import requests


API_URL = "http://127.0.0.1:8000/analyze-resume"
RESUME_PATH = "data/resumes/sample_resume.pdf"


def test_complete_resume_analysis_workflow():

    job_description = """
    We are looking for a Software Engineer with experience
    in Python, Java, SQL, Machine Learning, Docker and AWS.

    The candidate should have strong backend development
    and problem-solving skills.
    """

    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": job_description
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=180
        )

    # Step 1 — HTTP request succeeded
    assert response.status_code == 200

    # Step 2 — Response is JSON
    result = response.json()

    # Step 3 — Overall API status
    assert result["status"] == "success"

    # Step 4 — Resume processing completed
    assert "resume" in result
    assert "analysis" in result["resume"]

    # Step 5 — ATS processing completed
    assert "ats_analysis" in result

    # Step 6 — AI processing completed
    assert "ai_analysis" in result

    # Step 7 — ATS score exists
    ats_analysis = result["ats_analysis"]

    assert "final_ats_score" in ats_analysis

    final_score = (
        ats_analysis["final_ats_score"]["final_ats_score"]
    )

    assert 0 <= final_score <= 100

    # Step 8 — Skill-gap analysis exists
    assert "skill_gap_analysis" in ats_analysis

    # Step 9 — Gemini resume analysis exists
    ai_analysis = result["ai_analysis"]

    assert "resume_analysis" in ai_analysis

    # Step 10 — Gemini analysis has expected fields
    resume_analysis = ai_analysis["resume_analysis"]

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

    print("\n========== END-TO-END TEST ==========")
    print("HTTP Status:", response.status_code)
    print("ATS Score:", final_score)
    print("Workflow completed successfully.")