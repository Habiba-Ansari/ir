import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# download once (comment after first run)
nltk.download('punkt')
nltk.download('stopwords')

# Step 1: read file
with open("input.txt", "r") as f:
    text = f.read()

# Step 2: tokenize
words = word_tokenize(text)

# Step 3: remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [w for w in words if w.lower() not in stop_words]

# Step 4: save to output file
with open("output.txt", "w") as f:
    f.write(" ".join(filtered))

# print result
print(filtered)
