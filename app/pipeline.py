from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)

from app.resume_parser.resume_builder import (
    build_resume_profile
)

from app.resume_parser.validator import (
    validate_resume,
    calculate_validation_score
)

from app.resume_parser.normalizer import (
    normalize_resume_profile
)

from app.resume_parser.json_storage import (
    save_resume_profile
)


def process_resume(pdf_path, output_path):

    raw_text = extract_text_from_pdf(
        pdf_path
    )

    cleaned_text = clean_text(
        raw_text
    )

    resume_profile = build_resume_profile(
        cleaned_text
    )

    validation_report = validate_resume(
        resume_profile
    )

    validation_score = calculate_validation_score(
        validation_report
    )

    normalized_profile = normalize_resume_profile(
        resume_profile
    )

    save_resume_profile(
        normalized_profile,
        output_path
    )

    return {
        "resume_profile": normalized_profile,
        "validation_report": validation_report,
        "validation_score": validation_score
    }