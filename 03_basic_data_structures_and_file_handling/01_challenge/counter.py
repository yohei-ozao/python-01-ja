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

    # ここにコードを書いてください
    c_banana = fruits.count("banana")
    c_apple = fruits.count("apple")
    c_orange = fruits.count("orange")
    c_grape = fruits.count("grape")
    c_melon = fruits.count("melon")
    c_kiwi = fruits.count("kiwi")
    c_strawberry = fruits.count("strawberry")
    occurrences = {"banana":str(c_banana), "apple":str(c_apple), "orange":str(c_orange), "grape":str(c_grape), "melon":str(c_melon), "kiwi":str(c_kiwi), "strawberry":str(c_strawberry)}
    for key,value in occurrences.items():
        print(str(key) + ": " + str(value))
    return occurrences

print(counter())
