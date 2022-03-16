import disnake as discord
from disnake.ext import commands
from api.check import utils
from api.server import base, main

from configs.config import marryct

class Marry(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("💕")
    async def marry(self, ctx, member: discord.Member):
        def check(msg):
            return msg.author != ctx.author and msg.author == member

        if member == ctx.author:
            await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_ERROR3")))
        elif base.user(ctx.author)[4] == 1:
            await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_ERROR").format(base.user(ctx.author)[3], ctx.prefix)))
        elif base.user(member)[4] == 1:
            await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_ERROR2").format(base.user(member)[3])))
        else:
            await ctx.send(f"{member.mention}")
            await ctx.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "MARRY_MSG").format(ctx.author.mention, member.mention)))
            response = await self.client.wait_for("message", check=check)
            if response.content.lower().strip() == "да" or response.content.lower().strip() == "Да":
                if member == ctx.author:
                    await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_ERROR3")))
                elif base.user(ctx.author)[4] == 1:
                    await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_ERROR").format(base.user(ctx.author)[3], ctx.prefix)))
                elif base.user(member)[4] == 1:
                    await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_ERROR2").format(base.user(member)[3])))
                else:
                    base.send(f"UPDATE users SET marry = '{ctx.author.id}' WHERE id = {member.id}")
                    base.send(f"UPDATE users SET _marry = 1 WHERE id = {member.id}")
                    base.send(f"UPDATE users SET marry = '{member.id}' WHERE id = '{ctx.author.id}'")
                    base.send(f"UPDATE users SET _marry = 1 WHERE id = {ctx.author.id}")
                    await ctx.send(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "MARRY_SUFF").format(member.mention, ctx.author.mention, ctx.prefix)))
                    category = discord.utils.get(ctx.guild.categories, id=marryct)
                    await ctx.guild.create_voice_channel(f'{ctx.author.name} 💕 {member.name}', category=category, user_limit=2)
                    channel = discord.utils.get(ctx.guild.channels, name=f'{ctx.author.name} 💕 {member.name}')
                    overwrite = channel.overwrites_for(ctx.guild.default_role)
                    overwrite.view_channel = False
                    overwrite.connect = False
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    await channel.set_permissions(ctx.author, view_channel = True, connect = True )
                    await channel.set_permissions(member, view_channel = True, connect = True )
                    base.send(f"UPDATE users SET channel = {channel.id} WHERE id = {ctx.author.id}")
                    base.send(f"UPDATE users SET channel = {channel.id} WHERE id = {member.id}")
            else:
                await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MARRY_NOPE").format(member.mention, ctx.author.mention)))

    @commands.command()
    async def divorce(self, ctx):
        def check(msg):
            return msg.author == ctx.author

        if base.user(ctx.author)[4] == 0:
            await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNMARRY_ERROR")))
        else:
            guildd = self.client.get_guild(ctx.guild.id)
            memberr = guildd.get_member(base.user(ctx.author)[3])
            await ctx.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "UNMARRY_MSG").format(ctx.author.mention, memberr.mention)))
            response = await self.client.wait_for("message", check=check)
            if response.content.lower().strip() == "да" or response.content.lower().strip() == "Да":
                if base.user(ctx.author)[4] == 0:
                    await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNMARRY_ERROR")))
                else:                
                    guild = self.client.get_guild(ctx.guild.id)
                    member = guild.get_member(base.user(ctx.author)[3])
                    channel = self.client.get_channel(base.user(ctx.author)[5])
                    await channel.delete()
                    await ctx.send(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "UNMARRY_SUFF").format(ctx.author.mention, member.mention)))
                    base.send(f"UPDATE users SET _marry = 0 WHERE id = {base.user(ctx.author)[3]}")
                    base.send(f"UPDATE users SET marry = NULL WHERE id = {base.user(ctx.author)[3]}")
                    base.send(f"UPDATE users SET marry = NULL WHERE id = {ctx.author.id}")
                    base.send(f"UPDATE users SET _marry = 0 WHERE id = {ctx.author.id}") 
                    base.send(f"UPDATE users SET channel = NULL WHERE id = {ctx.author.id}")
                    base.send(f"UPDATE users SET channel = NULL WHERE id = {base.user(ctx.author)[3]}")                          
            else:
                await ctx.send(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNMARRY_NOPE")))         

def setup(client):
    client.add_cog(Marry(client))