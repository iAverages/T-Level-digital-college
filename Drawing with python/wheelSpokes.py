# import turtle lib
# LOOP 12 times
#   go forward 50 pixels
#   go backward 50 pixels
#   rotate left 30 degs

from turtle import *

numSpokes = 360
degBetween = 360 / numSpokes

for i in range(numSpokes):
    penup()
    goto(0,0)
    left(degBetween)
    pendown()

done()