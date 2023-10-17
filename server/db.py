import psycopg
from .env import env

db = psycopg.connect(env['POSTGRES_URL'])

def get(table, data):
	# TODO
	if table == "user":
		return {"is_active": False}

def create(table, data):
	pass
