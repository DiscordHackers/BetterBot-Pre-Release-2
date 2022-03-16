import disnake as discord
import sqlite3

from configs.config import *

def guild(guild):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM guilds WHERE guild = {guild.id}")
    result = cursor.fetchone()

    return result
    
def user(user):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE guild = {user.guild.id} AND id = {user.id}")
    result = cursor.fetchone()

    return result

def send(result):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    print(result)
    cursor.execute(result)
    connection.commit()