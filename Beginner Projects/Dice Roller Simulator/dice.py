# Simulate rolling a dice (1–6). Ask the user if they want to roll again.
# Random module, basic loops
# Terminal Based

import random


while True:
    roll = input("Do you want to roll the dice? (yes/no): ").strip().lower()
    if roll == "yes":
        print(f"You rolled a {random.randint(1, 6)}!")
    elif roll == "no":
        print("End!")
        break
    else:
        print("Please enter 'yes' or 'no'.")