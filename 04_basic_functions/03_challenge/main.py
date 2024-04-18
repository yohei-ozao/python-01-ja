def unique_substrings(input_string):
    # 「pass」を削除して、ここにコードを書いてください
    substrings = (input_string)
    teststrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            if substrings[i:j] in teststrings:
                break
            teststrings.append(substrings[i:j])
    return teststrings


input_string = "banana"
print(unique_substrings(input_string))
