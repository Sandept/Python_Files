<p align="center">
  <img src="https://img.icons8.com/color/96/000000/python--v1.png" alt="Python Logo" width="96"/>
</p>

<h1 align="center">🎯 Number Guessing Game</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Game-CLI-orange?style=for-the-badge"/>
</p>

<p align="center">
  A fun and interactive command-line number guessing game built with Python. <br/>
  The computer picks a secret number — can you guess it in just <strong>4 tries</strong>? 🤔
</p>

---

## 📖 Table of Contents

- [About the Game](#-about-the-game)
- [How It Works](#-how-it-works)
- [Code Walkthrough](#-code-walkthrough)
- [Getting Started](#-getting-started)
- [Example Output](#-example-output)
- [Key Concepts](#-key-concepts)

---

## 🕹️ About the Game

This is a classic **Number Guessing Game** where:

- The program secretly picks a **random number between 1 and 10**
- You get **4 chances** to guess the correct number
- After each wrong guess, you get a **hint** (too high or too low)
- Guess correctly and you **win** 🎉

---

## ⚙️ How It Works

```
Start
  │
  ▼
Generate a random number (1–10)
  │
  ▼
Loop: 4 chances
  │
  ├── User inputs a guess
  │       │
  │       ├── Correct? ──► "You Won!" → Exit
  │       ├── Too High? ──► "Number is less than X"
  │       └── Too Low?  ──► "Number is greater than X"
  │
  ▼
End (show remaining chances)
```

---

## 🔍 Code Walkthrough

### Step 1 — Import Required Modules

```python
import random
import time
```

| Module   | Purpose |
|----------|---------|
| `random` | Generates a random integer for the secret number |
| `time`   | Adds a short pause for dramatic effect 🎭 |

---

### Step 2 — Welcome the Player

```python
print('Hello World! Welcome to the game')
time.sleep(2)
```

- Greets the player with a welcome message
- `time.sleep(2)` pauses execution for **2 seconds** to build anticipation

---

### Step 3 — Generate the Secret Number

```python
n = random.randint(1, 10)
print('Number has been generated!!\nYou have 4 chances to guess the number')
```

- `random.randint(1, 10)` picks a **random integer from 1 to 10** (inclusive)
- The player is informed a number has been chosen and they have 4 chances

---

### Step 4 — Set Up the Guess Counter

```python
count = 4
```

- `count` tracks how many guesses remain
- Starts at **4** and decrements after each wrong guess

---

### Step 5 — The Game Loop

```python
while count != 0:
    a = int(input('Guess the number: '))

    if a == n:
        print("Yay! That's right. You won!")
        break
    elif a > n:
        print('The number is less than ', a)
    else:
        print('The number is greater than ', a)
    count -= 1
```

> ⚠️ **Note:** The original source uses `count=-1` which is a bug — it sets `count` to `-1` instead of decrementing it. The correct statement should be `count -= 1`.

| Condition      | Result                              |
|----------------|-------------------------------------|
| `a == n`       | 🎉 Correct! Print win message, break loop |
| `a > n`        | 📉 Hint: actual number is lower     |
| `a < n`        | 📈 Hint: actual number is higher    |

- `break` exits the loop immediately when the correct answer is guessed
- The loop exits naturally when `count` reaches `0`

---

### Step 6 — Show Final Count

```python
print(count)
```

- Prints the remaining guess count after the game ends
- `0` means all guesses were used up; a positive number means the player won with guesses to spare

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed on your machine

### Run the Game

```bash
# Clone or download the file, then run:
python main.py
```

No external libraries needed — only Python's built-in `random` and `time` modules are used!

---

## 🖥️ Example Output

```
Hello World! Welcome to the game
Number has been generated!!
You have 4 chances to guess the number

Guess the number: 5
The number is greater than  5

Guess the number: 8
The number is less than  8

Guess the number: 7
Yay! That's right. You won!
1
```

---

## 💡 Key Concepts

| Concept | Used In |
|---------|---------|
| `random.randint()` | Generating the secret number |
| `time.sleep()` | Adding delay for user experience |
| `while` loop | Repeating guesses up to 4 times |
| `if / elif / else` | Comparing the guess to the secret number |
| `break` | Exiting the loop on a correct guess |
| `int(input())` | Reading and converting user input |

---

## 🐛 Known Bug

In the original code, the line `count=-1` **sets** count to `-1` instead of **decrementing** it. This causes an infinite loop if the player never guesses correctly. 

**Fix:**
```python
# ❌ Bug
count=-1

# ✅ Correct
count -= 1
```

---

<p align="center">Made with ❤️ in Python</p>