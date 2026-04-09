from indexer import build_index
from search import search

def main():
    print("🔄 Building index...")
    index = build_index()

    print("✅ Search Engine Ready!")

    while True:
        query = input("\n🔍 Enter search query (or 'exit'): ")

        if query.lower() == "exit":
            break

        results = search(query, index)

        if not results:
            print("❌ No results found.")
        else:
            print("\n📊 Results:")
            for doc, score in results:
                print(f"{doc} (score: {score})")

if __name__ == "__main__":
    main()