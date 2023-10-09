import logging

import flask

from src import env, bot, db

app = flask.Flask(__name__)

@app.route("/api")
def index():
	return env.WEBHOOK_URL

@app.route(f"/api/bot/{env.TOKEN}", methods=["POST"])
def bot_webhook():
	if flask.request.headers.get('content-type') == 'application/json':
		bot.process_webhook(upd_json=flask.request.get_data().decode('utf-8'))
		return ""
	else:
		flask.abort(403)