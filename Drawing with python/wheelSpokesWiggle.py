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

# settings to control how many spokes and 
# size of each spoke
lineSize = 10
lineWiggleDeg = 50
numWiggles = 5
numSpokes = 360


degBetween = 360 / numSpokes

speed (0)
# Loop for each spoke
for i in range(numSpokes):
    # Loop for each wiggle in each spoke
    for j in range(numWiggles):
        left(lineWiggleDeg)
        forward(lineSize)
        right(lineWiggleDeg)
        forward(lineSize)
    # reset position and prepare for next iteration
    penup()
    goto(0,0)
    left(degBetween)
    pendown()
    


done()