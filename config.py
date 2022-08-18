from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/FallenXBots")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

