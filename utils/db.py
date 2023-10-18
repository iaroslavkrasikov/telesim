from psycopg import connect, sql, rows
from .env import env

db = connect(env['POSTGRES_URL'], autocommit=True, row_factory=rows.dict_row)

def get_all(table: str) -> list | None:
	return db.get(table)


def get_one(table: str, params: dict) -> dict | None:
	sql.SQL("select * from my_table where ({}) VALUES ({})").format(
		sql.SQL(', ').join(map(sql.Identifier, params)),
		sql.SQL(', ').join(sql.Placeholder() * len(params))).as_string()


	values_sql = sql.SQL(', ').join([sql.Identifier(key) for key in params.keys()])
	query = sql.SQL("SELECT * FROM {table_name} WHERE {} = %s").format(table_name=sql.Identifier(table),name="O'Rourke"))
    .as_string(conn))

	params_str = '(' + ''.join([f'(%{key})s, ' for key in params.keys()]) + ')'
	db.execute(f"select * from users where {params_str}", params.values()).fetchone()

def add(table: str, data: dict) -> int | None:
	if table in db:
		id = len(db[table])
		db[table].append({'id': id, **data})
		return id