from configuration import ADMINS
from discord.ext import commands

def _is_bot_admin(user_id):
    return user_id in ADMINS

def is_bot_admin():
    """
    This is a command level check for bot administrators
    """
    def predicate(ctx):
        return _is_bot_admin(ctx.message.author)
    return commands.check(predicate)
