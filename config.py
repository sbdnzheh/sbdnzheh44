from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f9d65bf4364e302d6e532.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f9d65bf4364e302d6e532.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/R_Q_R7")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/H_H_H_P")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1213559434").split()))


FAILED = "https://telegra.ph/file/f9d65bf4364e302d6e532.jpg"
