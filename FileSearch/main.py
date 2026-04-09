from search import search_files

def main():
    print("🔍 Smart File Search Tool")

    directory = input("Enter directory path: ")
    name = input("Search by name (optional): ")
    ext = input("Extension (e.g., .py) (optional): ")

    min_size = input("Min size KB (optional): ")
    max_size = input("Max size KB (optional): ")

    min_size = float(min_size) if min_size else 0
    max_size = float(max_size) if max_size else float('inf')

    results = search_files(directory, name, ext, min_size, max_size)

    if not results:
        print("❌ No files found.")
        return

    print("\n📊 Results:")
    for file in results:
        print(f"{file['name']} | {file['size_kb']} KB | {file['path']}")

if __name__ == "__main__":
    main()