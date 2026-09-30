from app.LLM.llm_engine import generate_llm_analysis


resume_text = """
Aaryan is a Computer Science student with experience
in Python, Java, SQL, Spring Boot and Machine Learning.
He has built backend applications using Spring Boot,
Hibernate and MySQL.
"""


job_description = """
We are looking for a Software Engineer with experience
in Python, SQL, Machine Learning, Docker and AWS.
"""


result = generate_llm_analysis(
    resume_text,
    job_description
)

print("========== LLM ANALYSIS ==========")
print(result)