from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


resume_text = """
Python developer with experience in SQL and machine learning.
Developed machine learning models using Python.
"""


job_description = """
Looking for a Python developer with experience in SQL
and machine learning.
"""


documents = [
    resume_text,
    job_description
]


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()


# Convert text into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)


# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)


print("========== COSINE SIMILARITY MATRIX ==========")

print(similarity_matrix)


# Resume is row 0
# Job description is row 1

similarity_score = similarity_matrix[0][1]

print("\n========== RESUME-JOB SIMILARITY ==========")

print(similarity_score)

print("\nSimilarity Percentage:")

print(round(similarity_score * 100, 2), "%")