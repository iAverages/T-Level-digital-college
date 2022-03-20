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
lineSize = 100
numSpokes = 36
flagSize = 30

degBetween = 360 / numSpokes

# Loop for each spoke
for i in range(numSpokes):
    forward(lineSize)
    # Loop for each wiggle in each spoke
    for j in range(3):
        left(90)
        forward(flagSize)
    # Fix rotation after drawing square/flag
    left(90)

    # reset position and prepare for next iteration
    penup()
    goto(0,0)
    right(degBetween)
    pendown()
    

done()