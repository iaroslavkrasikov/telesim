import hashlib
from os import environ, path
from dotenv import dotenv_values

env = {**environ, **dotenv_values(".env.local", verbose=True)}

env["WEBHOOK_URL"] = path.expandvars(env["WEBHOOK_URL"])

secret = f"{env['TOKEN']}WebAppData".encode("utf-8")
env["SECRET"] = hashlib.sha256(secret).hexdigest()

print("(env) loaded")
