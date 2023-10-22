from os import environ, path
from dotenv import dotenv_values

from .hash import hmac_sha256

env = {**environ, **dotenv_values(".env.local", verbose=True)}

env["WEBHOOK_URL"] = path.expandvars(env["WEBHOOK_URL"])

env["SECRET"] = hmac_sha256("WebAppData", env["TOKEN"])

print("(env) loaded")
