import os
from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)
from typing import Any
from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form,
    HTTPException
)
from pydantic import BaseModel
from app.LLM.llm_engine import generate_llm_analysis
from app.pipeline import process_resume
from app.api.ats_api import run_ats_analysis
from app.job_processor.skill_extractor import extract_skills

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend API for AI Resume Analyzer",
    version="1.0.0"
)

class AnalysisResponse(BaseModel):
    status: str
    resume: dict[str, Any]
    ats_analysis: dict[str, Any]
    ai_analysis: dict[str, Any]


class JobRequest(BaseModel):
    job_description: str


@app.get("/")
def root():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Backend is working correctly"
    }


@app.post("/job-description")
def submit_job_description(
    request: JobRequest
):
    return {
        "message": "Job description received successfully",
        "job_description": request.job_description
    }


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    upload_directory = "data/uploads"

    os.makedirs(
        upload_directory,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_directory,
        file.filename
    )

    file_content = await file.read()

    with open(
        file_path,
        "wb"
    ) as output_file:

        output_file.write(
            file_content
        )

    output_path = "output/resume_profile.json"

    resume_result = process_resume(
        file_path,
        output_path
    )

    raw_resume_text = extract_text_from_pdf(
        file_path
    )

    resume_text = clean_text(
        raw_resume_text
    )

    job_description = """
    Software Engineer with Python, SQL,
    Docker, Machine Learning and AWS experience.
    """

    job_skills = [
        "Python",
        "SQL",
        "Docker",
        "Machine Learning",
        "AWS"
    ]

    resume_skills = resume_result[
        "resume_profile"
    ].get(
        "skills",
        []
    )

    ats_result = run_ats_analysis(
        resume_text,
        job_description,
        resume_result["resume_profile"],
        resume_skills,
        job_skills
    )
    llm_result = generate_llm_analysis(
    resume_text,
    job_description
)

    return {
    "message": "Complete resume analysis completed successfully",

    "filename": file.filename,

    "job_description": job_description,

    "job_skills": job_skills,

    "resume_analysis": resume_result,

    "ats_analysis": ats_result,

    "llm_analysis": llm_result
}
@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
) -> AnalysisResponse:

    try:

        upload_directory = "data/uploads"

        os.makedirs(
            upload_directory,
            exist_ok=True
        )

        file_path = os.path.join(
            upload_directory,
            file.filename
        )

        file_content = await file.read()

        with open(
            file_path,
            "wb"
        ) as output_file:

            output_file.write(
                file_content
            )

        output_path = "output/resume_profile.json"

        resume_result = process_resume(
            file_path,
            output_path
        )

        raw_resume_text = extract_text_from_pdf(
            file_path
        )

        resume_text = clean_text(
            raw_resume_text
        )

        job_skills = extract_skills(
            job_description.lower()
        )

        resume_skills = resume_result[
            "resume_profile"
        ].get(
            "skills",
            []
        )

        ats_result = run_ats_analysis(
            resume_text,
            job_description,
            resume_result["resume_profile"],
            resume_skills,
            job_skills
        )

        llm_result = generate_llm_analysis(
            resume_text,
            job_description
        )

        return {
            "status": "success",
            "resume": {
                "filename": file.filename,
                "analysis": resume_result
            },
            "ats_analysis": ats_result,
            "ai_analysis": llm_result
        }

    except Exception as e:
        print(f"Resume analysis failed: {e}")
    raise HTTPException(
        status_code=500,
        detail="Resume analysis failed. Please try again."
    )