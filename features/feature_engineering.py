import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega variables basadas en medias móviles y diferenciales para crypto.
    """
    df['return'] = df['Close'].pct_change()
    df['ma_5'] = df['Close'].rolling(window=5).mean()
    df['ma_10'] = df['Close'].rolling(window=10).mean()
    df['volatility'] = df['Close'].rolling(window=5).std()

    df['ma_diff'] = df['ma_5'] - df['ma_10']
    df['volume_change'] = df['Volume'].pct_change()
    
    df.dropna(inplace=True)
    return df

def create_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la columna binaria 'target': 1 si sube el siguiente día, 0 si baja.
    """
    df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)
    return df

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesamiento completo para crypto.
    """
    df = add_features(df)
    df = create_target(df)
    return df

