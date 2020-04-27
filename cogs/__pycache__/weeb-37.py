# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot\cogs\weeb.py
# Compiled at: 2020-02-03 02:39:26
# Size of source mod 2**32: 610 bytes
import asyncio, random
from datetime import datetime
from io import BytesIO
import math, discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils import checks, responses, default

class weeb(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    @commands.cooldown(3, 20, BucketType.user)
    async def null(self, ctx):
        await ctx.send('Null test completed.')


def setup(bot):
    bot.add_cog(weeb(bot))