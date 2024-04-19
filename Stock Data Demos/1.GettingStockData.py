import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

#the following data gets stock data from the last year until the latest possible
#then it shows it in a simple graph

today=date.today()
one_year_ago= today - timedelta(days=365)
print("the date is: ",today, one_year_ago)

# Get the data for the stock AAPL
apple_df= yf.download('AAPL',one_year_ago,today)

# Plot the closing price of the AAPL
#apple_df['Adj Close'].plot()

#I make a matplotlib object
one_stock_year, ax_one_year = plt.subplots()

#I add labels to show data about the plot
ax_one_year.plot(apple_df['Adj Close'],label="AAPL")
ax_one_year.set_xlabel("Time")
ax_one_year.set_ylabel("Price")
ax_one_year.set_axisbelow(True)
ax_one_year.yaxis.grid(color="gray",alpha=0.5)
ax_one_year.xaxis.grid(color="gray",alpha=0.5)

#shows and starts the plot
plt.legend()
plt.show()







one_year_ago= today - timedelta(days=440)

# Get the data for the stock AAPL
apple_df_rolled= yf.download('AAPL',one_year_ago,today)

apple_df_rolled.rolling(window=50)['Adj Close'].mean().plot()
#apple_df['Adj Close'].plot()


