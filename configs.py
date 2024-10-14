

import os


class Config(object):
	API_ID = int(os.environ.get("26162072"))
	API_HASH = os.environ.get("ba25181c01b50d945748801b6c8b6ecc")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	UR_CHANNEL = os.environ.get("https://t.me/Filmone_Backup")
	UR_GROUP = os.environ.get("https://t.me/Filmone_Request")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("mongodb+srv://j32025026:<db_diTBNy6AvTzCpOYi>@cluster0.mmcgi.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", https://t.me/Filmone_Backup)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	HOME_TEXT = os.environ.get("HOME_TEXT")
