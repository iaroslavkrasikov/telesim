import logging
import telebot

from . import env

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env.TOKEN)
# bot.remove_webhook()
# bot.set_webhook(f"{env.WEBHOOK_URL}/{env.TOKEN}")

def process_webhook(upd_json):
	update = telebot.types.Update.de_json(upd_json)
	bot.process_new_updates([update])

@bot.message_handler(commands=['start'])
def handle_start():
	pass

@bot.message_handler(func=lambda m: True)
def any_message_handler(message):
	bot.send_message(message.chat.id, "🤔")

