import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    if value in '0123456789':
        entry.insert(tk.END, value)
    elif value in '+-*/' and current and current[-1] not in '+-*/':
        entry.insert(tk.END, value)
    elif value == '.' and '.' not in current.split()[-1]:
        entry.insert(tk.END, value)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to handle key presses
def key_press(event):
    if event.char in '0123456789+-*/.':
        button_click(event.char)
    elif event.keysym in ['Return', 'KP_Enter']:
        calculate()
    elif event.keysym == 'Escape':
        clear()
    elif event.keysym in ['KP_Add', 'KP_Subtract', 'KP_Multiply', 'KP_Divide']:
        button_click(event.keysym[-1])

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Bind key presses to the entry widget
entry.bind('<Key>', key_press)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons dynamically
row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                    command=calculate).grid(row=row, column=col, sticky="nsew")
    elif button == "C":
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                    command=clear).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                    command=lambda b=button: button_click(b)).grid(row=row, column=col, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the main event loop
root.mainloop()