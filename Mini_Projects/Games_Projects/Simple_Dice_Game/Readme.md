# 🎲 Simple Tkinter Dice Simulator 🎲

A very simple, first-class desktop application to roll a dice, made with Python!

---

## 👋 Hello Friends! Welcome to the Project!

Are you tired of losing your physical Ludo dice? No worries at all! Today, we are going to build a very simple and beautiful **GUI (Graphical User Interface) Dice Simulator** using Python's built-in `tkinter` library.

This project is **100% beginner-friendly**. I will explain everything inch-by-inch, so just sit back, relax, and let's dive into the code!

---

## 📸 Output Screenshot

When you run the program, you will see a cute little window like this:

> A clean window with a text label, an entry box to show the number, and a **"Roll"** button that turns black when you hover your mouse over it!

---

## 🧠 Code Explanation: Inch by Inch

Let's break down the logic behind our `dice.py` file. What exactly is happening under the hood? Let's see!

---

### Step 1: Importing the Required Tools

First of all, we need to bring our tools into the workshop.

```python
from tkinter import *
import random
```

- `from tkinter import *` — `tkinter` is Python's standard tool to create GUI applications. We are importing everything (`*`) from it so we can use buttons, labels, and windows without any doubt.
- `import random` — We need this module to generate a random number (just like a real dice throws a random face).

---

### Step 2: The Main Logic (Rolling the Dice)

Now, we create a function that will do the actual magic when we click the button.

```python
def roll():
    r = random.randint(1, 6)  # Pick a random number from 1 to 6
    s = str(r)                # Convert that number into a string (text)
    e.delete(0, END)          # Clear whatever is already written in the box
    e.insert(0, s)            # Put our new random number into the box
```

**Tension-free logic:** Generate number → Convert to string → Clear old output → Show new output. Simple!

---

### Step 3: Adding Some "Masala" (Hover Effects)

To make our application look premium, we are adding hover effects to our button.

```python
def on_enter(event):
    button1.config(fg="black")  # When mouse enters, text color becomes black

def on_leave(event):
    button1.config(fg="green")  # When mouse leaves, text color goes back to green
```

---

### Step 4: Creating the Main Window

Now we will design the physical window that the user will see.

```python
root = Tk()
root.geometry("99x117+1153+210")
root.title("Dice")
```

- `Tk()` — Creates the main window.
- `geometry()` — Sets the fixed size and position of our window on the screen. It is **99×117 pixels** wide and tall!
- `title()` — Gives our window a nice name at the top.

---

### Step 5: Adding the Widgets (Components)

A window is empty without things inside it. Let's add a **Label**, an **Entry** box, and a **Button**.

```python
label   = Label(root, text="Simple Dice", wraplength=100)
e       = Entry(root, width=5)
button1 = Button(root, text="Roll", command=roll, wraplength=100)
```

| Widget     | Purpose |
|------------|---------|
| `Label`    | Displays the static text "Simple Dice". |
| `Entry`    | The small white box where the output number appears. `width=5` keeps it compact. |
| `Button`   | The hero of our app! `command=roll` tells it to run `roll()` on every click. |

---

### Step 6: Binding the Hover Effects

```python
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)
```

This connects our hover functions (`on_enter` and `on_leave`) to the button. It watches exactly where your mouse is!

---

### Step 7: Placing Everything on the Screen

Just creating widgets is not enough — we have to place them neatly. We are using the `.grid()` system for this.

```python
label.grid(row=0, sticky=N)
e.grid(row=2, sticky=N)
button1.grid(row=4, sticky=S)
```

- `sticky=N` — Sticks the widget to the **North (Top)** of the grid cell.
- `sticky=S` — Sticks the widget to the **South (Bottom)** of the grid cell.

---

### Step 8: Keep the Engine Running

```python
root.mainloop()
```

`mainloop()` is an **infinite loop**. It tells the computer to keep displaying the window until the user explicitly clicks the close (**✕**) button. Without this, your app will open and close in 1 millisecond!

---

## 🚀 How to Run the Project?

Very simple! Just follow these steps:

1. Make sure you have **Python** installed on your system.
2. Open your **command prompt** or **terminal**.
3. Navigate to the folder where `dice.py` is saved.
4. Type the following command and hit **Enter**:

```bash
python dice.py
```

5. 🎉 Enjoy rolling the dice!