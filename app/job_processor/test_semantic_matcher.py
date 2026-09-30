from semantic_matcher import (
    calculate_semantic_similarity
)


resume_text = """
I developed predictive models using Python
and worked on data analysis projects.
"""


job_description = """
We are looking for a candidate with
Machine Learning experience and Python skills.
"""


similarity = calculate_semantic_similarity(
    resume_text,
    job_description
)


print("========== SEMANTIC MATCHING ==========")

print("Resume-JD Semantic Similarity:")

print(similarity, "%")