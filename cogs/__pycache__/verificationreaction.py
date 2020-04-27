# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot\cogs\verificationreaction.py
# Compiled at: 2020-03-13 16:06:22
# Size of source mod 2**32: 2400 bytes
import asyncio, re, traceback, typing, datetime, discord
from discord.ext import commands
from discord.ext.commands import errors
import time, subprocess, select
from utils import checks
reactactive = True

def disablereact():
    global reactactive
    reactactive = False


def enablereact():
    global reactactive
    reactactive = True


class verificationreaction(commands.Cog):
    """verificationreaction"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if reactactive == False:
            return
        channel = self.bot.get_channel(680775831840489502)
        if channel.id != 680775831840489502:
            return
        f = open('PicID.txt', 'r')
        number = f.read()
        number = int(number)
        channel = self.bot.get_channel(680775831840489502)
        message = await channel.fetch_message(number)
        guild = self.bot.get_guild(411363271568785418)
        guestrole = guild.get_role(674646545680826389)
        for reaction in message.reactions:
            async for user in reaction.users():
                if payload.member.id == 135161245941628928:
                    return
                await payload.member.add_roles(guestrole)
                return

    @commands.Cog.listener()
    async def on_message(self, verificationreaction):
        if verificationreaction.channel.id != 680775831840489502:
            return
        number = verificationreaction.id
        f = open('PicID.txt', 'w')
        f.write(f"{str(number)}")
        f.close()

    @commands.command()
    @commands.check(checks._owners)
    async def enableart(self, ctx):
        if reactactive == True:
            await ctx.send('React detection is already enabled.')
        else:
            enablereact()
            await ctx.send('React detection was enabled.')

    @commands.command()
    @commands.check(checks._owners)
    async def disableart(self, ctx):
        if reactactive == False:
            await ctx.send('React detection is already disabled.')
        else:
            disablereact()
            await ctx.send('React detection was disabled.')


def setup(bot):
    bot.add_cog(verificationreaction(bot))