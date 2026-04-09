class Snippet:
    def __init__(self, title, code, language, tags):
        self.title = title
        self.code = code
        self.language = language
        self.tags = tags

    def to_dict(self):
        return {
            "title": self.title,
            "code": self.code,
            "language": self.language,
            "tags": self.tags
        }