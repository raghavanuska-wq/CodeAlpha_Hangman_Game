import random
words = ["python", "programming", "NLP", "artificial", "intelligence"]
word = random.choice(words)
guesses = ""
turns = 6
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()
    if failed == 0:
        print("Congratulations!🎉You won!")
        break
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong! You have", turns, "more guesses.")
        if turns == 0:
            print("Game Over! The word was:", word)
    