# Historical V@R

import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

assets = ['ABEV3.SA', 'CIEL3.SA', 'COGN3.SA', 'EGIE3.SA', 'KLBN11.SA', 
          'LWSA3.SA', 'MGLU3.SA', 'MRFG3.SA', 'MULT3.SA', 'PETZ3.SA']
weights = np.array([0.10, 0.10, 0.10, 0.10, 0.10,
                    0.10, 0.10, 0.10, 0.10, 0.10])

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

# V@R
var95 = np.nanpercentile(portfolioreturndf, 5)
var95*100