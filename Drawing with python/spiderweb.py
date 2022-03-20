from turtle import * 
from math import cos, sin, pi, atan2, degrees, acos, sqrt
from random import randrange 

# function to get a number from users input
# will keep asking for number input if invalid input 
# is used
def getIntInput(message):
    while True:
        try:
            return int(input(message))
        except NumberFormatExecption:
            print("That is not a number.")

def setRandomColor():
    color(randrange(1,255),randrange(1,255),randrange(1,255))

def getSpokeEnd(diamter, spokeNum):
    angle = degBetween * spokeNum
    x = diamter * cos(angle * (pi / 180))
    y = diamter * sin(angle * (pi / 180))
    return [x,y]

speed(0)
# changes how python interpates the numbers passed into 
# the color function
colormode(255)

# size of each spoke
lineSize = 150
numSpokes = getIntInput("how many spokes should the web have: ")
numberOfRings = getIntInput("how many rings should the web have: ")
degBetween = 360 / numSpokes

# Draw spokes
for i in range(numSpokes):
    forward(lineSize)
    penup()
    goto(0,0)
    # setRandomColor()
    right(degBetween)
    pendown()

# gap between rings
gap = lineSize / numberOfRings - 4 # - 4 to leave a gap on the edge of the web
radius = gap

for a in range(numberOfRings):
    goto(0,0)
    setheading(degBetween * a)
    forward(radius)
    right(45)
    for i in range(numSpokes):
        x1,y1 = getSpokeEnd(radius, i)
        x2,y2 = getSpokeEnd(radius, i + 1)
        b = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
        circle(b, -60)
        left(90)
    radius += gap
    # setRandomColor()

penup()
goto(0,0)
setheading(0)

# stop the turtle from closing right away
# so i can take screenshot
done()

