from collections import defaultdict

LOG_FILE = "security-tools/sample.log"
FAILURE_THRESHOLD = 3

def analyze_log(filepath):
    failed_attempts = defaultdict(int)
    suspicious_ips = set()

    with open(filepath, "r") as f:
        for line in f:
            if "LOGIN FAILED" in line:
                ip = line.split("ip=")[1].strip()
                failed_attempts[ip] += 1

    print("=== Login Analysis Report ===\n")
    for ip, count in failed_attempts.items():
        status = "⚠ SUSPICIOUS — possible brute-force" if count >= FAILURE_THRESHOLD else "Normal"
        print(f"IP: {ip} — Failed attempts: {count} — {status}")
        if count >= FAILURE_THRESHOLD:
            suspicious_ips.add(ip)

    print(f"\nTotal suspicious IPs flagged: {len(suspicious_ips)}")

if __name__ == "__main__":
    analyze_log(LOG_FILE)