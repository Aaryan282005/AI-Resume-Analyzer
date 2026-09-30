from limitations import (
    get_matching_limitations
)


limitations = get_matching_limitations()


print("========== MATCHING SYSTEM LIMITATIONS ==========")


for number, limitation in enumerate(
    limitations,
    start=1
):

    print(
        str(number) + ".",
        limitation
    )