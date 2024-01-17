import requests
import json
from config import keys

API_KEY = '1611af7fc982708a6b04f79ee7350e76'
#http://api.exchangeratesapi.io/v1/convert?access_key=1611af7fc982708a6b04f79ee7350e76&from=EUR&to=USD&amount=3
# http://data.fixer.io/api/convert?access_key=eOtQGBUsMAkFH9MxuPn1syYQh9BBpKyo}&from=EUR&to=RUB&amount=25

class APIException(Exception):
	pass

class Convertor:
	@staticmethod
	def get_price(quote: str, base: str, amount: str):
		if quote == base:
			raise APIException(f"Невозможно перевести одинаковые валюты: {base}")

		try:
			quote_ticker = keys[quote]
		except KeyError:
			raise APIException(f'Неудалось обработать валюту {quote}')

		try:
			base_ticker = keys[base]
		except KeyError:
			raise APIException(f'Неудалось обработать валюту {base}')

		try:
			amount = float(amount)
		except ValueError:
			raise APIException(f'Неудалось обработать количество {amount}')

		r = requests.get(f'http://api.exchangeratesapi.io/v1/convert?access_key={API_KEY}&from=EUR \
		                &to={base_ticker}&amount=3')

		total_base = json.loads(r.content)[keys[base]]

		return total_base
