from configuration import ADMINS
from discord.ext import commands
from pathlib import Path
import os, sys

"""
Core utlities
"""

def load_extension_directory(bot, ext):
    cmd_path = os.path.join(os.getcwd(), ext)
    for f in os.listdir(cmd_path):
        if f == '__init__.py' or not f.endswith('.py'):
            continue
        bot.load_extension('commands.{}'.format(Path(f).stem))


"""
Auxiliary utiltizes
"""

def _is_bot_admin(user_id):
    return user_id in ADMINS

def is_bot_admin():
    """
    This is a command level check for bot administrators
    """
    def predicate(ctx):
        return _is_bot_admin(ctx.message.author)
    return commands.check(predicate)
