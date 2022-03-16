from datetime import datetime
import disnake as discord
from disnake.ext import commands
from configs.config import *
from api.server import base, main


class OnGuildJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for member in guild.members:
            if not member.bot:
                try:
                    # * Включение логов в канал замедляет запись
                    if base.user(member) is None:
                        base.send(f"INSERT INTO users VALUES ('{guild.id}', '{member}', {member.id}, NULL, 0, NULL)")
                    else:
                        pass
                except:
                    continue

        if base.guild(guild) is None:
            base.send(f"INSERT INTO guilds VALUES ('{guild.id}', '{guild.name}', '{prefix}', '{lang}')")
        else:
            pass

def setup(client):
    client.add_cog(OnGuildJoin(client))