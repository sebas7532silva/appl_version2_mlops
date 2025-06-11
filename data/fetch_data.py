import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_data(ticker="AAPL", days=30):
    df = yf.download(ticker, period="30d", interval="1h", auto_adjust=False)
    df.dropna(inplace=True)
    df['Return'] = df['Close'].pct_change().fillna(0)
    return df
