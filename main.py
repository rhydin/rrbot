"""
rrbot
TODO: a good description
"""
from discord.ext import commands
from configuration import CONFIG, PREFIX
from database import DB
import sys
from bot_utils import load_extension_directory


# output some boot up information

print('Using `{}` as command token.'.format(PREFIX))
bot = commands.Bot(command_prefix=PREFIX)


# load the extensions

for ext in ['commands', 'events']:
    load_extension_directory(bot, ext)


# go live

print('All aboard!')
if '-c' in sys.argv:
    import code
    code.interact(local=dict(globals(), **locals()))
else:
    bot.run(CONFIG['discord_client_secret'])
