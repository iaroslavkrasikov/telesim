import flask

from .env import env
from . import bot

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/api")
def index():
	return flask.Response(status=200)

@app.route("/api/bot/hook", methods=["POST"])
def bot_webhook():
	headers = flask.request.headers
	content_type = headers.get("Content-Type")
	header_secret = headers.get("X-Telegram-Bot-Api-Secret-Token")

	if content_type == "application/json" and header_secret == env["SECRET"]:
		bot.process_update(upd_json=flask.request.get_data().decode("utf-8"))
		return flask.Response(status=204)
	else:
		return flask.Response(status=403)
