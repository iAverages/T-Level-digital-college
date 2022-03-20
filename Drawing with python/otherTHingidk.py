# import turtle lib
# LOOP 12 times
#   LOOP 5 times
#       left 50
#       forward 10
#       right 50
#       forward 10
#   pen up
#   go to 0,0
#   left 30
#   pen down

from turtle import *
from math import cos, sin, pi

# settings to control how many spokes and 
# size of each spoke
lineSize = 50
lineWiggleDeg = 50
numWiggles = 5
numSpokes = 13


degBetween = 360 / numSpokes

speed (0)
# Loop for each spoke
for i in range(numSpokes):
    forward(lineSize)
    # reset position and prepare for next iteration
    penup()
    goto(0,0)
    left(degBetween)
    pendown()

def getSpokeEnd(spokeNum):
    angle = degBetween * spokeNum
    x = lineSize * cos(angle * (pi / 180))
    y = lineSize * sin(angle * (pi / 180))
    return [x,y]


forward(lineSize)
for i in range(numSpokes + 1):
    left(degBetween)
    x,y = getSpokeEnd(i)
    goto(x,y)

done()