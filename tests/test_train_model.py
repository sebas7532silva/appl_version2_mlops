import pandas as pd
from models.train_model import train_model

def test_train_model():
    data = {
        "return": [0.01, 0.02, -0.01, 0.03, 0.01, -0.02, 0.00, 0.01, -0.01, 0.02],
        "ma_5": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        "ma_10": [99, 100, 101, 102, 103, 104, 105, 106, 107, 108],
        "volatility": [1, 1.1, 0.9, 1.2, 1, 0.8, 1, 1.1, 0.9, 1],
        "ma_diff": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "volume_change": [0.05, -0.02, 0.03, 0.01, -0.01, 0, 0.02, -0.03, 0.04, 0.01],
        "target": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    clf, acc, f1 = train_model(df)
    assert acc >= 0 and acc <= 1
    assert f1 >= 0 and f1 <= 1
    assert hasattr(clf, "predict")
