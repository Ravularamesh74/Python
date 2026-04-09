from parser import parse_markdown

INPUT_FILE = "sample.md"
OUTPUT_FILE = "output.html"

def convert():
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    html_content = parse_markdown(lines)

    full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Markdown Output</title>
</head>
<body>
{html_content}
</body>
</html>
"""

    with open(OUTPUT_FILE, "w") as f:
        f.write(full_html)

    print("✅ Conversion complete! Check output.html")

if __name__ == "__main__":
    convert()