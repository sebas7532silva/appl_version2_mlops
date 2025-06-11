from data.fetch_data import fetch_stock_data

def test_fetch_stock_data():
    df = fetch_stock_data()
    assert not df.empty
    assert "Close" in df.columns
    assert "Volume" in df.columns
