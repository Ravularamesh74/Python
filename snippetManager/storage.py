import json
from models import Snippet

FILE = "snippets.json"

def load_snippets():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Snippet(**item) for item in data]
    except:
        return []

def save_snippets(snippets):
    with open(FILE, "w") as f:
        json.dump([s.to_dict() for s in snippets], f, indent=4)