import re

def check_password_strength(password):

    min_length = 8
    exists_uppercase = any(char.isupper() for char in password)
    exists_lowercase = any(char.islower() for char in password)
    exists_digit = any(char.isdigit() for char in password)
    exists_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))


    strength = 0
    if len(password) >= min_length:
        strength += 1
    if exists_uppercase:
        strength += 1
    if exists_lowercase:
        strength += 1
    if exists_digit:
        strength += 1
    if exists_special:
        strength += 1


    if strength <= 2:
        classification = "Weak"
    elif strength == 3 or strength == 4:
        classification = "Moderate"
    else:
        classification = "Strong"

    # Provide feedback
    suggestion = []
    if len(password) < min_length:
        suggestion.append(f"- Password should be at least {min_length} characters long.")
    if not exists_uppercase:
        suggestion.append("- Add at least one uppercase letter.")
    if not exists_lowercase:
        suggestion.append("- Add at least one lowercase letter.")
    if not exists_digit:
        suggestion.append("- Include at least one number.")
    if not exists_special:
        suggestion.append("- Include at least one special character (e.g., !, @, #).")

    return classification, suggestion

def main():
    print("Password Strength Checker")
    print("=" * 25)
    password = input("Enter your password: ")

    classification, suggestion = check_password_strength(password)

    print(f"\nPassword Strength: {classification}")
    if suggestion:
        print("Suggestions to strengthen your password:")
        for tip in suggestion:
            print(tip)

if __name__ == "__main__":
    main()
