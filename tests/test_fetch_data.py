from data.fetch_data import get_stock_data

def test_fetch_data():
    df = get_stock_data()
    assert not df.empty
    assert "Close" in df.columns
    assert "Volume" in df.columns
