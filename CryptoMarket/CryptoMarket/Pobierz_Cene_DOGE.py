# your_existing_module.py
import requests
from .binance_keys import API_KEY


def pobierz_dane_doge_binance():
    base_url = "https://api.binance.com/api/v3/ticker/price"
    symbol = "DOGEUSDT"

    params = {"symbol": symbol}

    try:
        response = requests.get(base_url, params=params, headers={"X-MBX-APIKEY": API_KEY})
        response.raise_for_status()
        dane = response.json()
        cena_dogecoin = float(dane["price"])
        return cena_dogecoin
    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania danych: {e}')
        return None
