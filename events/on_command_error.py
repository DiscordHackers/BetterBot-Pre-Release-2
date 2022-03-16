import disnake as discord
import traceback
from datetime import datetime
from disnake.ext import commands
from disnake.ext.commands import MissingPermissions, BotMissingPermissions, CommandNotFound, BadArgument, MissingRequiredArgument
from api.server import main
from configs.config import *

class OnCommandError(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):

        if isinstance(exception, MissingPermissions):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_PERMISSIONS")))
        elif isinstance(exception, MissingRequiredArgument):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_ARGS")))
        elif isinstance(exception, BadArgument):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_TRYARGS")))
        elif isinstance(exception, BotMissingPermissions):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_BOTPERMISSIONS")))
        elif isinstance(exception, commands.CommandOnCooldown): 
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR_CD").format(round(int(exception.retry_after) / 60))))
        elif isinstance(exception, CommandNotFound):
            return
            
def setup(client):
    client.add_cog(OnCommandError(client))