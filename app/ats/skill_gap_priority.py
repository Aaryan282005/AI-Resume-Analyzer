def prioritize_skill_gaps(
    missing_skills,
    high_priority_skills,
    medium_priority_skills,
    low_priority_skills
):
    prioritized_gaps = []

    for skill in missing_skills:

        normalized_skill = skill.lower().strip()

        if normalized_skill in [
            item.lower().strip()
            for item in high_priority_skills
        ]:
            priority = "HIGH"

        elif normalized_skill in [
            item.lower().strip()
            for item in medium_priority_skills
        ]:
            priority = "MEDIUM"

        elif normalized_skill in [
            item.lower().strip()
            for item in low_priority_skills
        ]:
            priority = "LOW"

        else:
            priority = "MEDIUM"

        prioritized_gaps.append(
            {
                "skill": skill,
                "priority": priority
            }
        )

    priority_order = {
        "HIGH": 1,
        "MEDIUM": 2,
        "LOW": 3
    }

    prioritized_gaps.sort(
        key=lambda item: priority_order[
            item["priority"]
        ]
    )

    return prioritized_gaps