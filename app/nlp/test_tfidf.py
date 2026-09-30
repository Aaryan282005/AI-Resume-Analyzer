from sklearn.feature_extraction.text import TfidfVectorizer


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


vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)


print("========== VOCABULARY ==========")

print(vectorizer.get_feature_names_out())


print("\n========== TF-IDF VECTORS ==========")

print(tfidf_matrix.toarray())