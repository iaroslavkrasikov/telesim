from os import getenv as env
import psycopg
import telebot
import flask




# We have development env with dev WEBHOOK_URL and local dev DB
# And we have Vercel prod env where WEBHOOK_URL=VERCEL_URL.
# TOKEN is universal but stored only on Vercel env.
# We check current env, if dev then we add TOKEN to dev env
env = dotenv_values("../.env.local")
env["WEBHOOK_URL"] = env["VERCEL_URL"]
_env_TOKEN = env["TOKEN"]
if env["VERCEL_ENV"] == "development":
	env = dotenv_values("../.env.development.local")
	env["TOKEN"] = _env_TOKEN


db = psycopg.connect(env("POSTEGRES_SQL"))
bot = telebot.TeleBot(env("TOKEN"))
app = flask.Flask(__name__)


@bot.message_handler(func=lambda m: True)
def send_welcome(message):
	bot.reply_to(message, "Start")

@app.route("/api")
def index():
	return env.get("WEBHOOK_URL")


@app.route("/api", methods=["POST"])
def webhook():
	if flask.request.headers.get('content-type') == 'application/json':
		json_string = flask.request.get_data().decode('utf-8')
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])
		return ''
	else:
		flask.abort(403)