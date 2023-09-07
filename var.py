# Historical V@R

import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

assets = ['PETR4.SA', 'VALE3.SA', 'ABEV3.SA', 'BBAS3.SA']
weights = np.array([0.25, 0.25, 0.25, 0.25])

start = '2007-01-01'
end = '2023-09-06'

portfolio = yf.download(assets, start = start, end = end)['Adj Close']
portfolio.head()

returns = portfolio.pct_change()
returns.head()

portfolioreturn = (returns * weights).sum(axis=1)
portfolioreturn.head()

# dataframe
portfolioreturndf = pd.DataFrame()
portfolioreturndf["Returns"] = portfolioreturn
portfolioreturndf.head()

# histogram
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
portfolioreturndf['Returns'].plot.hist(bins = 80)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("Portfolio daily returns data")
ax1.text(-0.35,200,"Extreme Low\nreturns")
ax1.text(0.25,200,"Extreme High\nreturns")
plt.show()

