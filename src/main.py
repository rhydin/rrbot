"""
rrbot
TODO: a good description
"""

from configuration import CONFIG, LOG_LEVEL, PREFIX, ROOT
import os, sys, logging

logging.basicConfig(
        filename=f'{ROOT}/logs/main.log',
        filemode='w',
        level=getattr(logging, LOG_LEVEL),
        format='[%(asctime)s|%(levelname)s]%(filename)s@L%(lineno)d - %(message)s'
)


# verify the database
from db import db_test
db_test()


# start building the bot up
from discord.ext import commands
from bot_utils import load_extension_directory, load_prefixes, prefix_operator


# output some boot up information

logging.info('Using `{}` as default command token.'.format(PREFIX))
load_prefixes()
bot = commands.Bot(command_prefix=prefix_operator)


# load the extensions

for ext in ['commands', 'events']:
    load_extension_directory(bot, ext)

import mqtt_client

# go live

logging.info('All aboard!')
if '-c' in sys.argv:
    print('Notice: This is not a live connection to any asyncio resources.  Discord is not running, mqtt will not respond. Database is accessible, however.  This is a test console for base functionality only.')
    import code
    code.interact(local=dict(globals(), **locals()))
else:
    bot.run(CONFIG['discord_client_secret'])
