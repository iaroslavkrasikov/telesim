from urllib.parse import urlunparse
import logging
import telebot

bot = None

def init(WEBHOOK_URL, TOKEN):
	bot = telebot.TeleBot(TOKEN)
	bot.remove_webhook()
	bot.set_webhook(urlunparse("https", WEBHOOK_URL, f"api/bot/{TOKEN}"))

def process_webhook(upd_json):
	update = bot.types.Update.de_json(upd_json)
	bot.process_new_updates([update])

@bot.message_handler(func=lambda m: True)
def any_message_handler(message):
	bot.send_message(message.chat.id, "🤔")

