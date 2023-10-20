import hashlib, hmac

def hmac_sha256(key, msg, hex=True, encode_key=True, encoding='utf-8') -> str | bytes:
	if encode_key:
		key = key.encode(encoding)

	msg = msg.encode(encoding)
	sign = hmac.new(key, msg, hashlib.sha256)

	if hex:
		return sign.hexdigest()
	else:
		return sign.digest()
