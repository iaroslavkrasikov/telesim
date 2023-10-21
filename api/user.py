import json, hashlib, hmac
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from utils import env, db, hmac_sha256

def valid_init_data(init_data: dict) -> bool:
	# Sorted key=value\n string format as in Telegram docs
	init_data = dict(sorted(init_data.items()))
	hash = init_data['hash']
	del init_data['hash']
	data_check_string = ''.join([f'{key}={value}\n' for key, value in init_data.items()]).strip()

	if hmac_sha256(env['SECRET'], data_check_string, encode_key=False) != hash:
		return False

	return True

def verify(f):
	def decorator(handler: BaseHTTPRequestHandler):
		path = urlparse(handler.path)

		# NOTE: parse_qs() returns {key:[value]}
		init_data = {key: value[0] for key, value in parse_qs(path.query).items()}

		if not valid_init_data(init_data):
			print(f"(auth) client banned\n\t")
			handler.send_error(403)
			return

		init_data['user'] = json.loads(init_data['user'])

		return f(handler, init_data)

	return decorator

class handler(BaseHTTPRequestHandler):
	@verify
	def do_GET(self, init_data):

		user = db.user.find_unique(where={'telegram_id': init_data['user']['id']})

		if user is None:
			user = db.user.create({
			    'telegram_id': init_data['user']['id'],
			})

		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(user.model_dump_json().encode('utf-8'))
		return
