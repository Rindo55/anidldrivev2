from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Telegram API credentials obtained from https://my.telegram.org/auth
API_ID=10247139
API_HASH="96b46175824223a33737657ab943fd6a"
BOT_TOKENS = os.getenv("BOT_TOKENS", "6417602347:AAELMBu-V_FwqI5fA8v5L3RmRiAVqh70jKQ").strip(", ").split(",")
BOT_TOKENS = [token.strip() for token in BOT_TOKENS if token.strip() != ""]  # Clean up any extra spaces
STORAGE_CHANNEL=-1001503950731
DATABASE_BACKUP_MSG_ID=5
# List of Premium Telegram Account Pyrogram String Sessions used for file upload/download operations
STRING_SESSIONS = os.getenv("STRING_SESSIONS", "").strip(", ").split(",")
STRING_SESSIONS = [
    session.strip() for session in STRING_SESSIONS if session.strip() != ""
]

# Chat ID of the Telegram storage channel where files will be stored


# Message ID of a file in the storage channel used for storing database backups
#r database backup

# Password used to access the website's admin panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "MrBorn2Help")  # Default to "admin" if not set

# Determine the maximum file size (in bytes) allowed for uploading to Telegram
# 1.98 GB if no premium sessions are provided, otherwise 3.98 GB
if len(STRING_SESSIONS) == 0:
    MAX_FILE_SIZE = 1.98 * 1024 * 1024 * 1024  # 2 GB in bytes
else:
    MAX_FILE_SIZE = 3.98 * 1024 * 1024 * 1024  # 4 GB in bytes

# Database backup interval in seconds. Backups will be sent to the storage channel at this interval
DATABASE_BACKUP_TIME = int(
    os.getenv("DATABASE_BACKUP_TIME", 60)
)  # Default to 60 seconds

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", 60))  # Default to 60 seconds

# Choose whether to use .session files for session persistence or in-memory sessions
# Set to False to use in-memory sessions instead of .session files
USE_SESSION_FILE = bool(
    os.getenv("USE_SESSION_FILE", True)
)  # Default to True (use .session files)


# Domain to auto-ping and keep the website active
WEBSITE_URL = os.getenv("WEBSITE_URL", None)
