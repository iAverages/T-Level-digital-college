from statistics import mean
import matplotlib.pyplot as pl
import pandas as pd


class TextDisplay:

    text = []
    minLength = 0

    def __init__(self) -> None:
        # Python shares arrays accross all instances of a class
        self.text = []

    def add(self, msg, *numbers):
        self.text.append([msg, *numbers])
        msgLength = len(msg)
        if (msgLength > self.minLength):
            self.minLength = msgLength

    def print(self):
        for group in self.text:
            t = group[0]
            extra = " " * (self.minLength + 1 - len(t))
            print(f"    {t}{extra}", round(*group[1:], 2))


data = None


def getData():
    """Function to get data from Task4a_data.csv file"""
    global data
    if (type(data) != pd.core.frame.DataFrame):
        try:
            data = pd.read_csv("Task4a_data.csv")
        except FileNotFoundError:
            print("Unable to find data file (Task4a_data.csv) exiting..")
            exit(1)
    return data


#The menu() function generates the UI the accepts and validates user choice
def menu():
    while True:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("")
        print("######################################################")

        menu_choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 6:
                print("Sorry, you did not neter a valid choice")
            else:
                return menu_choice


#Gets the short version of the conversion information based on user menu choice
def get_currency():
    currencies = {
        "1": "GBP - EUR",
        "2": "EUR - GBP",
        "3": "GBP - AUD",
        "4": "AUD - GBP",
        "5": "GPB - JPY",
        "6": "JPY - GPB"
    }
    currency = currencies.get(menu_choice)
    return currency


menu_choice = menu()
currency = get_currency()


# The get_conversion_rate function uses pandas to get the latest conversion rate
# Imports a csv file in to a data frame
# Uses "iloc" to get the last/most recent value in the selected column
def get_conversion_rate(curr):
    df = getData()
    conversion_rate = round(df[curr].iloc[-1], 2)
    return conversion_rate


conversion_rate = get_conversion_rate(currency)

# Accepts and validates user input for teh amount they want to convert
print("You are converting: ", currency)

while True:
    conversion_amount = input("please enter the ammount you wish to convert")
    try:
        float(conversion_amount)
    except:
        print("Sorry, you must enter a numerical value")
    else:
        conversion_amount = float(conversion_amount)
        break

# conversion_amount = float(get_amount_to_convert())

# Performs the converison and outputs the final values
amount_recieved = round(conversion_amount * conversion_rate, 2)

print("##################################")
print(f"You are converting {conversion_amount} in {currency[0:3]}")
print(f"You will recieve {amount_recieved} in {currency[6:9]}")

yesAccept = ["yes", "y", "1"]


def askYesNo(msg):
    while True:
        intp = input(f"{msg} (yes/y/no/n)")
        if (intp == ""):
            print("Please enter your option")
        elif (intp.lower() in yesAccept):
            return True
        else:
            return False


def trends(curr):
    text = TextDisplay()
    print(f"\nTrends for {curr}")

    # Average
    data = getData()[[curr, "Date"]]
    df = data[curr]
    avg = df.mean()
    text.add("The average convertion rate is", avg)

    # Oldest and newest date
    oldest = df.iloc[0]
    newest = get_conversion_rate(curr)
    text.add("The oldest convertion rate data is:", oldest)
    text.add("The newest convertion rate data is:", newest)

    # Highest and lowest values
    lowest = df.min()
    highest = df.max()
    text.add("The lowest convertion rate is:", lowest)
    text.add("The highest convertion rate is:", highest)
    text.print()

    avgMonths = {}
    # Sort each month into groups to average later
    for _, row in data.iterrows():
        splitDate = row["Date"].split("/")
        month = splitDate[1]
        year = splitDate[2]
        key = f"{month}-{year}"
        try:
            avgMonths[key]
        except KeyError:
            avgMonths[key] = []
        avgMonths[key].append(row[curr])

    xPoints = []
    yPoints = []
    # Convert data points from each month to
    # get average conversion rate
    for k, v in avgMonths.items():
        xPoints.append(k)
        yPoints.append(mean(v))

    # Build graph
    pl.title(f"Average conversion rates for {curr} each month")
    pl.xlabel("Date")
    pl.ylabel("Convertion")
    pl.grid()
    pl.plot(xPoints, yPoints)
    pl.show()


if (askYesNo("Do you want to view the GBP-USD and USD-GBP Trends?")):
    trends("GBP - USD")
    trends("USD - GBP")
