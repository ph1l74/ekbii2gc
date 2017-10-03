import os

feed_url = os.environ['FEED_URL']
calendar_id = os.environ['CAL_ID']
token = os.environ['TOKEN']
token_name = os.environ['TOKEN_NAME']

db = {"user": os.environ['DB_USER'],
      "password": os.environ['DB_PASS'],
      "address": os.environ['DB_ADDRESS'],
      "port": os.environ['DB_PORT'],
      "db_name": os.environ['DB_NAME']}

bot_token = os.environ['BOT_TOKEN']