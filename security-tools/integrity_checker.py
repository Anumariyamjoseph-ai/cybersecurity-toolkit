import hashlib
import json
import os

HASH_STORE = "security-tools/file_hashes.json"

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_hashes():
    if os.path.exists(HASH_STORE):
        with open(HASH_STORE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_STORE, "w") as f:
        json.dump(hashes, f, indent=2)

def track_file(filepath):
    hashes = load_hashes()
    hashes[filepath] = get_file_hash(filepath)
    save_hashes(hashes)
    print(f"Now tracking: {filepath}")

def check_file(filepath):
    hashes = load_hashes()
    if filepath not in hashes:
        print(f"{filepath} is not being tracked yet.")
        return
    current_hash = get_file_hash(filepath)
    if current_hash == hashes[filepath]:
        print(f"{filepath}: UNCHANGED ✓")
    else:
        print(f"{filepath}: MODIFIED ⚠ — file has changed since last check!")

if __name__ == "__main__":
    print("1. Track a new file")
    print("2. Check a tracked file")
    choice = input("Choose (1 or 2): ")
    filepath = input("Enter file path: ")

    if choice == "1":
        track_file(filepath)
    elif choice == "2":
        check_file(filepath)