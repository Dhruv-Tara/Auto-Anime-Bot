# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara

import json
import logging

from pyrogram import Client


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(),logging.FileHandler('logging.txt')]
)
LOG = logging.getLogger('AutoAnimeBot')



with open("./AAB/config.json","r") as Config :
    Vars = json.load(Config)

LOG.info(f"Written By : {Vars['Author']}")
LOG.info(f"Licensed Under : {Vars["Licensed_under"]}")

# VARS 

try :

    production_chat = Vars['production_chat']
    file_channel = Vars['files_channel']
    Main_Channel = Vars['main_channel']
    Owner = Vars['owner']
    Db_Uri = Vars['database_url']
    api_id = Vars['api_id']
    api_hash = Vars['api_hash']
    main_bot_token = Vars['main_bot']
    client_bot_token = Vars['client_bot']
    thumbnail_url = Vars['thumbnail_url']

except Exception as e :
    LOG.critical("Important Vars are not filled properly fill it in config.json")


# You can change it As u want to but It should have 3 brackets.  || go to __main__.py and change it
    
post_message = """
🔸 {}
➖〰️➖〰️➖〰️➖〰️➖〰️
🔸 Episode - {}
〰️➖〰️➖〰️➖〰️➖〰️➖
🔸 Status - {}
➖〰️➖〰️➖〰️➖〰️➖〰️
🔸 Quality - Sub
〰️➖〰️➖〰️➖〰️➖〰️➖
"""





file_client = Client(
    "FileBot",
    api_id= api_id ,
    api_hash= api_hash,
    bot_token= client_bot_token
)


bot = Client(
    "mainbot",
    api_id= api_id,
    api_hash= api_hash,
    bot_token= main_bot_token
)



