import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt 
from scipy.stats import norm

years = 15

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365*years)

tickers = ['ADVANIHOTR.NS', 'APTECHT.NS', 'BLUEDART.NS', 'UBL.NS', 'BFUTILITIE.NS']

adj_close_df = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=startDate, end=endDate)
    adj_close_df[ticker] = data['Close']

log_returns = np.log(adj_close_df / adj_close_df.shift(1))
log_returns = log_returns.dropna()

def expected_return(weights, log_returns):
    return np.sum(weights * log_returns.mean())

def standard_deviation(weights, cov_matrix):
    variance = weights.T @ cov_matrix @ weights
    return np.sqrt(variance)

cov_matrix = log_returns.cov() 

portfolio_value = 1000000
weights = np.array([1/len(tickers)] * len(tickers))

portfolio_expected_return = expected_return(weights, log_returns)
portfolio_std_dev = standard_deviation(weights, cov_matrix) 

def random_z_score():
    return np.random.normal(0, 1)

days = 5

def scenario_gain_loss(portfolio_value, portfolio_std_dev, z_score, days):
    return portfolio_value * (portfolio_expected_return * days + portfolio_std_dev * z_score * np.sqrt(days))

simulations = 10000
scenarioReturn = []

for i in range(simulations):
    z_score = random_z_score()
    scenarioReturn.append(scenario_gain_loss(portfolio_value, portfolio_std_dev, z_score, days))

confidence_interval = 0.99
VaR = -np.percentile(scenarioReturn, (1 - confidence_interval) * 100)
print(f'Value at Risk (VaR) at {confidence_interval * 100:.0f}% confidence level: ${VaR:,.2f}')

plt.hist(scenarioReturn, bins=50, density=True)
plt.xlabel('Scenario Gain/Loss ($)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Scenario Gain/Loss for {days}-Day Portfolio Returns')
plt.axvline(-VaR, color='r', linestyle='dashed', linewidth=2, label=f'VaR at {confidence_interval:.0%} confidence level')  
plt.legend()
plt.show()