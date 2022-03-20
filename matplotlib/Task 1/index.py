import matplotlib.pyplot as pl
import numpy

c = lambda *x: numpy.array(x)

pl.plot(c(1, 8), c(3, 10))

pl.show()
