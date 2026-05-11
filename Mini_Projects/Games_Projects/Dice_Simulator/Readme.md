# 🎲 Dice Simulator

A lightweight, terminal-based dice rolling simulator written in Python. Rolls two dice simultaneously and displays ASCII-art faces for each result — perfect for board games, tabletop RPGs, or just satisfying the urge to roll.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Dice Simulator is a simple Python script that mimics rolling a pair of standard six-sided dice (d6). Each roll randomly selects two dice faces and renders them as ASCII art directly in the terminal. The program loops continuously, prompting the user to roll again until they choose to stop.

---

## Features

- 🎲 **Dual Dice Roll** — Simulates rolling two dice at once per turn
- 🖼️ **ASCII Art Faces** — Visually rendered dice faces for values 1 through 6
- 🔁 **Continuous Play Loop** — Re-roll as many times as desired without restarting
- ⚡ **Zero Dependencies** — Uses only Python's built-in `random` module

---

## Prerequisites

- **Python 3.6+** — No third-party packages required

Verify your Python version:

```bash
python --version
```

---

## Installation

1. **Clone the repository** (or download the file directly):

```bash
git clone https://github.com/your-username/dice-simulator.git
cd dice-simulator
```

2. **Confirm the file is present:**

```bash
ls main.py
```

No virtual environment or package installation is needed.

---

## Usage

Run the simulator from your terminal:

```bash
python main.py
```

**Example session:**

```
This is a dice stimulator

    ("===========")
    ("|  O    O |")
    ("|    0    |")
    ("| O     O |")
    ("===========")

    ("===========")
    ("|         |")
    ("|    O    |")
    ("|         |")
    ("===========")

Press y to roll again: y
```

- Press **`y`** and hit Enter to roll again.
- Press **any other key** (or just Enter) to exit.

---

## Project Structure

```
dice-simulator/
│
├── main.py        # Main script — all logic and ASCII art definitions
└── README.md      # Project documentation
```

---

## How It Works

| Step | Description |
|------|-------------|
| **1. Define faces** | Six multi-line strings (`one` through `six`) represent ASCII art dice faces. |
| **2. Build outcome list** | All six faces are stored in `outcomes_list`. |
| **3. Sample randomly** | `random.sample(outcomes_list, 2)` selects 2 unique faces per roll without repetition. |
| **4. Display results** | Both selected faces are printed to the terminal. |
| **5. Loop** | The user is prompted to continue; the loop exits on any input other than `"y"`. |

---

## License

This project is released under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute it freely.

---

*Built with Python 🐍 — simple, fast, and fun.*