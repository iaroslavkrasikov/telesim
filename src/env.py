from os import environ, path
import hashlib
from dotenv import dotenv_values

print("test " * 6)

locals().update({
	**environ,
	**dotenv_values(".env.local", verbose=True)
})

if not "WEBHOOK_URL" in locals(): 
	WEBHOOK_URL = DEV_WEBHOOK_URL # pyright: ignore
else:
	WEBHOOK_URL = path.expandvars(WEBHOOK_URL) # pyright: ignore

TOKEN_MD5 = hashlib.md5(TOKEN.encode("utf-8")).hexdigest() # pyright: ignore
						