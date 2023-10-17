import telebot
import logging

from .env import env
from . import db

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env['TOKEN'])

webhook_info = bot.get_webhook_info()
if webhook_info.url != env['WEBHOOK_URL']:
	bot.set_webhook(env['WEBHOOK_URL'], secret_token=env['TOKEN_MD5'])

def is_user_active(user_id):
	user = db.get("user", {"telegram_id": user_id})

	if not user is None:
		if user["is_active"] == True:
			return True
	return False

def add_new_user(user_id):
	db.create("user", {"telegram_id": user_id})

def web_app_inline_keyboard():
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
	# Remove "api/bot" from url
	web_app = telebot.types.WebAppInfo(env['WEBHOOK_URL'][:-len("api/bot")])
	keyboard.add(
	    telebot.types.InlineKeyboardButton(text="Get started",
	                                       web_app=web_app))

	return keyboard

def process_update(upd_json):
	update = telebot.types.Update.de_json(upd_json)
	bot.process_new_updates([update])

@bot.message_handler(content_types=["web_app_data"])
def web_app_data_handler(message):
	# TODO: Check if we can webapp.sendData
	bot.send_message(message.chat.id, message.web_app_data.data)

@bot.message_handler(commands=["start"])
def start_handler(message):
	welcome_text = (
	    f"Welcome to [@telesimbot](tg://user?id={env['TOKEN'].split(':')[0]})! "
	    "Here you can Buy our eSIM instantly with TON or any credit card, "
	    "load it into your phone and start using the Internet "
	    "over more than 70 countries around the world. \n\n"
	    "Press *Open Telesim* or button below to begin.")
	user_id = message.from_user.id

	if is_user_active(user_id):
		pass
	else:
		add_new_user(user_id)

	bot.send_message(message.chat.id,
	                 text=welcome_text,
	                 parse_mode="Markdown",
	                 reply_markup=web_app_inline_keyboard())

@bot.message_handler(func=lambda m: True)
def any_message_handler(message):
	bot.send_message(message.chat.id, "🤔")
