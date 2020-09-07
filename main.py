"""
rrbot
TODO: a good description
"""

import sys, logging
logging.basicConfig(filename='logs/main.log', filemode='w', level=logging.DEBUG)

from discord.ext import commands
from configuration import CONFIG, PREFIX
from database import DB
from bot_utils import load_extension_directory


# output some boot up information

logging.info('Using `{}` as command token.'.format(PREFIX))
bot = commands.Bot(command_prefix=PREFIX)


# load the extensions

for ext in ['commands', 'events']:
    load_extension_directory(bot, ext)


# go live

logging.info('All aboard!')
if '-c' in sys.argv:
    import code
    code.interact(local=dict(globals(), **locals()))
else:
    bot.run(CONFIG['discord_client_secret'])
