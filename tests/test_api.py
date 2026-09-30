import requests

API_URL = "http://127.0.0.1:8000/analyze-resume"
RESUME_PATH = "data/resumes/sample_resume.pdf"


def test_api_returns_success():
    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": """
            We are looking for a Software Engineer
            with experience in Python, SQL, Machine Learning,
            Docker and AWS.
            """
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=120
        )

    assert response.status_code == 200


def test_api_response_is_json():
    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": """
            Software Engineer with Python and SQL experience.
            """
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=120
        )

    assert response.headers["content-type"].startswith(
        "application/json"
    )


def test_api_contains_required_sections():
    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": """
            Software Engineer with Python,
            SQL, Docker and AWS.
            """
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=120
        )

    result = response.json()

    assert result["status"] == "success"
    assert "resume" in result
    assert "ats_analysis" in result
    assert "ai_analysis" in result


def test_api_resume_section():
    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": """
            Software Engineer with Python and SQL.
            """
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=120
        )

    result = response.json()

    assert "filename" in result["resume"]
    assert "analysis" in result["resume"]


def test_api_ats_section():
    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": """
            Software Engineer with Python,
            Java, SQL, Docker and AWS.
            """
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=120
        )

    result = response.json()
    ats = result["ats_analysis"]

    assert "final_ats_score" in ats
    assert "skill_gap_analysis" in ats
    assert "prioritized_skill_gaps" in ats


def test_api_ai_analysis_section():
    with open(RESUME_PATH, "rb") as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": """
            Software Engineer with Python,
            SQL and Machine Learning.
            """
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=120
        )

    result = response.json()
    ai_analysis = result["ai_analysis"]

    assert "resume_analysis" in ai_analysis