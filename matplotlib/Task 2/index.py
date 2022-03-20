import matplotlib.pyplot as pl
import numpy

c = lambda *x: numpy.array(x)


def build(*points):
    xPoints = []
    yPoints = []
    for x, y in points:
        xPoints.append(x)
        yPoints.append(y)
    return [c(*xPoints), c(*yPoints)]


points = [[1, 3], [2, 8], [6, 1], [8, 10]]

pl.plot(*build(*points))

pl.show()
