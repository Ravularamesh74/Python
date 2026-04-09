import os
import csv
from extractor import extract_metadata

IMAGE_FOLDER = "images"
OUTPUT_FILE = "report.csv"

def process_images():
    results = []

    for file in os.listdir(IMAGE_FOLDER):
        path = os.path.join(IMAGE_FOLDER, file)

        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            data = extract_metadata(path)
            results.append(data)

    return results

def save_to_csv(data):
    keys = ["filename", "format", "size", "file_size_kb", "camera", "date"]

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

def main():
    print("🔄 Processing images...")
    data = process_images()

    print("📊 Metadata:")
    for d in data:
        print(d)

    save_to_csv(data)
    print(f"\n✅ Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()