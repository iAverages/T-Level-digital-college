import matplotlib.pyplot as pl
import pandas as pd

data = pd.read_csv("./data.csv")

data.plot(x="Duration", y="Pulse")

pl.show()
