import requests


API_URL = "http://127.0.0.1:8000/analyze-resume"

RESUME_PATH = "data/resumes/sample_resume.pdf"

JOB_DESCRIPTION = """
We are looking for a Software Engineer with experience
in Python, SQL, Machine Learning, Docker and AWS.
"""


def test_backend_integration():

    with open(
        RESUME_PATH,
        "rb"
    ) as resume_file:

        files = {
            "file": (
                "sample_resume.pdf",
                resume_file,
                "application/pdf"
            )
        }

        data = {
            "job_description": JOB_DESCRIPTION
        }

        response = requests.post(
            API_URL,
            files=files,
            data=data
        )

    print("\n========== BACKEND INTEGRATION TEST ==========")

    print("\nHTTP STATUS:")
    print(response.status_code)

    print("\nAPI RESPONSE:")
    print(response.json())

    assert response.status_code == 200

    result = response.json()

    assert result["status"] == "success"

    assert "resume" in result

    assert "ats_analysis" in result

    assert "ai_analysis" in result

    assert "filename" in result["resume"]

    assert "analysis" in result["resume"]

    print("\n========== TEST RESULT ==========")
    print("Backend integration test passed successfully.")


if __name__ == "__main__":
    test_backend_integration()