from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)

from app.resume_parser.resume_builder import (
    build_resume_profile
)


PDF_PATH = "data/resumes/sample_resume.pdf"


def get_clean_resume_text():
    raw_text = extract_text_from_pdf(PDF_PATH)
    cleaned_text = clean_text(raw_text)
    return cleaned_text


def test_resume_parser_returns_profile():
    resume_text = get_clean_resume_text()

    resume_profile = build_resume_profile(
        resume_text
    )

    assert resume_profile is not None
    assert isinstance(resume_profile, dict)


def test_resume_profile_contains_required_sections():
    resume_text = get_clean_resume_text()

    resume_profile = build_resume_profile(
        resume_text
    )

    assert "personal_info" in resume_profile
    assert "education" in resume_profile
    assert "experience" in resume_profile
    assert "projects" in resume_profile
    assert "skills" in resume_profile


def test_resume_profile_sections_have_expected_types():
    resume_text = get_clean_resume_text()

    resume_profile = build_resume_profile(
        resume_text
    )

    assert isinstance(
        resume_profile["personal_info"],
        dict
    )

    assert isinstance(
        resume_profile["education"],
        dict
    )

    assert isinstance(
        resume_profile["experience"],
        dict
    )

    assert isinstance(
        resume_profile["projects"],
        list
    )

    assert isinstance(
        resume_profile["skills"],
        list
    )