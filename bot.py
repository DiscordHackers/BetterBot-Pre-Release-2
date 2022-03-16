import disnake as discord
import os
import sqlite3
from disnake.ext import commands
from disnake.ext.commands import bot, check, MissingPermissions, has_permissions
from disnake.utils import get
from os import listdir

from api.check import support, utils
from api.server import base, main
from configs.config import *

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.guilds = True
intents.messages = True

async def get_prefix(client, message):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM guilds WHERE guild = {message.guild.id}")
    result = cursor.fetchone()
    return result[2]

client = commands.Bot(command_prefix = get_prefix, intents=discord.Intents.all())

client.remove_command("help")

for filename in listdir('./commands/'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
    else:
        if (filename != '__pycache__'):
            for file in listdir(f'./commands/{filename}/'):
                if file.endswith('.py'):
                    client.load_extension(f'commands.{filename}.{file[:-3]}')

for filename in os.listdir('./events/'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')

# --------------------
# | BOT DEV CATEGORY |
# --------------------

@client.command()
@utils.developer()
async def cload(ctx, extension):
    client.load_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была включена"))


@client.command()
@utils.developer()
async def cunload(ctx, extension):
    client.unload_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была отключена"))


@client.command()
@utils.developer()
async def creload(ctx, extension):
    client.reload_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была перезагружена"))


@client.command()
@utils.developer()
async def eload(ctx, extension):
    client.load_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было включено"))

@client.command()
@utils.developer()
async def eunload(ctx, extension):
    client.unload_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было отключено"))

@client.command()
@utils.developer()
async def ereload(ctx, extension):
    client.reload_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было перезагружено"))

client.run(token)