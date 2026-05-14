

from os import environ

API_ID = int(environ.get("API_ID", "20807000"))
API_HASH = environ.get("API_HASH", "cde2366a7c61e23f4cb44618cbe6cf70")
BOT_TOKEN = environ.get("BOT_TOKEN", "8564398983:AAGxMpPkmLcgZsPnVzIQzCUIro5KNk76QBw")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/+jZIAVLX-rWQ1OGU9")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "890749443").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "890749443"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "-1003646612944")





