from discord.ext import commands

print('Loading `ping`')

@commands.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

def setup(bot):
    bot.add_command(ping)
