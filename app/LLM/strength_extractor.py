def extract_strengths(resume_analysis):
    strengths = resume_analysis.get(
        "strengths",
        []
    )

    return strengths