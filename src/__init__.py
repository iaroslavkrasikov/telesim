import flask
from src import env, bot, db

env = env.init(environ)
bot = bot.init(env.VERCEL_URL, env.TOKEN)
app = flask.Flask(__name__)

@app.route(f"/api/bot/{env.TOKEN}", methods=["POST"])
def bot_webhook(token):
	if flask.request.headers.get('content-type') == 'application/json':
		bot.process_webhook(upd_json=flask.request.get_data().decode('utf-8'))
		return ""
	else:
		flask.abort(403)