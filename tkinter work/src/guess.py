import tkinter as ttk
from tkinter.ttk import *
import random
from turtle import st

numberToGuess = random.randrange(0, 20)
guessCount = 0
totalGuesses = 3
root = ttk.Tk()
root.title("Guess the number")

## Calulate postion to center window
windowHeight = 1000
windowWidth = 500
xCordinate = int((root.winfo_screenwidth() / 2) - (windowWidth / 2))
yCordinate = int((root.winfo_screenheight() / 2) - (windowHeight / 2))
root.geometry(f"{windowWidth}x{ windowHeight}+{ xCordinate}+{yCordinate}")

## Double lambda so I can pass props into the command
## function for buttons in tkinter
## *_ stops python complaining about passing a prop
## When the function doesnt need one
passProps = lambda func, *x: lambda *_: func(*x)
fromRGB = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'

print(f"Number: {numberToGuess}")


def _setBG(color, *props):
    for prop in props:
        try:
            prop.configure(background=fromRGB(*color))
        except:
            pass


def _setFG(color, *props):
    for prop in props:
        try:
            prop.configure(foreground=fromRGB(*color))
        except:
            pass


def getInt(text):
    try:
        return int(text)
    except:
        return None


def handleSubmit(label, text):
    global numberToGuess
    global guessCount
    # default colors
    bgColor = [240, 240, 240]
    fgColor = [0, 0, 0]
    labelText = "You guessed incorrectly"
    userGuess = getInt(text.get())

    # Ignore submit if user has guessed too many times
    if guessCount > totalGuesses: return

    ## Handle no input from user
    if userGuess == None:
        labelText = "Please enter a number between 1 and 20"
        setBG(bgColor)
        setFG(fgColor)
        label.config(text=labelText)
        ## return early to not increase guess count
        return

    guessCount += 1

    if userGuess == numberToGuess:
        labelText = "Well done you guessed the number"
        bgColor = [173, 255, 47]
    else:
        diff = 0
        if userGuess > numberToGuess:
            diff = userGuess - numberToGuess
        else:
            diff = numberToGuess - userGuess

        if diff == 1:
            bgColor = [255, 215, 0]  # orange
            labelText = "Warm"
        else:
            bgColor = [135, 206, 250]  # light blue
            labelText = "Cold"

        if guessCount > totalGuesses:
            labelText = f"You ran out of guesses the number was {numberToGuess}"
            bgColor = [139, 0, 0]
            fgColor = [255, 255, 255]

    setBG(bgColor)
    setFG(fgColor)


frame = ttk.Frame(root)

lbl = Label(frame,
            text="Please enter a number between 1 and 20",
            font=("Cooper", 16))
txt = Entry(frame, width=10)
btn = Button(frame, text="Submit", command=passProps(handleSubmit, lbl, txt))

# Used to set colors on multiple components
toChange = [root, lbl, frame]
setBG = lambda color: _setBG(color, *toChange)
setFG = lambda color: _setFG(color, *toChange)

# Allows user to press enter to submit their answer
txt.bind("<Return>", passProps(handleSubmit, lbl, txt))

# Pack everything
lbl.pack()
txt.pack()
btn.pack()

frame.pack(expand=True)

root.mainloop()
