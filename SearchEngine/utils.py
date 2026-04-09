import re

STOPWORDS = {"is", "a", "the", "and", "for", "in", "are"}

def tokenize(text):
    words = re.findall(r'\w+', text.lower())
    return [w for w in words if w not in STOPWORDS]