import os
from os import environ

class Config:
    API_ID = environ.get("API_ID", "34446649")
    API_HASH = environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7972923352:AAHbU7f96-9eXkhgJREX8qcYLjGt_mXDx4k") 
    BOT_SESSION = environ.get("BOT_SESSION", "Arohi_X_bot") 
    
    # FIX: Checks both common names for the MongoDB string
    DATABASE_URI = environ.get("DATABASE_URI", environ.get("DATABASE", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0"))
    DATABASE_NAME = environ.get("DATABASE_NAME", "Anujedit")
    
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7892805795').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003515041061'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "log_channel_a") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    
    # Ensure PORT is an integer for Gunicorn/Web server
    PORT = int(environ.get('PORT', '5000'))

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
