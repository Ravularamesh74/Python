import os
from collections import defaultdict
from utils import tokenize

def build_index(folder="documents"):
    index = defaultdict(dict)

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        with open(path, "r") as f:
            content = f.read()

        words = tokenize(content)

        for word in words:
            if filename not in index[word]:
                index[word][filename] = 0
            index[word][filename] += 1

    return index