## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BQA4TqcHwciJnqIkENMmtZTlCSaCfDxhUENL301gGBzjQhiOH3zz3uMHb1wWS0sZNN4mhI4MArwvro16eHTfVyLXoLjA6-1dMyNAFu4-2CuDXtC6k9bwDkHXfQKY-Km4LQE_nyvmWiNBO6UEFgGJX6rbaDnGzHYxpUta4JoGi8jVOQ7S0bLJJT5GzuabPJk7bncotzf1SYcCWaDjtF9SIEEGoh13qwaGZ3HZq28OBPvuTpqy7nYqaeSQit58JLRccBFq_7g47suJlG44FnAqlG01uNOqd4atuBlYqJn-pZaSbVdutDtyIKved_p_yhnrXT17HDQxeVQdHKKNp2no-BAvAAAAAT4NoEIA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5873163824:AAESJ3RYzSXu5evI6wd-YwQ7IwL5lYf0ycA")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "18329555"))
API_HASH = getenv("API_HASH", "7bf83fddf8244fddfb270701e31470a8")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Fadil")
OWNER_USERNAME = getenv("OWNER_USERNAME", "CR7Suuuiiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "Fadil")
BOT_USERNAME = getenv("BOT_USERNAME", "vcvcvcvcvvvcccbot")
OWNER_ID = getenv("OWNER_ID", "5336047682")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FDAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5336047682").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
