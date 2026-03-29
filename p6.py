from collections import Counter
import math

def cosine_similarity(t1, t2):
    # Step 1: split words
    words1 = t1.split()
    words2 = t2.split()

    # Step 2: count frequency
    c1 = Counter(words1)
    c2 = Counter(words2)

    # Step 3: common words
    common = set(c1.keys()) & set(c2.keys())

    # Step 4: dot product
    dot = sum(c1[w] * c2[w] for w in common)

    # Step 5: magnitude
    mag1 = math.sqrt(sum(v*v for v in c1.values()))
    mag2 = math.sqrt(sum(v*v for v in c2.values()))

    # Step 6: similarity
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1 * mag2)


# Example
t1 = "this is a cat"
t2 = "this is a dog"

print(cosine_similarity(t1, t2))
