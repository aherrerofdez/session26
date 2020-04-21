from matplotlib import pylab as plt
import pandas as pd
import datetime

# Read csv stock data from American Airlines (AA) and Delta Airlines (DA)
df_AA = pd.read_csv("AAL.csv")
df_DA = pd.read_csv("DAL.csv")

print("AMERICAN AIRLINES STOCK SUMMARY")
print(df_AA.head(3))
print(df_AA.tail(3))
print("\n")
print("DELTA AIRLINES STOCK SUMMARY")
print(df_DA.head(3))
print(df_DA.tail(3))

# Converting Date to datetime
df_AA.Date = pd.to_datetime(df_AA.Date)
df_DA.Date = pd.to_datetime(df_DA.Date)

plt.rcParams["figure.figsize"] = [10, 5]
plt.figure("American Airlines Stock vs Delta Airlines Stock")
plt.xlabel("Date")
plt.ylabel("Stock Price")

# Animated Drawing
for i in range(0, len(df_AA.Date), 10):
    plt.clf()
    plt.xlim(datetime.datetime(2007, 7, 2), datetime.datetime(2020, 3, 31))
    plt.ylim(0, 65)
    plt.plot(df_AA.Date[0:i], df_AA.Close[0:i], 'b', label="American Airlines")
    plt.plot(df_DA.Date[0:i], df_DA.Close[0:i], 'r', label="Delta Airlines")
    plt.legend(loc="upper left")
    plt.draw()
    plt.pause(0.00001)

plt.show()