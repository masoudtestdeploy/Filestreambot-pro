# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(2669389)
    API_HASH = str('59f112100d19186dc03cd93fb7f2904a')
    BOT_TOKEN = str(getenv('BOT_TOKEN','5178931446:AAElUPUREIbc4q19dBkcthYZku0lKQB4eSo'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'filetolijnkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001684448513'))
    PORT = int(getenv('PORT', 443))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '185.110.191.15'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "a_msd_aaa").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'kmb.kenzodl.xyz')) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://masoudbiatomoviez:12345678VB@cluster0.jigze.mongodb.net/Cluster0?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
