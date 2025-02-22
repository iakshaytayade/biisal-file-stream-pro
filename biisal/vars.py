# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Bɪɪsᴀʟ Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/bisal_files"
bisal_grp = "https://t.me/+PA8OPL2Zglk3MDM1"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '29052852'))
    API_HASH = str(getenv('API_HASH', '0af68ba2f02e73ee4909678f33f8810c'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7621804139:AAHitPsq7WRcy2PQGAv1_rvzuFCIncdSZfM'))
    name = str(getenv('name', 'Rt_filetolink_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002456975976'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002431362405'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "5150993718").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'iakshaytayade'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://iakshaytayade:iakshaytayade@cluster0.7ujhg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'https://t.me/+Em9hcJaiR7JhZTg1')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002304030275")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1002302473574")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @biisal_bot ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
