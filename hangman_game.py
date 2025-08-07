import random

# Predefined list of words
word_list = ["toyota", "honda", "ford", 
             "bmw", "audi", "mercedes"]

# Select random word
word = random.choice(word_list)
guessed_letters = []
attempts = 6

print(" Welcome to Hangman Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess!")
    else:
        attempts -= 1
        print(f" Wrong guess! Attempts left: {attempts}")

    # Show current guessed word
    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Win condition
    if all(letter in guessed_letters for letter in word):
        print(" Congratulations! You guessed the word:", word)
        break
else:
    print("Game Over! The word was:", word)
