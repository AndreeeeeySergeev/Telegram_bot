import telebot
from config import TOKEN
from extensions import *



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
	text = "Для того, чтобы начать работу, введите команду боту в слудующем формате: \n евро \
	\n <в какую валюту перевести> \n <количество переводимой валюты>\
	\n 'Например: евро рубль 1' \
	\n Увидеть список всех доступных валют по команде: /values"
	bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
	text = 'Доступные варианты'
	for key in keys.keys():
		text = '\n'.join((text, key,))
	bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
	try:
		values = message.text.split(' ')
		if len(values) != 3:
			raise APIException("Слишком много параметров")

		quote, base, amount = values
		total_base = Convertor.get_price(quote, base, amount)
	except APIException as e:
		bot.reply_to(message, f"Ошибка пользователя. \n{e}")
	except Exception as e:
		bot.reply_to(message, f"Не удалось обработать команду. \n{e}")
	else:
		text = f'Цена {amount} {quote} в {base} - {total_base}'
		bot.send_message(message.chat.id, text)


bot.polling()
