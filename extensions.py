import requests
import json
from config import keys

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        # Используем CryptoCompare API (бесплатное и не требует сложной регистрации)
        r = requests.get(f'https://min-api.cryptocompare.com{base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[quote_ticker]
        
        return total_base * amount
