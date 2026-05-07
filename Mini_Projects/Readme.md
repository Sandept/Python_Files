# 🔐 Python GUI Password Generator

A lightweight, easy-to-use Desktop Graphical User Interface (GUI) application that generates secure, random passwords and automatically copies them to your clipboard. Built using Python and Tkinter.

## ✨ Features
* **Simple GUI:** Clean and minimalistic user interface.
* **Custom Length:** Choose exactly how long you want your password to be.
* **Highly Secure:** Uses a mix of lowercase, uppercase, numbers, and special characters.
* **Auto-Copy:** Automatically copies the generated password to your clipboard for instant pasting.

## 🛠️ Modules Used
This project relies on the following Python modules:
1. **`tkinter`**: The standard GUI toolkit for Python (comes pre-installed with Python). Used to create the window, buttons, and text fields.
2. **`random`**: A built-in Python module used to generate random selections from our lists of characters.
3. **`pyperclip`**: A cross-platform third-party module used to copy text to the computer's clipboard.

### Prerequisites
Because `pyperclip` is not a standard built-in Python module, you will need to install it before running the script. Open your Command Prompt or Terminal and run:
```bash
pip install pyperclip
```

---

## 📖 Code Explanation: Inch-by-Inch for Beginners

If you are new to Python or Tkinter, here is a detailed breakdown of how this code works behind the scenes!

### 1. Importing the Modules
```python
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
```
* `import random`: Brings in Python's randomizer tools so we can pick random letters and numbers.
* `from tkinter import *`: Imports everything (`*`) from the Tkinter library to build the graphical window.
* `from tkinter import messagebox`: Specifically imports the pop-up box feature from Tkinter to show the final password to the user.
* `import pyperclip`: Brings in the tool that allows Python to talk to your computer's "Copy/Paste" clipboard.

### 2. Setting Up the Main Window
```python
gui = Tk()
gui.title('Password Generator')
gui.geometry('250x200')
gui.resizable(0,0)
```
* `gui = Tk()`: Initializes the main application window and assigns it to the variable `gui`.
* `gui.title(...)`: Sets the text that appears at the top bar of the window.
* `gui.geometry('250x200')`: Sets the initial size of the window to 250 pixels wide by 200 pixels tall.
* `gui.resizable(0,0)`: Prevents the user from maximizing or dragging the edges of the window to resize it (`0,0` means False for both width and height).

### 3. The Core Logic (The `process` function)
```python
def process():
    length = int(string_pass.get())
```
* `def process():`: Defines the function that will run when the "Generator" button is clicked.
* `string_pass.get()`: Grabs the number the user typed into the text box.
* `int(...)`: Converts that input (which is initially treated as text) into a mathematical Integer (a whole number).

```python
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']
    all = lower + upper + num + special
```
* Here, we create four separate lists containing the alphabet, numbers, and allowed special characters.
* `all = ...`: We add all four lists together into one giant master list called `all` that contains every possible character.

```python
    ran = random.sample(all, length)
    password = "".join(ran)
```
* `random.sample(all, length)`: This is the magic! It looks at our giant `all` list and randomly picks unique characters. It picks exactly as many characters as the user requested (`length`).
* `"".join(ran)`: `random.sample` outputs a list (like `['A', '5', '&']`). The `"".join()` command stitches them together into a single, clean text string (like `"A5&"`).

```python
    messagebox.showinfo('Result', 'Your password {} \n\nPassword Copied to Clipboard'.format(password))
    pyperclip.copy(password)
```
* `messagebox.showinfo(...)`: Triggers a pop-up window. The first string ('Result') is the title. The second string is the message. The `{}` acts as a placeholder, and `.format(password)` drops our newly generated password into that placeholder. `\n\n` creates two new lines (Enter key presses) for spacing.
* `pyperclip.copy(password)`: Silently copies the generated password to your computer's clipboard so you can immediately press `Ctrl+V` (or `Cmd+V`) to paste it anywhere.

### 4. Creating the User Interface (Widgets)
```python
string_pass = StringVar()
label = Label(text="Password Length").pack(pady=10)
txt = Entry(textvariable=string_pass).pack()
btn = Button(text="Generator", command=process).pack(pady=10)
```
* `string_pass = StringVar()`: Creates a special Tkinter variable that tracks what the user types into the text entry box.
* `Label(...)`: Creates standard text on the screen.
* `Entry(...)`: Creates the blank text box where the user types the number. We link it to our `string_pass` variable.
* `Button(...)`: Creates the clickable button. `command=process` tells the button to run our `process()` function when clicked.
* `.pack(pady=10)`: `pack()` is Tkinter's way of placing items on the screen. It stacks them vertically in the center. `pady=10` adds a little bit of vertical padding (empty space) above and below the items so they don't look squished.

### 5. Running the Application
```python
gui.mainloop()
```
* This is the engine of the GUI. It tells Python to run an infinite loop, waiting for the user to click buttons or type things. Without this line, the window would open and close instantly.

### 6. Extra / Leftover Code
```python
a = "Pythyon"
print(a)
```
*(Note: This code at the very bottom creates a variable `a` with a typoed string and prints it to the background console. It does not affect the graphical user interface. This is likely leftover test code and can be safely deleted if you want to clean up your script!)*
