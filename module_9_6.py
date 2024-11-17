def all_variants(text: str):
    length = len(text)
    for x in range(1, length + 1):
        for j in range(length - x + 1):
            yield text[j:j + x]

a = all_variants("abc")
for i in a:
    print(i)

