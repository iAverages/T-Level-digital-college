from dis import dis
import os
import random

## Settings
maxGueses = 6

worldListPath = os.path.join(os.path.dirname(__file__),
                             "../../wordlist/words-sorted.txt")
colors = {
    "green": "\u001b[42;1m",
    "yellow": "\u001b[43m",
    # Grey doesnt exist, use black instead
    "grey": "\u001b[40;1m",
    "reset": "\u001b[0m"
}

words = []
with open(worldListPath) as file:
    dupes = 0
    for line in file:
        if line not in words:
            words.append(line.replace("\n", ""))
        else:
            dupes += 1
    if dupes > 0:
        print(f"Found {dupes} duplicated words in wordlist")


class ItemCounter:
    count = {}

    def __init__(self) -> None:
        self.count = {}

    def inc(self, key):
        if key in self.count:
            self.count[key] = self.count[key] + 1
        else:
            self.count[key] = 1

        self.count[key] += 1

    def get(self, key):
        try:
            return self.count[str(key)]
        except KeyError:
            return 0


class TextDisplay:

    text = []
    indent = 0

    def __init__(self, indent) -> None:
        self.text = []
        self.indent = indent

    def add(self, text):
        self.text.append(self.getIndent() + text)

    def getIndent(self):
        return " " * self.indent

    def print(self):
        print("\n".join(self.text))


# list of colors that should have the text color
# changed to "bright black"
changeText = ["yellow"]


def setColor(color, text, addSpace=True):
    space = " " if addSpace else ""
    textFormatted = text
    if (color in changeText):
        # "bright black"
        textFormatted = "\u001b[30;1m" + textFormatted
    return colors[color] + space + textFormatted + space + colors["reset"]


def getInput(text, failText="Please enter something"):
    while True:
        userInput = input(text + ": ")
        if userInput == "" or len(userInput) != (len(words[0])):
            print(failText)
        else:
            return userInput


def getYesNoInput(text, failText="Please enter something"):
    while True:
        userInput = input(text + ":")
        if userInput == "":
            print(failText)
        else:
            return userInput


def randomWord():
    return words[random.randrange(0, len(words) - 1)]


def getScoreColor(num):
    color = "grey"
    if num == 2:
        color = "green"
    elif num == 1:
        color = "yellow"
    scoreDisplay = scoreDisplay + setColor(color, guess[i])


def playGame(wordToGuess):
    guesses = 0
    previousGuesses = []
    while guesses < maxGueses:
        guesses += 1
        print("\n".join(previousGuesses))
        guess = getInput("What is your guess?")

        ## If user guesses correctly
        if guess == wordToGuess:
            previousGuesses.append(
                setColor("green", " ".join(list(wordToGuess))))
            print("\n".join(previousGuesses))
            print("You guessed the word!")
            break

        # 2 = found correct pos
        # 1 = in word wrong pos
        # 0 = not in word
        statuses = [0] * len(guess)
        charsTaken = [False] * len(wordToGuess)

        ## All correct letters in correct positions
        for i in range(0, len(guess)):
            letter = guess[i]
            if wordToGuess[i] == letter:
                statuses[i] = 2
                charsTaken[i] = True

        ## Find all other chars in incorrect position
        for i in range(0, len(guess)):
            letter = guess[i]
            ## Ignore chars alr found
            if statuses[i] == 2:
                continue

            ## Find char if in word that hasnt been found yet
            indexOfPresentChar = 0
            for index in range(0, len(wordToGuess)):
                if wordToGuess[index] == letter and not charsTaken[index]:
                    indexOfPresentChar = index
                    break

            ## If yes set yellow, else set grey
            if (indexOfPresentChar > 0):
                statuses[i] = 1
                charsTaken[indexOfPresentChar] = True
            else:
                statuses[i] = 0

        ## Format guess with colors
        guessScore = []
        for idx in range(0, len(guess)):
            letter = guess[idx]
            color = "grey"
            if (statuses[idx] == 2):
                color = "green"
            elif (statuses[idx] == 1):
                color = "yellow"
            guessScore.append(setColor(color, letter))

        ## Append current guess to all guesses
        previousGuesses.append("".join(guessScore))

    ## If user did not guess the word
    if guesses >= maxGueses:
        print(f"You did not guess the word in under {maxGueses} attmepts")
        print(f"The word was {wordToGuess}")

    playAgain = getYesNoInput("Do you want to play again?")
    if playAgain:
        playGame(randomWord())
    else:
        print("Goodbye!")
        exit(0)


def welcomeMenu():
    menu = TextDisplay(3)
    print("Welcome to wordle\n\n")
    print("HOW TO PLAY")
    menu.add(
        "Each guesss must be a valid 5 letter word. Hit the enter button to submit"
    )
    menu.add(
        "After each guess, the color of the tiles will change to show how close your guess was to the word."
    )
    menu.print()
    examples = TextDisplay(3)
    print("\nEXAMPLES")

    H = setColor("green", "H")
    examples.add(f"{H} A P P Y")
    examples.add("The letter H is in the word and in the correct spot.")

    R = setColor("yellow", "R")
    examples.add(f"B {R} A V E")
    examples.add("The letter R is in the word and in the wrong spot.")

    D = setColor("grey", "D")
    examples.add(f"W O R {D} S")
    examples.add("The letter D is not in the word in any spot.")
    examples.print()

    print("\nStart playing unlimited games of Wordle for FREE")
    playGame(randomWord())


welcomeMenu()