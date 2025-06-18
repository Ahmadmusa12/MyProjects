import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character types selected"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("🔐 Strong Password Generator 🔐")
    try:
        length = int(input("Enter password length (e.g. 12): "))
    except ValueError:
        print("❌ Invalid input. Using default length of 12.")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\n🧾 Your secure password:\n{password}")

if __name__ == "__main__":
    main()

