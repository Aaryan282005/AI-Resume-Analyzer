import pymupdf


def extract_text_from_pdf(pdf_path):
    try:
        document = pymupdf.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text  
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def clean_text(text):
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)    
