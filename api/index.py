from os import environ as env
from dotenv import load_dotenv, find_dotenv
import telebot
import flask

load_dotenv("../.env.local")

WEBHOOK_URL = "https://" + env.get("VERCEL_URL")
if env.get("VERCEL_ENV") == "development":
	WEBHOOK_URL = env.get("DEV_WEBHOOK_URL")

bot = telebot.TeleBot(env.get("TOKEN"))
bot.set_webhook(url=WEBHOOK_URL)

app = flask.Flask(__name__)

@bot.message_handler(func=lambda m: True)
def send_welcome(message):
	bot.reply_to(message, "Start")

@app.route("/api")
def index():
	return WEBHOOK_URL


@app.route("/api", methods=["POST"])
def webhook():
	if flask.request.headers.get('content-type') == 'application/json':
		json_string = flask.request.get_data().decode('utf-8')
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])
		return ''
	else:
		flask.abort(403)

# class handler(BaseHTTPRequestHandler):
# 	def do_GET(self):
# 		self.send_response(200)
# 		self.send_header('Content-type','text/plain')
# 		self.end_headers()
# 		self.wfile.write("Hello".encode('utf-8'))
# 		return
# 	def do_POST(self):
# 		self.send_response(200)
# 		self.send_header('Content-type','text/plain')
# 		self.end_headers()
# 		content_len = int(self.headers.get('Content-Length'))
# 		bot.process_new_updates([telebot.types.Update.de_json(self.rfile.read(content_len).decode('utf-8'))])
# 		return