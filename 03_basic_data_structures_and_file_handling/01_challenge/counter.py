def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # Your code here
    for fruit in fruits:
        if fruit not in occurrences:
            occurrences[fruit] = 1
        else:
            occurrences[fruit] += 1

    for k, v in occurrences.items():
        print(f"{k}: {v}")

    return occurrences
