import re

def check_password_strength(password):
    # Initialize the strength score
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine overall strength
    if strength == 5:
        feedback.append("Password strength: Strong")
    elif 3 <= strength < 5:
        feedback.append("Password strength: Medium")
    else:
        feedback.append("Password strength: Weak")

    return feedback

# Example usage
password = input("Enter your password: ")
feedback = check_password_strength(password)
print("\n".join(feedback))
