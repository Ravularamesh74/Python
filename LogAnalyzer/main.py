from parser import parse_line
from analyzer import analyze, filter_by_status
from utils import log

LOG_FILE = "sample.log"

def load_logs():
    logs = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                logs.append(parsed)
    return logs

def save_report(report):
    with open("report.txt", "w") as f:
        for key, value in report.items():
            f.write(f"{key}: {value}\n")

def main():
    log("Loading logs...")
    logs = load_logs()

    log("Analyzing logs...")
    report = analyze(logs)

    print("\n📊 Report:")
    for k, v in report.items():
        print(f"{k}: {v}")

    save_report(report)
    log("Report saved to report.txt")

    # Example filter
    errors_404 = filter_by_status(logs, 404)
    print(f"\n🔍 404 Errors: {len(errors_404)}")

if __name__ == "__main__":
    main()