from storage import load_snippets, save_snippets
from models import Snippet
from utils import print_snippet

def add_snippet(snippets):
    title = input("Title: ")
    language = input("Language: ")
    tags = input("Tags (comma separated): ").split(",")
    code = input("Code:\n")

    snippet = Snippet(title, code, language, [t.strip() for t in tags])
    snippets.append(snippet)
    save_snippets(snippets)
    print("✅ Snippet added!")

def view_snippets(snippets):
    if not snippets:
        print("No snippets found.")
        return

    for i, s in enumerate(snippets):
        print_snippet(s, i)

def search_snippets(snippets):
    keyword = input("Search keyword: ").lower()

    results = [
        s for s in snippets
        if keyword in s.title.lower() or keyword in s.code.lower()
    ]

    for i, s in enumerate(results):
        print_snippet(s, i)

def filter_by_tag(snippets):
    tag = input("Enter tag: ").lower()

    results = [
        s for s in snippets
        if tag in [t.lower() for t in s.tags]
    ]

    for i, s in enumerate(results):
        print_snippet(s, i)

def delete_snippet(snippets):
    view_snippets(snippets)
    idx = int(input("Enter ID to delete: "))

    if 0 <= idx < len(snippets):
        snippets.pop(idx)
        save_snippets(snippets)
        print("🗑 Deleted successfully!")

def update_snippet(snippets):
    view_snippets(snippets)
    idx = int(input("Enter ID to update: "))

    if 0 <= idx < len(snippets):
        s = snippets[idx]

        s.title = input(f"New title ({s.title}): ") or s.title
        s.language = input(f"New language ({s.language}): ") or s.language
        s.tags = input("New tags (comma): ").split(",") or s.tags
        s.code = input("New code:\n") or s.code

        save_snippets(snippets)
        print("✏️ Updated successfully!")

def menu():
    snippets = load_snippets()

    while True:
        print("\n📌 Snippet Manager")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Filter by Tag")
        print("5. Update")
        print("6. Delete")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_snippet(snippets)
        elif choice == "2":
            view_snippets(snippets)
        elif choice == "3":
            search_snippets(snippets)
        elif choice == "4":
            filter_by_tag(snippets)
        elif choice == "5":
            update_snippet(snippets)
        elif choice == "6":
            delete_snippet(snippets)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()