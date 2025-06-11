# tests/test_fetch_data.py
from unittest.mock import patch
import pandas as pd
from data.fetch_data import get_stock_data

@patch('data.fetch_data.yf.download')
def test_fetch_data(mock_download):
    mock_df = pd.DataFrame({
        'Close': [150, 152, 153],
        'Open': [148, 151, 152],
        'High': [151, 153, 154],
        'Low': [147, 150, 151],
        'Adj Close': [150, 152, 153],
        'Volume': [1000000, 1100000, 1200000]
    })
    mock_download.return_value = mock_df

    df = get_stock_data()
    assert not df.empty
    assert 'Return' in df.columns

