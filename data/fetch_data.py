import requests

def get_crypto_price(coin_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    r = requests.get(url)
    data = r.json()
    price = data.get(coin_id, {}).get("usd", None)
    print(f"Precio de {coin_id}: ${price}")
    return price
