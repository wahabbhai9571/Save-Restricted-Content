# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25405777"))
API_HASH = getenv("API_HASH", "6bff46327fffc7e03fa30a1ed19c5ce0")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8007695130").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fibegi:8oV4fjNNVasSfcoY@cluster0.jp8thup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002648848764")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002881363429"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "999999"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
