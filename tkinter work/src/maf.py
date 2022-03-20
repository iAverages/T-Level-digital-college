import tkinter as tk
from tkinter.ttk import *
import random

root = tk.Tk()
root.geometry("500x500")
root.title("mafs")

## Double lambda so I can pass props into the command
## function for buttons in tkinter
## *_ stops python complaining about passing a prop
## When the function doesnt need one
passProps = lambda func, *x: lambda *_: func(*x)
fromRGB = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'

n1, n2 = [random.randrange(1, 100) for _ in range(2)]

print(n1, n2)

radioFrame = tk.Frame(root, padx=5, pady=5)
selected = tk.IntVar()
rad1 = Radiobutton(radioFrame, text='Addition', value=1, variable=selected)
rad2 = Radiobutton(radioFrame, text='Subtraction', value=2, variable=selected)
rad3 = Radiobutton(radioFrame,
                   text='Multiplication',
                   value=3,
                   variable=selected)
rad4 = Radiobutton(radioFrame, text='Division', value=4, variable=selected)

# radioFrame.(row=0, column=2)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)

radioFrame.pack(expand=True)

# .pack(padx=5, pady=5)

btn = Button(root, text="Submit")

root.mainloop()