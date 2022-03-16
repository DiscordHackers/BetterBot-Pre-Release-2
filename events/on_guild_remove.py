from datetime import datetime
import disnake as discord
from disnake.ext import commands
from api.server import base, main
from configs.config import *

class OnGuildRemove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        for member in guild.members:
            try:
                if base.user(member) is not None:
                    base.send(f"DELETE FROM users WHERE guild = {guild.id}")
                    
                else:
                    pass
            except:
                continue

        if base.guild(guild) is not None:
            base.send(f"DELETE FROM guilds WHERE guild = {guild.id}")
        else:
            pass


def setup(client):
    client.add_cog(OnGuildRemove(client))