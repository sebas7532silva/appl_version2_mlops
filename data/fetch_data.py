import requests
import pandas as pd

def get_crypto_price(coin_id="bitcoin", days=30):
    """
    Obtiene datos históricos diarios de precios y volúmenes para una criptomoneda.
    coin_id: id de la moneda (ej. 'bitcoin')
    days: cantidad de días hacia atrás (ej. 30)
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    r = requests.get(url, params=params)
    data = r.json()
    
    # Precios: lista de [timestamp, price]
    prices = data.get("prices", [])
    volumes = data.get("total_volumes", [])
    
    # Convertimos a DataFrame
    df_prices = pd.DataFrame(prices, columns=["timestamp", "price"])
    df_volumes = pd.DataFrame(volumes, columns=["timestamp", "volume"])
    
    # Convertimos timestamp a datetime
    df_prices["date"] = pd.to_datetime(df_prices["timestamp"], unit="ms")
    df_volumes["date"] = pd.to_datetime(df_volumes["timestamp"], unit="ms")
    
    # Unimos precios y volúmenes por fecha
    df = pd.merge(df_prices[["date", "price"]], df_volumes[["date", "volume"]], on="date")
    
    # Aquí solo tenemos precio (close), vamos a simular Open, High, Low para el ejemplo
    # En datos reales esto debería venir del API o de otra fuente
    df["Open"] = df["price"] * 0.98
    df["High"] = df["price"] * 1.02
    df["Low"] = df["price"] * 0.97
    df["Close"] = df["price"]
    
    # Ordenamos columnas al estilo OHLCV
    df = df[["date", "Open", "High", "Low", "Close", "volume"]]
    df.rename(columns={"volume": "Volume"}, inplace=True)
    
    return df

