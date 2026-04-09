from collections import defaultdict
from utils import tokenize

def search(query, index):
    words = tokenize(query)
    scores = defaultdict(int)

    for word in words:
        if word in index:
            for doc, freq in index[word].items():
                scores[doc] += freq

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked