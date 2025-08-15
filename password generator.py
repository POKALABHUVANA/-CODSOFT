import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("enter desired password length:"))
        if length < 4:
            print("password length should be at least 4 for better security.")
            return
        password = generate_password(length)
        print(f"generated password: {password}")
    except valueError:
        print("Invalid input ! Please enter a number.")
main()
