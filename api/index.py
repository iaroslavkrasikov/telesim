import flask
import hashlib

from src import env, bot, db

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/api")
def index():
	return flask.Response(status=200)

@app.route("/api/bot", methods=["POST"])
def bot_webhook():
	headers = flask.request.headers
	if  headers.get("Content-Type") == "application/json" and \
		headers.get("X-Telegram-Bot-Api-Secret-Token") == env.TOKEN_MD5: 

		bot.process_update(upd_json=flask.request.get_data().decode('utf-8'))
		
		return flask.Response(status=204)
	else:
		return flask.Response(status=403)