# Historical V@R

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

assets = ['ABEV3.SA', 'CIEL3.SA', 'COGN3.SA', 'EGIE3.SA', 'KLBN11.SA', 
          'LWSA3.SA', 'MGLU3.SA', 'MRFG3.SA', 'MULT3.SA', 'PETZ3.SA']
weights = np.array([0.10, 0.10, 0.10, 0.10, 0.10,
                    0.10, 0.10, 0.10, 0.10, 0.10])

start = '2022-01-01'
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

# V@R
confidence_level = 0.95
historical_var = np.nanpercentile(portfolioreturndf, (1-confidence_level)*100)
print(f"Historical VaR at {confidence_level*100}% confidence level: {historical_var:.4f}")

#Plot
plt.hist(portfolioreturndf, bins=10, density=True, alpha=0.6, color='g', label='Returns')
# Add a vertical line to mark the VaR
plt.axvline(x=historical_var, color='r', linestyle='--', label=f'{confidence_level*100}% VaR')
# Add labels and legend
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.legend()
# Show the plot
plt.title('Historical Value at Risk (VaR) Calculation')
plt.show()