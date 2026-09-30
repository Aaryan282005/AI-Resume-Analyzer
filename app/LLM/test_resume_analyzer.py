import sys
import os
import json

# Add project's "app" folder to the path so pdf_processor/LLM can be found
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)

from app.LLM.resume_analyzer import (
    analyze_resume_with_gemini
)

# Build an absolute path to the PDF (works regardless of current working directory)
pdf_path = os.path.join(PROJECT_ROOT, "..", "data", "resumes", "sample_resume.pdf")
pdf_path = os.path.abspath(pdf_path)

raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(raw_text)

print("========== SENDING RESUME TO GEMINI ==========")

analysis = analyze_resume_with_gemini(cleaned_text)

print("\n========== STRUCTURED AI ANALYSIS ==========")
print(json.dumps(analysis, indent=4))