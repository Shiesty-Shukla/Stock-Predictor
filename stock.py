import pandas as pd
from sklearn.linear_model import LinearRegression
from yahoofinancials import YahooFinancials
stock = input("What stock: ")

highs = []
lows = []
opens = []
closes = []

yahoo_financials = YahooFinancials(str(stock))
stats=(yahoo_financials.get_historical_price_data("2010-01-01", "2021-06-29", "daily"))

i = 0
for date in stats[str(stock)]["prices"]:
    if i == 0:
        i += 1
        continue
    highs.append(date["high"])
    lows.append(date["low"])
    opens.append(date["open"])
    closes.append(date["close"])
    i += 1
print("No, of data pts", i)

total = []
totalopens = []
for j in range(4):
    opens.append(0)

for i in range(i-1):
    total.append([opens[i], lows[i], highs[i], closes[i]])


def Predictor(lst, months):
    total_training = lst[0:i-months]
    total_validations = lst[i-months:]

    df = pd.DataFrame(total_training, dtype=float)
    XTrain = df.iloc[:, :-1]
    yTrain = df.iloc[:, [-1]]

    clf = LinearRegression()
    clf.fit(XTrain, yTrain)

    print("\n\n")

    dfP = pd.DataFrame(total_validations, dtype=float)
    XValidations = dfP.iloc[:, :-1]
    YValidations = dfP.iloc[:, [-1]]

    print("\n\nPrediction")
    YPrediction = clf.predict(XValidations)

    print("\nOriginal")
    print(YValidations)

    print("\nPredicted")
    print(YPrediction)

Predictor(total,1)




