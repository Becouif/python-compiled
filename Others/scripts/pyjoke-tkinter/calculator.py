import tkinter as tk
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))
def clear_entry():
    entry.delete(0, tk.END)
def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
root = tk.Tk()
root.title("Simple Calculator")
# Entry field
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)
# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=4, height=2, command=lambda t=text: click_button(t))
    button.grid(row=row, column=column)
# Special case for the clear button
clear_button = tk.Button(root, text="C", width=4, height=2, command=clear_entry)
clear_button.grid(row=4, column=1)
# Special case for the equals button
equals_button = tk.Button(root, text="=", width=4, height=2, command=calculate_result)
equals_button.grid(row=4, column=2)
root.mainloop()