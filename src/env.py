from os import environ, path
from dotenv import dotenv_values

locals().update({
	**environ,
	**dotenv_values(".env.local", verbose=True)
})


if not "WEBHOOK_URL" in locals(): 
	WEBHOOK_URL = DEV_WEBHOOK_URL # pyright: ignore
else:
	WEBHOOK_URL = path.expandvars(WEBHOOK_URL) # pyright: ignore