from turtle import * 
from random import randrange 
# function to get a number from users input
# will keep asking for number input if invalid input 
# is used
def getIntInput(message):
    while True:
        try:
            return int(input(message))
        except:
            print("That is not a number.")

# Get users input
sides = getIntInput("how many sides: ")
times = min(getIntInput("how many times should be draw the shape: "), 360)

# caluclate values and set speed
shapeAngle = 360 / sides
size = 50
degBetween = 360 / times
speed(0)
# changes how python interpates the numbers passed into 
# the color function
colormode(255)

# function that actually draws the shape
def drawShape():
    for i in range(sides):
        forward(size)
        # change color to random color
        # color(randrange(1,255), randrange(1,255), randrange(1,255))
        left(shapeAngle)

# draw shape number of times
for i in range(times):
    drawShape()
    left(degBetween)

# stop the turtle from closing right away
# so i can take screenshot
done()

