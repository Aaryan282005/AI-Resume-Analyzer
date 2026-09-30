def extract_weaknesses(resume_analysis):

    weaknesses = resume_analysis.get(
        "weaknesses",
        []
    )

    return weaknesses