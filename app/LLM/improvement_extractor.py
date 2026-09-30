def extract_improvement_suggestions(resume_analysis):

    improvements = resume_analysis.get(
        "improvement_areas",
        []
    )

    return improvements