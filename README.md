# 🎮 Hangman Game (Text-Based Python Version)

## 📌 Description
This is a simple **text-based Hangman game** developed in Python for beginners to practice basic programming concepts. 
The game randomly selects a word from a small list of predefined words, and the player must guess the word one letter at a time. 
The player has a maximum of 6 incorrect guesses before the game ends. It's a fun way to reinforce knowledge of loops, conditionals, 
string operations, and list management in Python.

## ✅ Features
- Uses a list of 5 predefined words.
- Allows up to 6 incorrect guesses.
- Real-time word progress display.
- Input validation (only single letters allowed).
- Basic console input/output — no external libraries required.

## 🔧 Technologies Used
- Python 3
- Concepts: `random`, `while` loop, `if-else`, `strings`, `lists`

## ▶️ How to Run
1. Make sure Python is installed on your system.
2. Save the game code in a file named `hangman.py`.
3. Open a terminal or command prompt.
4. Run the script using:

```
python hangman.py
```

## 🖼️ Example Gameplay

```
🎮 Welcome to Hangman Game!
_ _ _ _ _
Guess a letter: a
✅ Good guess!
Word: _ a _ _ _
Attempts left: 6
...
🎉 Congratulations! You guessed the word: mango
```

## 📁 File Structure

```
hangman/
├── hangman.py
└── README.md
```

## 📚 Learning Concepts
- Loop control with `while`
- String manipulation and formatting
- List usage for tracking guessed letters
- Basic user input validation
- Game logic implementation

## 💡 Future Improvements (Optional)
- Allow multiple rounds and scoring
- Add support for full word guessing
- Add ASCII art for hangman graphics