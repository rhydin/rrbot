from discord.ext import commands
from bot_utils import _is_bot_admin
import logging

logging.info('Loading `admin commands`')

class AdminCog(commands.Cog, name='Bot Administrator Commands'):
    def __init__(self, bot):
        self.bot = bot

    def cog_check(self, ctx):
        """
        This checks to ensure only listed administrators can execute the commands in this cog.
        """
        id = ctx.message.author.id
        logging.info('Administrator check: {}'.format(id))
        logging.info(ctx.message.content)
        return _is_bot_admin(id)

    @commands.command(name='shutdown')
    async def shutdown(self, ctx):
        await ctx.bot.logout()

def setup(bot):
    bot.add_cog(AdminCog(bot))
