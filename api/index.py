import telebot
import flask
from werkzeug.middleware.proxy_fix import ProxyFix

TOKEN="6489626721:AAESYIEpSOFBDFJp3fjfJ_6qC8azb8a_Z1Q"
DEBUG=True

bot = telebot.TeleBot(TOKEN)
bot.set_webhook(url="https://vtct6rkk-5173.euw.devtunnels.ms/api")

app = flask.Flask(__name__)

@bot.message_handler(func=lambda m: True)
def send_welcome(message):
	bot.reply_to(message, "Start")

@app.route("/api")
def index():
	return "HELLO!"

@app.route("/api", methods=["POST"])
def webhook():
	if flask.request.headers.get('content-type') == 'application/json':
		json_string = flask.request.get_data().decode('utf-8')
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])
		return " XX "
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