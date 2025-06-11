from data.fetch_data import fetch_data

def test_fetch_data():
    df = fetch_data()
    assert not df.empty
    assert "Close" in df.columns
    assert "Volume" in df.columns
