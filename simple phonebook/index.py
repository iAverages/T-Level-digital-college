import json

PHONEBOOK = "phonebook.json"
defaultPhonebook = {"adrian": 8001, "brian": 8002, "charlotte": 8003, "dan": 1234}


def saveDefaults():
    with open(PHONEBOOK, "w") as defFile:
        defFile.write(json.dumps(defaultPhonebook))
        return defaultPhonebook


def savePhonebook():
    with open(PHONEBOOK, "w") as file:
        file.write(json.dumps(phonebook))


try:
    with open(PHONEBOOK, "r") as file:
        phonebook = json.loads(file.read())
except json.JSONDecodeError:
    print("Failed to load phonebook,generating new from default")
    phonebook = saveDefaults()
except FileNotFoundError:
    print("phonebook.json not found, saving defaults")
    phonebook = saveDefaults()


def getEntry(key):
    return (key, phonebook.get(key.lower()))


def nameLookup(name):
    number = phonebook.get(name.lower())
    return f"{name.lower()} - {number}"


def numberLookup(num):
    for name, number in phonebook.items():
        if number == int(num):
            return f"{name} - {number}"
    return None


def addEntry(name, number):
    phonebook[name] = number
    savePhonebook()
    return True


def removeEntry(name, save=True):
    removed = phonebook.pop(name)
    if save == True:
        savePhonebook()
    return removed


def editName(name, newName):
    try:
        number = phonebook.get(name)
        removeEntry(name, False)
        addEntry(newName, number)
        return True
    except:
        return False


def editNumber(name, newNumber):
    return addEntry(name, newNumber)


def addSpace(text, num):
    return text + (" " * (num - len(text)))


def displayPhonebook():
    longest = 0
    for name in phonebook.keys():
        if len(name) > longest:
            longest = len(name)
    header1 = addSpace("Name", longest)
    print(f"{header1} Number")
    for x, y in phonebook.items():
        print(f"{addSpace(x, longest)} {y}")


def menu():
    while True:
        print("Phonebook Application Menu")
        print("1 - Look up name")
        print("2 - Look up number")
        print("3 - Add entry")
        print("4 - Remove entry")
        print("5 - Edit name")
        print("6 - Edit number")
        print("7 - Display phonebook")
        print("8 - Exit")

        userInput = input("Select a function: ")

        try:
            int(userInput)
        except:
            print("Sorry, you did not enter a valid choice")
        else:
            if int(userInput) < 1 or int(userInput) > 8:
                print("Sorry, you did not neter a valid choice")
            else:
                return userInput


def handle(cb, *text):
    userInput = []
    try:
        for t in text:
            userInput.append(input(f"{t}: "))
    except KeyboardInterrupt:
        print("Closing...")
        exit()
    print(cb(*userInput))


# We use lambda here otherwise python will call the function before we want to
menuOptions = {
    1:
        lambda: handle(nameLookup, "What name do you want to look up?"),
    2:
        lambda: handle(numberLookup, "What number do you want to look up?"),
    3:
        lambda: handle(addEntry, "What is the name of the new user", "What is the number of the new user"),
    4:
        lambda: handle(removeEntry, "What is the name of the user you want to remove?"),
    5:
        lambda: handle(editName, "What is the current name you want to edit?", "What is the new name that should be set"
                      ),
    6:
        lambda: handle(editNumber, "What is the name of the user you want to edit",
                       "What is the new number for this user"),
    7:
        displayPhonebook,
    8:
        exit
}

askToShowMenu = False
while True:
    try:
        menu_choice = int(menu())
        menuOptions[menu_choice]()
        askToShowMenu = True
        # break
    except Exception as e:
        print(e)
        print("That is not a valid menu option")
