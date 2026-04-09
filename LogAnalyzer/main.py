import re
from collections import Counter

LOG_FILE = "sample.log"

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
endpoint_pattern = r'\"GET (.*?) HTTP'

def analyze_logs():
    with open(LOG_FILE, "r") as file:
        data = file.readlines()

    ips = []
    endpoints = []
    errors = 0

    for line in data:
        ip = re.search(ip_pattern, line)
        endpoint = re.search(endpoint_pattern, line)

        if ip:
            ips.append(ip.group())

        if endpoint:
            endpoints.append(endpoint.group(1))

        if "404" in line:
            errors += 1

    print("📊 Log Analysis Report")
    print("----------------------")
    print("Top IP:", Counter(ips).most_common(1))
    print("Most Visited Endpoint:", Counter(endpoints).most_common(1))
    print("Total 404 Errors:", errors)

if __name__ == "__main__":
    analyze_logs()