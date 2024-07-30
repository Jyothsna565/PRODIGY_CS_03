import re

def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for a stronger password.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for a stronger password.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers for a stronger password.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters for a stronger password.")

    # Determine strength based on score
    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback

# Main program
while True:
    password = input("Enter a password to check its strength (or 'q' to quit): ")
    if password.lower() == 'q':
        break

    strength, feedback = assess_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great job! Your password meets all the criteria for a strong password.")

    print()  # Add a blank line for readability

print("Thank you for using the password strength checker!")
