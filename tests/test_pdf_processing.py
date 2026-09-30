from app.pdf_processor.pdf_reader import (
    extract_text_from_pdf,
    clean_text
)


PDF_PATH = "data/resumes/sample_resume.pdf"


def test_pdf_text_extraction():
    text = extract_text_from_pdf(PDF_PATH)

    assert text is not None
    assert isinstance(text, str)
    assert len(text.strip()) > 0


def test_pdf_text_cleaning():
    text = extract_text_from_pdf(PDF_PATH)
    cleaned_text = clean_text(text)

    assert cleaned_text is not None
    assert isinstance(cleaned_text, str)
    assert len(cleaned_text.strip()) > 0