from random import random
from tkinter import *
from tkinter.ttk import *
import random

window = Tk()

randColor = lambda: random.randrange(0, 255)
fromRGB = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'

lbl = Label(window, text="dwda")

txt = Entry(window, width=10)


def handleClick(event=None):
    global lbl
    global txt

    lbl.configure(background=fromRGB(randColor(), randColor(), randColor()), text=f"Hello {txt.get()}")
    window.configure(bg=fromRGB(randColor(), randColor(), randColor()))


window.title("Hello")

window.geometry("500x500")

btn = Button(window, text="Click", command=handleClick).pack()

txt.bind("<Return>", handleClick)
lbl.pack()
txt.pack()

window.mainloop()
