import psycopg
from .env import env

print(env['POSTGRES_URL'])

db = psycopg.connect('postgresql://postgres:root@localhost:5432/telesim')

def get(table, data):
	# TODO
	if table == "user":
		return {"is_active": False}

def create(table, data):
	pass
