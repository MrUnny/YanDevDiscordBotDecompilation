# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\autorole.py
# Compiled at: 2020-02-01 17:44:02
# Size of source mod 2**32: 2399 bytes
import asyncio, json, discord
from discord.ext import commands
from discord.ext.commands import BucketType
from io import BytesIO
from discord.utils import get
import subprocess, select
from utils import checks

class autorole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(checks.is_joel)
    async def setuproles(self, ctx):
        rolesmsg = await ctx.send('Creating roles...')
        guild = self.bot.get_guild(411363271568785418)
        try:
            await guild.create_role(name='Level 1')
            await guild.create_role(name='Level 2')
            await rolesmsg.edit(content='Creating roles... Done.')
        except:
            await rolesmsg.edit(content="I cannot do that, Prehaps I am missing the `Manage roles` permission? This is also necessary if I want to adjust everyone's roles.")

        channelmsg = await ctx.send('Creating super secret channel...')
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), 
         guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)}
        channel = await guild.create_text_channel('welcome-read-me', overwrites=overwrites)
        await channelmsg.edit(content='Creating super secret channel... done, you can change how you want this, I have already setup the permissions for you.')
        await channel.send('Done setting this channel permissions up! You can do whatever you need to do here!')

    @commands.command()
    @commands.check(checks.is_joel)
    async def roleset(self, ctx, member: discord.Member=None):
        role = ctx.guild.get_role(672750684029976576)
        edit = await ctx.send('adding role...')
        await member.add_roles(role)
        await edit.edit(content='adding role... done')

    @commands.command()
    @commands.check(checks.is_joel)
    async def preverify(self, ctx, member: discord.Member=None):
        role = ctx.guild.get_role(672750684029976576)
        role2 = ctx.guild.get_role(672750684722167818)
        edit = await ctx.send('Pre-verifying user...')
        await member.remove_roles(role)
        await member.remove_roles(role2)
        await edit.edit(content='Pre-verifying user... done')


def setup(bot):
    bot.add_cog(autorole(bot))