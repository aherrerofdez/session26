from matplotlib import pylab as plt
import pandas
import datetime

df1 = pandas.read_csv("AAPL.csv")
print(df1.head())
df1['Date'] = pandas.to_datetime(df1.Date)
print(df1.head())

df2 = pandas.read_excel("iphone-dates.xlsx")
print(df2)
df2['Date'] = pandas.to_datetime(df2.Date)
indexes = []
values = []
dates = []
for date2 in df2.Date:
    print(df1.index[df1.Date == date2], df1.index[df1.Date == date2][0])
    indexes.append(df1.index[df1.Date == date2][0])
    values.append(df1["Close"][df1.index[df1.Date == date2][0]])
    dates.append(df1["Date"][df1.index[df1.Date == date2][0]])
print(indexes, values)

mean = df1["Close"].mean()

plt.figure("Apple Stock and Iphone Launch")
plt.xlabel("Dates")

datenow = datetime.datetime.now()
datestart = datetime.datetime(2005, 4, 20)

for i in range(0, len(df1["Date"]), 10):
    plt.clf()
    plt.ylim(0, 330)
    plt.xlim(datestart, datenow)
    plt.plot(df1["Date"][0:i], df1["Close"][0:i], 'r-', linewidth=0.6, label="Stock price, mean="+str(mean), )
    # plt.plot(df1["Date"][0:i], df1["Close"][0:i], '-o', ms=7, markevery=indexes, linewidth=0, label="Iphone launch date")

    # put the values
    for j in range(len(dates)):
        if (dates[j] > df1["Date"][i]):
            break
        plt.text(dates[j], values[j], str(int(values[j])))
    plt.plot(dates[0:j], values[0:j], '-o', ms=7, linewidth=0, label="Iphone launch date")
    plt.legend(loc="upper left")
    plt.draw()
    plt.pause(0.001)

plt.show()
