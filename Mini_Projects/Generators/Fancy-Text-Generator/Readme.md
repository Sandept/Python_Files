# ✨ Fancy Text Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Library-pyfiglet-blueviolet?style=for-the-badge&logo=python&logoColor=white" alt="pyfiglet"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge&logo=windowsterminal&logoColor=white" alt="CLI Tool"/>
  <img src="https://img.shields.io/badge/Difficulty-Beginner%20Friendly-brightgreen?style=for-the-badge" alt="Beginner Friendly"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/>
</p>

<p align="center">
  Transform any plain text into stunning <strong>ASCII art banners</strong> right in your terminal! 🎨<br/>
  Perfect for creating cool headers, announcing projects, or just having fun with text!
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

**Fancy Text Generator** is a lightweight Python CLI tool that converts any text you type into large, bold **ASCII art banners** using the `pyfiglet` library. It greets you with a styled app header and then lets you generate as many banners as you want — simply type, see your art, and choose to repeat or exit.

---

## ✨ Features

- 🎨 Converts **any text** into big, bold ASCII art instantly
- 🖼️ Displays a **styled app banner** on every run using `pyfiglet`
- 🔁 **Repeat mode** — run as many times as you like without restarting
- 🚪 **Clean exit** — graceful program termination using `sys.exit()`
- 🔠 All output is automatically converted to **UPPERCASE** for bold impact
- 👶 Dead simple — only **one external library** required (`pyfiglet`)

---

## ⚙️ How It Works

```
Start
  │
  ▼
run_loop() — starts the main loop
  │
  ▼
┌──────────────────────────────────────────┐
│  ascii_maker()                            │◄─────────────────────┐
│    │                                      │                      │
│    ├─► Prints decorative separator line   │                      │
│    ├─► Renders "A C I I banner" header    │                      │
│    ├─► Prints separator line again        │                      │
│    └─► Prompts: "Enter Your Text:"        │                      │
│             │                             │                      │
│             └─► Converts input to         │                      │
│                 ASCII art (UPPERCASE)     │                      │
│                 and prints it             │                      │
└──────────────────────────────────────────┘                      │
  │                                                                │
  ▼                                                                │
ending()                                                           │
  │                                                                │
  ├── User presses "y" → return True ────────────────────────────┘
  │
  └── Any other key → sys.exit() → Program Ends
```

---

## 📁 Project Structure

```
fancy-text-generator/
│
└── main.py          # Complete application — all logic in one clean file
```

### Function Overview

| Function | Role |
|---|---|
| `ascii_maker()` | Prints the app banner, prompts for text, renders it as ASCII art |
| `ending()` | Asks the user to repeat or quit; returns `True` to continue or exits |
| `run_loop()` | Main loop that calls `ascii_maker()` and `ending()` repeatedly |

---

## 🚀 Getting Started

### Prerequisites

Make sure **Python 3.x** is installed:

```bash
python --version
# Expected: Python 3.x.x
```

### Install the Required Library

This project uses **`pyfiglet`** — a Python library that converts text to ASCII art fonts.

```bash
pip install pyfiglet
```

### Installation & Run

**Step 1:** Clone or download the project

```bash
git clone https://github.com/your-username/fancy-text-generator.git
cd fancy-text-generator
```

**Step 2:** Install the dependency

```bash
pip install pyfiglet
```

**Step 3:** Run it!

```bash
python main.py
```

---

## 🖥️ Sample Output

```
----------------------------------------------------------------------
    _    ____ ___ ___    _                               
   / \  / ___|_ _|_ _|  | |__   __ _ _ __  _ __   ___ _ __ 
  / _ \| |    | | | |   | '_ \ / _` | '_ \| '_ \ / _ \ '__|
 / ___ \ |___ | | | |   | |_) | (_| | | | | | | |  __/ |   
/_/   \_\____|___|___|  |_.__/ \__,_|_| |_|_| |_|\___|_|   

----------------------------------------------------------------------

Enter Your Text: Hello World

 _   _ _____ _     _     ___   __        _____  ____  _     ____  
| | | | ____| |   | |   / _ \  \ \      / / _ \|  _ \| |   |  _ \ 
| |_| |  _| | |   | |  | | | |  \ \ /\ / / | | | |_) | |   | | | |
|  _  | |___| |___| |__| |_| |   \ V  V /| |_| |  _ <| |___| |_| |
|_| |_|_____|_____|_____\___/     \_/\_/  \___/|_| \_\_____|____/ 


Thanks for using the code :)

Do you want to run the program again? (y for yes) (any key for no): n
```

---

## 🔍 Code Walkthrough

### Step 1 — Import the Libraries

```python
import sys
import pyfiglet
```

| Library | Purpose |
|---|---|
| `sys` | Built-in module used to call `sys.exit()` for a clean program termination |
| `pyfiglet` | Third-party library that renders text strings as large ASCII art fonts |

> 💡 `sys` comes with Python — no install needed. `pyfiglet` must be installed via `pip install pyfiglet`.

---

### Step 2 — `ascii_maker()` — Display the Banner & Convert Text

```python
def ascii_maker():
    print('-' * 70)
    ascii_banner = pyfiglet.figlet_format("A C I I banner").upper()
    print(ascii_banner)
    print('-' * 70)

    text = input("\nEnter Your Text: ")
    banner = pyfiglet.figlet_format(f"{text}").upper()
    print(banner)
```

**Line-by-line breakdown:**

| Line | What it does |
|---|---|
| `print('-' * 70)` | Prints a horizontal divider — `'-' * 70` repeats the `-` character 70 times |
| `pyfiglet.figlet_format("A C I I banner")` | Converts the static app title text into ASCII art |
| `.upper()` | Converts all letters to uppercase for a bold, impactful look |
| `input("\nEnter Your Text: ")` | Prompts the user to type any text they want converted |
| `pyfiglet.figlet_format(f"{text}")` | Converts the user's input into ASCII art using an f-string |

> 💡 An **f-string** (`f"{text}"`) is a Python string that embeds a variable's value directly inside it. `f"{text}"` is equivalent to just passing `text` directly.

---

### Step 3 — `ending()` — Ask to Repeat or Quit

```python
def ending():
    print("\n\nThanks for using the code :)\n")
    a = input("Do you want to run the program again? (y for yes) (any key for no): ")
    if a.lower() == 'y':
        return True
    else:
        sys.exit()
```

**How it works:**

| Part | What it does |
|---|---|
| `a.lower()` | Converts the user's input to lowercase so `"Y"` and `"y"` both work |
| `return True` | Signals the loop in `run_loop()` to continue |
| `sys.exit()` | Immediately and cleanly terminates the entire program |

> 💡 `sys.exit()` is the proper Python way to stop a program. It raises a `SystemExit` exception internally, which cleanly closes the app.

---

### Step 4 — `run_loop()` — The Main Control Loop

```python
def run_loop():
    while True:
        ascii_maker()
        if not ending():
            break

run_loop()
```

**How it works:**

| Part | What it does |
|---|---|
| `while True:` | Runs forever until explicitly stopped — an infinite loop |
| `ascii_maker()` | Calls the banner display and text conversion each cycle |
| `if not ending():` | Calls `ending()` — if it returns `True` (user chose `y`), `not True` = `False`, loop continues |
| `break` | Safety net to exit the loop if `ending()` somehow returns a falsy value |
| `run_loop()` | The final line that actually starts the program |

> 💡 In practice, `sys.exit()` inside `ending()` handles all exits, so the `break` is a defensive safeguard — a good habit in production code.

---

## 🛠️ Possible Improvements

Here are some fun ideas to take this further:

- [ ] 🎨 **Choose a font** — `pyfiglet` supports 400+ fonts; let users pick one (e.g., `slant`, `block`, `banner3`)
- [ ] 💾 **Save to file** — export the ASCII art to a `.txt` file for sharing
- [ ] 🌈 **Add color** — use the `colorama` or `rich` library to print colorful banners
- [ ] 📋 **List available fonts** — add an option to display all `pyfiglet` font names
- [ ] 🖼️ **Side-by-side preview** — show the same text in multiple fonts at once
- [ ] 🔧 **Fix app title typo** — `"A C I I banner"` in `ascii_maker()` should read `"ASCII banner"`

---

## 📦 Dependencies

| Package | Version | Install |
|---|---|---|
| `pyfiglet` | Latest | `pip install pyfiglet` |

---

## 👨‍💻 Author

Built with ❤️ using Python & pyfiglet.  
Fork it, add your favorite font, and make it yours!

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.