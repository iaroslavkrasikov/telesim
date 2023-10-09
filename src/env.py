from os import environ
from dotenv import dotenv_values

locals().update({
	**environ,
	**dotenv_values(".env.local", verbose=True)
})

if not "WEBHOOK_URL" in locals(): WEBHOOK_URL = DEV_WEBHOOK_URL # pyright: ignore