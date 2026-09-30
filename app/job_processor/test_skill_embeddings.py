from skill_embeddings import (
    generate_skill_embeddings
)


skills = [
    "Python",
    "Machine Learning",
    "SQL"
]


embeddings = generate_skill_embeddings(skills)


print("========== SKILLS ==========")

for skill in skills:
    print(skill)


print("\n========== EMBEDDING SHAPES ==========")

print(embeddings.shape)