import hashlib
from os import environ, path
from dotenv import dotenv_values

env = {**environ, **dotenv_values(".env.local", verbose=True)}

if not "WEBHOOK_URL" in env:
	env['WEBHOOK_URL'] = env["DEV_WEBHOOK_URL"]
else:
	env["WEBHOOK_URL"] = path.expandvars(env["WEBHOOK_URL"])

env["TOKEN_MD5"] = hashlib.md5(env["TOKEN"].encode("utf-8")).hexdigest()

print("(env) loaded")
