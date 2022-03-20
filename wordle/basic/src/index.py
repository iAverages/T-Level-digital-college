import random 

colors = {
    "green": "\u001b[42;1m",
    "yellow": "\u001b[43m",
    # Grey doesnt exist, use black instead
    "grey": "\u001b[40;1m",
    "reset": "\u001b[0m"
}

words = [
    "which",
    "there",
    "their",
    "about",
    "would",
    "these",
    "other",
    "words",
    "could",
    "write",
    "first",
    "water"
]
# word = words[random.randrange(0, len(words) - 1)]
word = "gamer"

# list of colors that should have the text color 
# changed to "bright black"
changeText = ["yellow"]
def setColor(color, text, addSpace = True):
    space = " " if addSpace else ""
    textFormatted = text
    if (color in changeText):
        # "bright black"
        textFormatted = "\u001b[30;1m" + textFormatted
    return colors[color] + space + textFormatted + space + colors["reset"]

def printc(*text): 
    print(*text, colors["reset"])

def getInput(text, failedText):
    while True:
        userInput = input(text + ": ")
        if userInput == "" or len(userInput) != 5:
            print(failedText)
        else:
            return userInput

def calculateCorrect(word, guess):
    check = [0] * 5
    for i in range(len(guess)):
        char = guess[i]
        if char == word[i]:
            check[i] = 2
        elif char in word:
            check[i] = 1
        else: 
            check[i] = 0
    return check

while True:
    guess = getInput(
        "Please enter your guess", 
        "Please enter a word that is 5 characers long"
    )

    if guess == word:
        printc(setColor("green", word))
        print("You got guessed the word correctly")
        break
    checkedGuess = calculateCorrect(word, guess)
    displayChecked = ""
    numCorrect = 0

    for i in range(len(checkedGuess)):
        num = checkedGuess[i]
        guessChar = guess[i]
        if num == 2:
            displayChecked += setColor("green", guessChar)
        elif num == 1:
            displayChecked += setColor("yellow", guessChar)
        else:
            displayChecked += setColor("grey", guessChar)
    print(displayChecked)