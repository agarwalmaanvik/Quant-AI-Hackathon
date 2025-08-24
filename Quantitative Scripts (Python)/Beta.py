import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings

#warnings.simplefilter(action="ignore", category=FutureWarning)
# Set parameters
index = "^NSEI"
stock = "ITCHOTELS.NS"
period = "3y"
interval = "1wk"


def get_price_data(ticker, period, interval):
    """Fetch historical price data using yfinance."""
    data = yf.download(ticker, period=period, interval=interval)
    return data[["Close"]].dropna()  # Ensure we maintain the index

def calculate_beta(index, stock, period, interval, just_beta=False):
    index_data = get_price_data(index, period=period, interval=interval)
    stock_data = get_price_data(stock, period=period, interval=interval)

    # Rename columns for clarity
    index_data.rename(columns={"Close": "Index_Close"}, inplace=True)
    stock_data.rename(columns={"Close": "Stock_Close"}, inplace=True)

    # Merge data correctly using pd.concat()
    data = pd.concat([index_data, stock_data], axis=1).dropna()

    # Compute percentage returns
    data["Index_Return"] = data["Index_Close"].pct_change()
    data["Stock_Return"] = data["Stock_Close"].pct_change()
    
    data.dropna(inplace=True)

    # Linear Regression Model
    X = data["Index_Return"].values.reshape(-1, 1)
    y = data["Stock_Return"].values

    model = LinearRegression().fit(X, y)
    beta = model.coef_[0]

    return beta if just_beta else (beta, model, data)


# Calculate beta
beta, model, data = calculate_beta(index, stock, period, interval)
print(f"{stock} beta compared to {index} is: {beta.round(4)}")

# Prepare data for plotting (Reuse already fetched data)
X = data["Index_Return"].values.reshape(-1, 1)
y = data["Stock_Return"].values

X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
Y_line = model.predict(X_line)

# Plot results
plt.figure(figsize=(10, 7))
plt.scatter(X, y, alpha=0.3, label="Actual Returns")
plt.plot(X_line, Y_line, "r", alpha=0.9, label="Regression Line")
plt.xlabel(f"{index} {interval} Return")
plt.ylabel(f"{stock} {interval} Return")
plt.title(f"Linear Regression over {period} of {stock} {interval} Return on {index} {interval} Return")

plt.annotate(f"Beta: {beta:.4f}", xy=(0.05, 0.95), xycoords="axes fraction",
             fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

plt.legend()
plt.show()