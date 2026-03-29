def create_index(docs):
    index = {}

    for i, doc in enumerate(docs):
        words = doc.split()

        for word in words:
            if word not in index:
                index[word] = []
            if i not in index[word]:
                index[word].append(i)

    return index


def search(index, query):
    return index.get(query, [])


# Documents
docs = [
    "this is a cat",
    "this is a dog",
    "cat and dog"
]

# Create index
index = create_index(docs)
print("Inverted Index:", index)

# Search
q = "cat"
print("Documents for", q, ":", search(index, q))
