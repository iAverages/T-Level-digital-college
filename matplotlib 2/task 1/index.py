import matplotlib.pyplot as pl

labels = [
    "Maths",
    "English",
    "Science",
    "French",
    "History",
]

sizes = [
    27,
    13,
    43,
    7,
    10,
]

pl.pie(sizes, labels=labels, autopct='%1.1f%%')
pl.title("School students favorate subjects")
pl.show()
