from discord.ext import commands
import logging

logging.info('Loading `ping`')

@commands.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

def setup(bot):
    bot.add_command(ping)
