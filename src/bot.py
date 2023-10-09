import logging
import telebot

from . import env

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env.TOKEN)

webhook_info = bot.get_webhook_info()
if webhook_info.url != env.WEBHOOK_URL:
	bot.set_webhook(env.WEBHOOK_URL, secret_token=env.TOKEN_MD5)

def process_update(upd_json):
	update = telebot.types.Update.de_json(upd_json)
	bot.process_new_updates([update])

@bot.message_handler(commands=['start'])
def start_handler(message):
	pass

@bot.message_handler(func=lambda m: True)
def any_message_handler(message):
	bot.send_message(message.chat.id, "🤔")