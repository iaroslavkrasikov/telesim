from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json, hashlib

from utils import env, db

def valid_init_data(init_data: dict) -> bool:
	# Sorted key=value\n string format as in Telegram docs
	init_data = dict(sorted(init_data.items()))
	data_check_string = ''.join([f'{key}={value}\n' for key, value in init_data.items()])
	_dcs = f"{data_check_string}{env['SECRET']}".encode('utf-8')

	if hashlib.sha256(_dcs).hexdigest() != init_data['hash']:
		return False

	return True

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		path = urlparse(self.path)
		# parse_qs returns {key:[value]}
		init_data = {key: value[0] for key, value in parse_qs(path.query).items()}

		if not valid_init_data(init_data):
			self.send_response(403)
			return

		init_data['user'] = json.loads(init_data['user'])

		db.get_one('users', {'id': init_data['user']['id']})

		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write('Hello, world!'.encode('utf-8'))
		return

@handler.get({'id': int})
def get(id):
	user = db.get_one('users', {'id': id})

	if user is None:
		hand
		new_user = db.add('users', {''})
