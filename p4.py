def ngram(text, n):
    grams = []

    for i in range(len(text) - n + 1):
        grams.append(text[i:i+n])

    return grams


# Example
text = "hello"
print(ngram(text, 2))
