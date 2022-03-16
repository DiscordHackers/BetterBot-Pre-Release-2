import disnake as discord
import json
import sqlite3
import datetime
import random
from api.server import base

from configs.config import *


def get_lang(guild, key):
    with open(f'data/languages/{base.guild(guild)[3]}.json', encoding='utf-8') as f:
        data = json.load(f)

    return data[key]

def done(guild, args):
    em = discord.Embed(colour=0x2ecc70, title=f'{okay} | {get_lang(guild, "EMBED_DONE")}', description=args)
    return em

def warn(guild, args):
    em = discord.Embed(colour=0x2ecc70, title=f'{warning} | {get_lang(guild, "EMBED_WARN")}', description=args)
    return em

def deny(guild, args):
    em = discord.Embed(colour=0xe74444, title=f'{error} | {get_lang(guild, "EMBED_DENY")}', description=args)
    return em

def ban(guild, args):
    em = discord.Embed(colour=0xe74444, title=f'{error} | {get_lang(guild, "EMBED_BAN")}', description=args)
    return em