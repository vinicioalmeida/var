# Parametric VaR

import numpy as np
from scipy.stats import norm

# Define portfolio properties
portfolio_values = [1000000, 2000000, 3000000]  # Replace with your portfolio values
portfolio_weights = [0.4, 0.3, 0.3]  # Replace with your portfolio weights

# Calculate portfolio mean and standard deviation
portfolio_mean_return = 0.08  # Replace with your portfolio's expected return
portfolio_std_dev = 0.2  # Replace with your portfolio's standard deviation

# Confidence level and time horizon
confidence_level = 0.95  # 95% confidence level
time_horizon = 1  # 1 day

# Calculate the z-score for the given confidence level
z_score = norm.ppf(confidence_level)

# Calculate the portfolio's expected return and standard deviation over the time horizon
expected_return = portfolio_mean_return * time_horizon
expected_std_dev = portfolio_std_dev * np.sqrt(time_horizon)

# Calculate the portfolio value at risk (VaR)
portfolio_var = portfolio_values[0] * (1 - z_score * expected_std_dev / portfolio_values[0])

print(f"Parametric VaR at {confidence_level*100}% confidence level for the portfolio is: ${portfolio_var:.2f}")