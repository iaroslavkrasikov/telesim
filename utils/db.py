import logging

from prisma import Prisma

db = Prisma()
db.connect()

logging.getLogger('prisma').setLevel(logging.DEBUG)
