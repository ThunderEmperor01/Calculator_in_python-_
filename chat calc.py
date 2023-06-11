import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Invalid input")

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Calculator")

# Increase window size
window.geometry("300x400")

entry = tk.Entry(window, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

row_num = 1
col_num = 0

for row in buttons:
    for label in row:
        button = tk.Button(window, text=label, width=5, font=('Arial', 14))

        if label == '=':
            button.configure(command=calculate)
        elif label == '0':
            button.configure(command=lambda digit=label: entry.insert(tk.END, digit))
        else:
            button.configure(command=lambda digit=label: entry.insert(tk.END, digit))

        button.grid(row=row_num, column=col_num, padx=5, pady=5)
        col_num += 1

    row_num += 1
    col_num = 0

clear_button = tk.Button(window, text="Clear", width=20, font=('Arial', 14), command=clear)
clear_button.grid(row=row_num, column=0, columnspan=4, padx=10, pady=10)

window.mainloop()
