import logging
import telebot

from . import env

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env.TOKEN)

webhook_info = bot.get_webhook_info()
if webhook_info.url != env.WEBHOOK_URL:
	bot.set_webhook(env.WEBHOOK_URL, secret_token=env.TOKEN_MD5)

def web_app_inline_keyboard():
   keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
   # Remove "api/bot" from url
   web_app = telebot.types.WebAppInfo(env.WEBHOOK_URL[:-7])
   keyboard.add(telebot.types.InlineKeyboardButton(text="Get started", web_app=web_app))

   return keyboard

def process_update(upd_json):
	update = telebot.types.Update.de_json(upd_json)
	bot.process_new_updates([update])

@bot.message_handler(commands=["start"])
def start_handler(message):
	welcome_text = (
		"Welcome to [@telesimbot](tg://user?id=123456789)! " 
		"Here you can Buy our eSIM instantly with TON or any credit card, "
		"load it into your phone and start using the Internet "
		"over more than 70 countries around the world. \n\n"
		"Push _Open Telesim_ or button below to begin." 
	)
	bot.send_message(message.chat.id, text=welcome_text, parse_mode="Markdown", reply_markup=web_app_inline_keyboard())

@bot.message_handler(func=lambda m: True)
def any_message_handler(message):
	bot.send_message(message.chat.id, "🤔")