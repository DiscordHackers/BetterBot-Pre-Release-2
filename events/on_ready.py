from datetime import datetime
import disnake as discord
from disnake.ext import commands, tasks
from configs.config import *
from api.server import base, main
import datetime, time

class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        #await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"help | client"))
        print("ptero start") # [[ Для того чтобы птеродактиль определил что сервер прошел инициализацию и уже запущен ]] #
        print("Успешно подключился к серверам Discord")
        print(f'Имя: {self.client.user.name}')
        print(f'ID: {self.client.user.id}')  

        for guild in self.client.guilds:
            print(guild.id , guild.name)

        channel = self.client.get_channel(versionid)
        await channel.edit(name = f'{versionname}: {version}')

        for guild in self.client.guilds:
            if base.guild(guild) is None:
                base.send(f"INSERT INTO guilds VALUES ('{guild.id}', '{guild.name}', '{prefix}', '{lang}')")
            else:
                pass
            
            for member in guild.members:
                if not member.bot:
                    try:
                        if base.user(member) is None:	
                            base.send(f"INSERT INTO users VALUES ('{guild.id}', '{member}', '{member.id}', NULL, 0, NULL)")
                        else:
                            pass
                    except:
                        continue                                               

def setup(client):
    client.add_cog(OnReady(client))