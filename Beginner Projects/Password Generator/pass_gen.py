# Terminal Based
# Generate a strong password based on user-defined length and character types (letters, numbers, symbols).
# Random, strings, secrets module

import secrets
import string


while True:
    length = int(input("Enter the length of password: "))
    if length != 0:
        a = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(a) for i in range(length))

        print(f"Your new password is: {password}")

    else:
        print("Quitting...")
        break