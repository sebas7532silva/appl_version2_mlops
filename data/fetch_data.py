import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_data(ticker="AAPL", days=30):
    end = datetime.today()
    start = end - timedelta(days=days)
    df = yf.download(ticker, start=start, end=end)
    df.dropna(inplace=True)
    df['Return'] = df['Close'].pct_change().fillna(0)
    return df
