import flask

from .env import env
from . import bot

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/api")
def index():
	return flask.Response(status=200)

@app.route("/api/bot", methods=["POST"])
def bot_webhook():
	headers = flask.request.headers
	content_type = headers.get("Content-Type")
	header_token = headers.get("X-Telegram-Bot-Api-Secret-Token")

	if content_type == "application/json" and header_token == env["TOKEN_MD5"]:
		bot.process_update(upd_json=flask.request.get_data().decode("utf-8"))
		return flask.Response(status=204)
	else:
		return flask.Response(status=403)
