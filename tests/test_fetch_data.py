# tests/test_fetch_data.py
from unittest.mock import patch
import pandas as pd
from data.fetch_data import get_crypto_price

@patch('data.fetch_data.requests.get')
def test_fetch_data(mock_get):
    mock_response = {
        "prices": [
            [1617753600000, 58000],
            [1617840000000, 59000],
            [1617926400000, 60000]
        ],
        "total_volumes": [
            [1617753600000, 1000],
            [1617840000000, 1100],
            [1617926400000, 1200]
        ]
    }
    mock_get.return_value.json.return_value = mock_response

    df = get_crypto_price(coin_id="bitcoin", days=3)
    
    assert not df.empty
    assert set(['Open', 'High', 'Low', 'Close', 'Volume', 'date']).issubset(df.columns)
    assert len(df) == 3

