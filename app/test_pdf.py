from app.pdf_processor.pdf_reader import extract_text_from_pdf, clean_text
from app.resume_parser.resume_builder import build_resume_profile
import json


pdf_path = "data/resumes/sample_resume.pdf"


raw_text = extract_text_from_pdf(pdf_path)

cleaned_text = clean_text(raw_text)


resume_profile = build_resume_profile(cleaned_text)


print("========== RESUME PROFILE ==========")

print(
    json.dumps(
        resume_profile,
        indent=4
    )
)