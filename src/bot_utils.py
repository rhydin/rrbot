import os, sys, logging
from configuration import ADMINS, PREFIXES, PREFIX
from discord.ext import commands
from pathlib import Path
from db import Session, bot_session, Servers, Channels

"""
Core utlities
"""

def load_extension_directory(bot, ext):
    cmd_path = os.path.join(os.getcwd(), ext)
    for f in os.listdir(cmd_path):
        if f == '__init__.py' or not f.endswith('.py'):
            continue
        bot.load_extension('commands.{}'.format(Path(f).stem))

def load_prefixes():
    global PREFIXES
    PREFIXES.clear()
    prefix_list = Servers.prefixed(bot_session)
    if prefix_list:
        for server in prefix_list:
            print('prefix {} => {}'.format(server.id, server.prefix))
            PREFIXES[server.id] = server.prefix

    prefix_list = Channels.prefixed(bot_session)
    if prefix_list:
        for channel in prefix_list:
            print('prefix {} => {}'.format(channel.id, channel.prefix))
            PREFIXES[channel.id] = channel.prefix

    print('Preloaded prefixes:\n{}'.format(PREFIXES))

def prefix_operator(bot, message):
    channel_id = message.channel.id
    server_id = message.guild.id
    return PREFIXES.get(channel_id, PREFIXES.get(server_id, PREFIX))

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

def db_session():
    """
    wrapper a command context in a database session
    """
    def predicate(ctx):
        ctx.db = Session()
        return True
    return commands.check(predicate)
