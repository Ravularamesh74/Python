def print_snippet(snippet, index=None):
    print("\n-----------------------------")
    if index is not None:
        print(f"ID: {index}")
    print(f"Title: {snippet.title}")
    print(f"Language: {snippet.language}")
    print(f"Tags: {', '.join(snippet.tags)}")
    print("Code:\n", snippet.code)
    print("-----------------------------")