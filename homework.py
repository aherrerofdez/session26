from matplotlib import pylab as plt
import pandas as pd

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

# Plotting
plt.figure("American Airlines Stock vs Delta Airlines Stock")
plt.plot(df_AA.Date, df_AA.Close, "b", label="American Airlines")
plt.plot(df_DA.Date, df_DA.Close, "r", label="Delta Airlines")
plt.legend(loc="upper left")

plt.show()
