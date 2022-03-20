import tkinter as tk
from tkinter.ttk import *
import time
import math
# from item import Item
from button import Button

categories = {
    "drinks": {
        "color": [255, 255, 0],
        "items": [
            {
                "name": "Peppsi",
                "price": 100
            },
            {
                "name": "Fanta",
                "price": 100
            },
            {
                "name": "Tango",
                "price": 100
            },
            {
                "name": "Strawberry Shake",
                "price": 100
            },
            {
                "name": "Chocolate Shake",
                "price": 100
            },
            {
                "name": "Vanilla Shake",
                "price": 100
            },
        ]
    },
    "burgers": {
        "color": [0, 176, 240],
        "items": [{
            "name": "Classic Burger",
            "price": 100
        }, {
            "name": "Cheeseburger",
            "price": 100
        }, {
            "name": "Double Cheeseburger",
            "price": 100
        }, {
            "name": "Quarter Pounder",
            "price": 100
        }, {
            "name": "Quarter Pounder with Cheese",
            "price": 100
        }, {
            "name": "Q Pounder with Cheese & Bacon",
            "price": 100
        }]
    },
    "chicken": {
        "color": [255, 230, 153],
        "items": [
            {
                "name": "Chicken Burger",
                "price": 100
            },
            {
                "name": "Chicken Quarter Pounder",
                "price": 100
            },
            {
                "name": "3 Chicken Nuggets",
                "price": 100
            },
            {
                "name": "6 Chicken Nuggets",
                "price": 100
            },
            {
                "name": "20 Nugget Share Box",
                "price": 100
            },
            {
                "name": "4 Spicy Dip Strips",
                "price": 100
            },
        ]
    },
    "sides": {
        "color": [248, 203, 173],
        "items": [{
            "name": "Fries",
            "price": 100
        }, {
            "name": "Fruit bag",
            "price": 100
        }, {
            "name": "Carrot sticks",
            "price": 100
        }, {
            "name": "Mozzarella Sticks",
            "price": 100
        }, {
            "name": "Jalapeno Bites",
            "price": 100
        }]
    },
    "desserts": {
        "color": [180, 199, 231],
        "items": [{
            "name": "Chocolate Muffin",
            "price": 100
        }, {
            "name": "Blueberry Muffin",
            "price": 100
        }, {
            "name": "Brownie",
            "price": 100
        }, {
            "name": "Apple Pie",
            "price": 100
        }, {
            "name": "Vanilla Ice Cream",
            "price": 100
        }, {
            "name": "Strawberry Ice Cream",
            "price": 100
        }, {
            "name": "Chocolate Ice Cream",
            "price": 100
        }]
    },
}

root = tk.Tk()
root.title("Order screen")
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
# a = Button(root, text="Hello1", color=[255, 255, 230])
# b = Button(root, text="Hello2", color=[255, 255, 230])
# c = Button(root, text="Hello3", color=[255, 255, 230])

menuItems = []
column = 0
frame = Frame(root)
frame.grid(row=0, column=0, sticky=tk.NSEW)

for category in categories:
    meta = categories[category]
    column += 1
    row = 0
    tk.Grid.columnconfigure(frame, column, weight=1)

    label = Label(
        frame,
        text=category.upper(),
    )
    label.grid(column=column, row=row)
    for item in meta["items"]:
        tk.Grid.rowconfigure(frame, row, weight=1)
        row += 1
        btn = Button(frame, column=column, row=row, text=item["name"], color=meta["color"])
        menuItems.append(btn)

    # frame.grid(column=column, sticky="nwse", row=0, padx=5, rowspan=10)

amountFrame = Frame(root)
amountColumn = 0
# Create 6 sales buttons
# 2 columns of 3 buttons
for i in range(2):
    amountColumn += 1
    row = 0
    tk.Grid.columnconfigure(amountFrame, amountColumn, weight=1)
    for x in range(3):
        row += 1
        tk.Grid.rowconfigure(amountFrame, row + 1, weight=1)
        btn = Button(amountFrame, text=i + x + 1, column=amountColumn, row=row)

label = Label(
    frame,
    text="SALES",
)

label.grid(column=column + 1, row=1)
amountFrame.grid(row=0, column=column, sticky=tk.NSEW)

# newOrder = Button(frame, row=row + 1, column=column + 1, text="New Order")
# finishOrder = Button(frame, row=row + 1, column=column, text="Complete The Sale")

# actionFrame.grid(
#     column=column + 1,
#     sticky="n",
#     row=1,
#     padx=5,
# )

# def aClick(self):
#     self.setText("I have been clicked")
#     self.setTextDelay(2000, "I am back to normal now!")

# def bClick(self):
#     self.setText("guesswhat")
#     self.setTextDelay(2000, "you smell")

# def cClick(self):
#     self.setText("i heard your a gamer")
#     self.setTextDelay(2000, "too bad im more gamer")

# a.onClick(aClick)
# b.onClick(bClick)
# c.onClick(cClick)

# root.grid()
root.mainloop()