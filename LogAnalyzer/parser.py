import re

log_pattern = re.compile(
    r'(?P<ip>\S+) .* \[(?P<time>.*?)\] "(?P<method>\S+) (?P<endpoint>\S+) .*" (?P<status>\d+)'
)

def parse_line(line):
    match = log_pattern.search(line)
    if match:
        return {
            "ip": match.group("ip"),
            "time": match.group("time"),
            "method": match.group("method"),
            "endpoint": match.group("endpoint"),
            "status": int(match.group("status"))
        }
    return None