import pandas as pd
from features.feature_engineering import prepare_features

def test_prepare_features():
    data = {
        "Close": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        "Volume": [1000, 1100, 1050, 1200, 1300, 1250, 1400, 1350, 1500, 1450, 1600]
    }
    df = pd.DataFrame(data)
    df_processed = prepare_features(df)
    # Checar que target existe y es binario
    assert "target" in df_processed.columns
    assert df_processed["target"].isin([0, 1]).all()
    # Checar que no hay NaNs
    assert not df_processed.isnull().values.any()
