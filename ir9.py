documents={
    1:"python is hard",
    2:"python is dumb",
    3:"singing is hard"
    }

inverted_index ={}

for doc_id, text in documents.items():
    words=text.split()

    for word in words:
        if word not in inverted_index:
            inverted_index[word]=[]
        if doc_id not in inverted_index[word]:
            inverted_index[word].append(doc_id)
    for word, docs in inverted_index.items():
        print(word, ":", docs)
ordered_list=sorted(inverted_index)
print(ordered_list)

for word in ordered_list:
    print(f'{word}:{inverted_index[word]}')

query= input("enter: ").lower().split()
result_docs = None
for word in query:
    if word in inverted_index:
        if result_docs is None:
            result_docs=inverted_index[word]
        else:
            result_docs = set()
            break
if result_docs:
    print(sorted(result_docs))
else:
    print("Not found")
