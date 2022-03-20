import random

num = random.randrange(1, 10)
found = False
guesses = 0

while guesses < 3:
    try:
        guess = int(input("Try and guess the number: "))
    except:
        print("Please enter a number!")
        continue
    guesses += 1
    if guess == num:
        print("Well done you guessed the word correctly")
        found = True
        break
    elif guess > num:
        print("Your guess is bigger than the number!")
    else:
        print("Your guess is smaller than the number!")

if found == False:
    print(f"You did not guess the number, the number was {num}")

print("Thanks for playing")