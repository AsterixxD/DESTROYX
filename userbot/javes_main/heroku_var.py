import os
cIient = "@DXplugins"
cIientt = "@DXplugins"
import asyncio
from sys import version_info
from logging import *
from distutils.util import strtobool as sb
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
load_dotenv("config.env")
from distutils.util import strtobool as sb


class config(object):
    API_KEY = os.environ.get("TELEGRAM_API_KEY", None)
    APP_ID = os.environ.get("TELEGRAM_API_KEY", None)
    API_HASH = os.environ.get("TELEGRAM_API_HASH", None)
    TAG_LOG =int(os.environ.get("TAG_LOG",None))
    STRING_SESSION = os.environ.get("TELEGRAM_STRING_SESSION", None)
    SCREEN_SHOT_KEY = os.environ.get("SCREEN_SHOT_KEY", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = SCREEN_SHOT_KEY
    BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    CMD_HNDLR = os.environ.get("CMD_HNDLR", None)
    SUDO_HNDLR = os.environ.get("SUDO_HNDLR", None)
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    GENIUS = os.environ.get("GENIUS_API_TOKEN", None)
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    ENV = os.environ.get("ENV", False)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)
    AFK_MESSAGE = os.environ.get("AFK_MESSAGE", None)
    ALIVE_S_MESSAGE = os.environ.get("ALIVE_S_MESSAGE", None)
    BIO_MESSAGE = os.environ.get("BIO_MESSAGE", None)
    ALIVE_E_MESSAGE = os.environ.get("ALIVE_E_MESSAGE", None)
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    PM_AUTO_BAN = sb(os.environ.get("PM_PROTECTOR", "True"))
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY","./downloads")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    PM_MESSAGE = os.environ.get('PM_MESSAGE', None)
    JAVES_NAME = os.environ.get("JAVES_NAME", None)
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ALIVE_NAME = os.environ.get("YOUR_SHORT_NAME", None)
    BLOCK_MESSAGE = os.environ.get("BLOCK_MESSAGE", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_APIKEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APPNAME", None)
    HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
    HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
    UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL","https://github.com/CRiMiNaL786/DESTROYX")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Javes")
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    PRIVATE_GROUP_ID = os.environ.get("BOTLOG_CHATID", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TAG_LOG =int(os.environ.get("TAG_LOG",None))
    TMP_DOWNLOAD_DIRECTORY=TEMP_DOWNLOAD_DIRECTORY



class Config(object):
    API_KEY = os.environ.get("TELEGRAM_API_KEY", None)
    TAG_LOG =int(os.environ.get("TAG_LOG",None))
    APP_ID = os.environ.get("TELEGRAM_API_KEY", None)
    API_HASH = os.environ.get("TELEGRAM_API_HASH", None)
    STRING_SESSION = os.environ.get("TELEGRAM_STRING_SESSION", None)
    BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    GENIUS = os.environ.get("GENIUS_API_TOKEN", None)
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    ENV = os.environ.get("ENV", False)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)
    AFK_MESSAGE = os.environ.get("AFK_MESSAGE", None)
    ALIVE_S_MESSAGE = os.environ.get("ALIVE_S_MESSAGE", None)
    BIO_MESSAGE = os.environ.get("BIO_MESSAGE", None)
    ALIVE_E_MESSAGE = os.environ.get("ALIVE_E_MESSAGE", None)
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    PM_AUTO_BAN = sb(os.environ.get("PM_PROTECTOR", "True"))
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY","./downloads")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    PM_MESSAGE = os.environ.get('PM_MESSAGE', None)
    JAVES_NAME = os.environ.get("JAVES_NAME", None)
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ALIVE_NAME = os.environ.get("YOUR_SHORT_NAME", None)
    BLOCK_MESSAGE = os.environ.get("BLOCK_MESSAGE", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_APIKEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APPNAME", None)
    HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
    HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
    UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL","https://github.com/CRiMiNaL786/DESTROYX")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Javes")
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    PRIVATE_GROUP_ID = os.environ.get("BOTLOG_CHATID", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    SCREEN_SHOT_KEY = os.environ.get("SCREEN_SHOT_KEY", None)
    TAG_LOG =int(os.environ.get("TAG_LOG",None))
    SCREEN_SHOT_LAYER_ACCESS_KEY = SCREEN_SHOT_KEY
    TMP_DOWNLOAD_DIRECTORY=TEMP_DOWNLOAD_DIRECTORY

class Development(config):
    LOGGER = True



