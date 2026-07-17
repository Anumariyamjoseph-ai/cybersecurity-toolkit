import subprocess

def scan_target(target="localhost"):
    print(f"Scanning {target}...\n")
    result = subprocess.run(
        ["nmap", target],
        capture_output=True,
        text=True
    )
    print(result.stdout)

if __name__ == "__main__":
    target = input("Enter target to scan (default: localhost): ") or "localhost"
    scan_target(target)