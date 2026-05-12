# 🧮 Math Quiz Game

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Game-orange?style=for-the-badge&logo=windowsterminal&logoColor=white" alt="CLI Game"/>
  <img src="https://img.shields.io/badge/Difficulty-Beginner%20Friendly-brightgreen?style=for-the-badge" alt="Beginner Friendly"/>
  <img src="https://img.shields.io/badge/Module-Random%20%7C%20Operator-purple?style=for-the-badge&logo=python" alt="Modules"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  A fast-paced command-line math quiz that tests your arithmetic skills! 🎯<br/>
  Answer correctly to keep your streak alive — one wrong answer ends the game!
</p>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Sample Output](#-sample-output)
- [Code Walkthrough](#-code-walkthrough)
- [Possible Improvements](#-possible-improvements)

---

## 🧩 About the Project

**Math Quiz Game** is an interactive Python terminal game that generates endless random arithmetic problems. The challenge? Answer as many as you can in a row — the moment you get one wrong, it's game over and your score is displayed. It supports all four basic operations: **addition**, **subtraction**, **multiplication**, and **division**.

---

## ✨ Features

- ➕➖✖️➗ Supports all **4 arithmetic operators** (`+`, `-`, `*`, `/`)
- 🎲 **Randomly generated** problems every round (numbers 1–10)
- 🔢 Accepts **decimal answers** for division problems
- 🛡️ **Error handling** — invalid inputs are caught gracefully and re-prompted
- 🏆 **Score tracker** — counts your correct answers in a row
- 💀 **Survival mode** — one wrong answer ends the game
- 👶 Zero dependencies — only uses Python's **built-in modules**

---

## ⚙️ How It Works

```
Start
  │
  ▼
game() — starts the quiz loop
  │
  ▼
┌────────────────────────────────────────┐
│  ask_question()                         │◄──────────────────────┐
│    │                                    │                       │
│    ├─► random_problem() generates Q     │                       │
│    │     • Picks two random numbers     │                       │
│    │     • Picks a random operator      │                       │
│    │     • Prints the question          │                       │
│    │     • Returns the correct answer   │                       │
│    │                                    │                       │
│    └─► User inputs their answer         │                       │
│          │                              │                       │
│          ├── Valid float? ──────────────┤                       │
│          │                              │                       │
│          └── Invalid? → errorHandle()  │                       │
│               loops until valid input   │                       │
└────────────────────────────────────────┘                       │
  │                                                               │
  ├── Correct ✅ → score += 1 → print "Correct!" ────────────────┘
  │
  └── Wrong ❌ → print "Incorrect" → break
        │
        ▼
  Game Over — display final score
```

---

## 📁 Project Structure

```
math-quiz-game/
│
└── main.py          # The entire application — all logic in one file
```

### Function Overview

| Function | Role |
|---|---|
| `random_problem()` | Generates a random math question, prints it, and returns the correct answer |
| `ask_question()` | Captures user input, calls error handling if needed, returns `True`/`False` |
| `errorHandle(problem_answer)` | Loops until the user enters a valid number |
| `game()` | Main game loop — tracks score, calls `ask_question()`, ends on wrong answer |

---

## 🚀 Getting Started

### Prerequisites

Make sure **Python 3.x** is installed on your machine.

```bash
python --version
# Expected: Python 3.x.x
```

### Installation & Run

**Step 1:** Clone or download the project

```bash
git clone https://github.com/your-username/math-quiz-game.git
cd math-quiz-game
```

**Step 2:** Run the script — no installs needed!

```bash
python main.py
```

---

## 🖥️ Sample Output

```
What is 7 + 3
Enter your answer: 10
Correct !
What is 9 * 4
Enter your answer: 36
Correct !
What is 6 / 2
Enter your answer: abc
Please enter a valid answer: 3.0
Correct !
What is 5 - 8
Enter your answer: 2
Incorrect
======== Game Over ========
Your score is 3
Keep going!
```

---

## 🔍 Code Walkthrough

### Step 1 — Import Built-in Modules

```python
import random
import operator
```

| Module | Purpose |
|---|---|
| `random` | Generates random numbers and picks random operators |
| `operator` | Provides arithmetic functions like `operator.add`, `operator.mul`, etc. |

> 💡 The `operator` module lets us store math operations as values in a dictionary, making it easy to pick one at random.

---

### Step 2 — `random_problem()` — Generate a Question

```python
def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = float(round(operators.get(operation)(num_1, num_2), 3))
    print(f'What is {num_1} {operation} {num_2}')
    return answer
```

**Step-by-step breakdown:**

| Line | What it does |
|---|---|
| `operators = {...}` | A dictionary mapping symbol strings (`"+"`) to actual math functions |
| `random.randint(1, 10)` | Picks a random whole number between 1 and 10 (inclusive) |
| `random.choice(...)` | Picks one operator symbol at random from the dictionary keys |
| `operators.get(operation)(num_1, num_2)` | Calls the matching math function with the two numbers |
| `float(round(..., 3))` | Rounds to 3 decimal places, useful for clean division results |
| `return answer` | Sends the correct answer back to be compared with user input |

---

### Step 3 — `errorHandle()` — Validate User Input

```python
def errorHandle(problem_answer):
    switch = False
    validated_guess = 0.0
    while switch == False:
        try:
            validated_guess = float(input('Please enter a valid answer: '))
            if type(validated_guess) is float:
                switch = True
                break
        except ValueError:
            pass
    return validated_guess
```

**What this does:**

- Runs in a loop until the user enters something that can be converted to a `float`
- If the user types `"abc"` or `"hello"`, `float()` raises a `ValueError`, which is caught by `except ValueError: pass` — it simply re-prompts without crashing
- Once valid input is received, `switch = True` exits the loop

> 💡 **`try / except`** is Python's way of handling errors gracefully. Instead of crashing, the program catches the error and asks again.

---

### Step 4 — `ask_question()` — Run One Round

```python
def ask_question():
    answer = random_problem()
    try:
        guess = float(input('Enter your answer: '))
    except ValueError:
        guess = errorHandle(answer)
    return guess == answer
```

**Step-by-step:**

1. Calls `random_problem()` to generate and display a question, storing the correct answer
2. Tries to read user input as a `float`
3. If input is invalid (e.g., letters typed), falls back to `errorHandle()` which loops until valid
4. Returns `True` if the guess matches the answer, `False` otherwise

> 💡 `return guess == answer` returns a **boolean** — `True` or `False` — by directly comparing two values.

---

### Step 5 — `game()` — The Main Game Loop

```python
def game():
    score = 0
    while True:
        if ask_question() == True:
            score += 1
            print('Correct !')
        else:
            print('Incorrect')
            break
    print(f'======== Game Over ========\nYour score is {score}\nKeep going!')
```

**How it works:**

| Part | Description |
|---|---|
| `score = 0` | Initialises the score counter at zero |
| `while True:` | An infinite loop — keeps running until a `break` is hit |
| `ask_question() == True` | Checks if the user answered correctly |
| `score += 1` | Increments score by 1 for each correct answer |
| `break` | Immediately exits the loop on a wrong answer |
| `f'...'` | An **f-string** — embeds the `score` variable directly inside the string |

---

## 🛠️ Possible Improvements

Here are some ideas to extend the project further:

- [ ] 🎚️ **Difficulty levels** — Easy (1–10), Medium (1–50), Hard (1–100)
- [ ] ⏱️ **Add a timer** — limit each answer to 10 seconds using the `time` module
- [ ] 🏅 **High score tracker** — save the best score to a `.txt` file between sessions
- [ ] 📊 **Show statistics** — track correct vs incorrect answers at the end
- [ ] 🔧 **Fix unused parameter** — `errorHandle(problem_answer)` receives the answer but never uses it; it can be removed or repurposed for a hint system
- [ ] 🎨 **Add color** — use the `colorama` library to color correct answers green and wrong ones red

---

## 👨‍💻 Author

Built with ❤️ using Python.  
Fork it, improve it, and make it your own!

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.