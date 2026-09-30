import json
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)

from app.LLM.resume_analyzer import (
    analyze_resume_with_gemini
)

from app.LLM.weakness_extractor import (
    extract_weaknesses
)


pdf_path = "data/resumes/sample_resume.pdf"


raw_text = extract_text_from_pdf(
    pdf_path
)

cleaned_text = clean_text(
    raw_text
)


print("========== ANALYZING RESUME ==========")


analysis = analyze_resume_with_gemini(
    cleaned_text
)


weaknesses = extract_weaknesses(
    analysis
)


print("\n========== RESUME WEAKNESSES ==========")


for number, weakness in enumerate(
    weaknesses,
    start=1
):

    print(
        str(number) + ".",
        weakness
    )


print("\n========== COMPLETE AI ANALYSIS ==========")


print(
    json.dumps(
        analysis,
        indent=4
    )
)