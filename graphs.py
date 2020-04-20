from matplotlib import pylab as plt
import pandas

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

plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="Stock price, mean="+str(mean))
# plt.plot(df1["Date"], df1["Close"], '-o', ms=7, markevery=indexes, linewidth=0, label="Iphone launch date")
plt.plot(dates, values, 'o', label="Iphone launch date")
# put the values
for i in range(len(dates)):
    plt.text(dates[i], values[i], str(int(values[i])))
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
