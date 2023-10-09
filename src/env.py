from dotenv import dotenv_values

class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def init(environ):
	return AttributeDict({
    	**dotenv_values(".env.local"),
    	**environ
	})