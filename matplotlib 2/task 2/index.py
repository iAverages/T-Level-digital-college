import matplotlib.pyplot as pl

data = [
    9,
    11,
    15,
    19,
    22,
    27,
    31,
    32,
    25,
    18,
    13,
    9,
]

labels = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

pl.bar(x=labels, height=data)
pl.ylabel("Temperature")
pl.xlabel("Month")
pl.xticks(rotation=45)
pl.title("Average temperatures in Madrid")

# Make sure all content is visible
pl.tight_layout()
pl.show()
