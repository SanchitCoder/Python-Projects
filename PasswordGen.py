# RANDOM PASSWORD GENERATOR TOOL IN PYTHON

import random
import string
#
# Step 1: Define the function to generate a random password
def generate_password(length=12, use_digits=True, use_special=True):
    # Define character sets
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    specials = string.punctuation   # !@#$%^&*()_+-=[]{}|;:'",.<>?/

    # Start with letters
    char_pool = letters

    # Include digits if selected
    if use_digits:
        char_pool += digits

    # Include special characters if selected
    if use_special:
        char_pool += specials

    # Ensure that the character pool is not empty
    if not char_pool:
        raise ValueError("No characters available for password generation!")

    # Generate password using random choices from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Step 2: Create a menu to interact with the user
def main():
    print("🔐 Welcome to the Random Password Generator 🔐")

    while True:
        try:
            # Take user input for password preferences
            length = int(input("\nEnter password length (e.g., 8, 12, 16): "))
            use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
            use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

            # Generate the password
            password = generate_password(length, use_digits, use_special)
            print(f"\n✅ Your random password is:\n👉 {password}")

        except ValueError as ve:
            print(f"❌ Error: {ve}")

        # Ask if user wants to generate another
        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thank you for using the Password Generator!")
            break

# Step 3: Run the app
if __name__ == "__main__":
    main()


