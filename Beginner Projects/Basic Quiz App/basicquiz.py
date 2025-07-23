# Terminal
# Dictionaries, scoring system
# Ask a set of questions with multiple-choice answers. Score the user's answers and show the final score.

que = {
    1:"What is the capital of France?",
    2:"Which planet is known as the Red Planet?",
    3:"What is the largest mammal in the world?",
    4:"Who wrote Romeo and Juliet?",
    5:"Which gas do plants absorb from the atmosphere?",
    6:"What is the square root of 64?",
    7:"Which continent is the Sahara Desert located on?",
    8:"Which ocean is the largest?",
    9:"Who painted the Mona Lisa?",
    10:"What do bees collect from flowers?"
}

ans = {
    1:"Paris",
    2:"Mars",
    3:"Blue Whale",
    4:"William Shakespeare",
    5:"Carbon Dioxide",
    6:"8",
    7:"Africa",
    8:"Pacific",
    9:"Leonardo da Vinci",
    10:"Nectar",
}

options = {
    1: "Berlin, Madrid, Paris, Rome",
    2: "Earth, Mars, Venus, Jupiter",
    3: "Elephant, Blue Whale, Giraffe, Great White Shark",
    4: "Charles Dickens, William Shakespeare, Mark Twain, Jane Austen",
    5: "Oxygen, Nitrogen, Carbon Dioxide, Hydrogen",
    6: "6, 7, 8, 9",
    7: "Asia, South America, Africa, Australia",
    8: "Atlantic, Pacific, Indian, Arctic",
    9: "Vincent van Gogh, Pablo Picasso, Leonardo da Vinci, Claude Monet",
    10: "Water, Nectar, Dust, Seeds",
}

score = 0

for i in que:
    print(que[i])
    answ = input(f"Enter your answer: {options[i]}: ")
    if ans[i].lower() == answ.lower():
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer...")

print(f"Your score is {score}.")