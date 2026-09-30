from jd_processor import (
    read_job_description,
    clean_job_description
)

from skill_extractor import (
    extract_skills
)


file_path = "data/jobs/sample_job.txt"

raw_text = read_job_description(file_path)

cleaned_text = clean_job_description(raw_text)

skills = extract_skills(cleaned_text)


print("========== CLEANED JOB DESCRIPTION ==========")
print(cleaned_text)

print("\n========== EXTRACTED SKILLS ==========")

for skill in skills:
    print(skill)