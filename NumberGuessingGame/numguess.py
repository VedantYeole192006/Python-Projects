import random

num = random.randint(0,100)

guessnum = 0

while True:
    guess = int(input("Guess a number between range of 0 to 100: "))
    
    if guess > 100:
        print("Number is above the limit!")
        continue
    elif num < guess:
        print("Go Lower")
        guessnum += 1
    elif num > guess:
        print("Go Higher")
        guessnum += 1
    else:
        print("You Got It!")
        guessnum += 1
        break

print("You took",guessnum,"guesses")