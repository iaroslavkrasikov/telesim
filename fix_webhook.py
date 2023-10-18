import sys
import telebot
import logging
from server.env import env

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env["TOKEN"])

webhook_info = bot.get_webhook_info()
WEBHOOK_URL = env["WEBHOOK_URL"]

if "prod" in sys.argv:
	WEBHOOK_URL = "https://telesim-mu.vercel.app/api/bot/"

bot.set_webhook(WEBHOOK_URL, secret_token=env["SECRET"])
