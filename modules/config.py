import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "26030478"))
API_HASH = getenv("API_HASH", "176fa1a0a1316f8517dbf941d8bdf5ef")
BOT_TOKEN = getenv("BOT_TOKEN", "6569449035:AAGNN6l7c6F41wSipOlIW6Ul5b2bX1s09KY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "2400"))
STRING_SESSION = getenv("STRING_SESSION", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
