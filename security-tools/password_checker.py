import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short — use at least 8 characters, ideally 12+")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$ etc.)")

    common_weak = ["password", "123456", "qwerty", "letmein", "admin"]
    if password.lower() in common_weak:
        score = 0
        feedback = ["This is a commonly used weak password — avoid it entirely"]

    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, tips = check_password_strength(pwd)
    print(f"\nStrength: {strength}")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(f" - {tip}")
    else:
        print("No issues found!")