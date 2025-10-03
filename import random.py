import random
import string

def generate_password(length):
    # Define possible character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure password length is valid
    if length < 4:
        return "Password length should be at least 4 characters."
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- Main Program ---
try:
    # Ask user for desired password length
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Your generated password is: {password}")
except ValueError:
    print("Please enter a valid number.")
