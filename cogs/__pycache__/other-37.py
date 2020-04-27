# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot - Copy\cogs\other.py
# Compiled at: 2020-04-08 18:22:11
# Size of source mod 2**32: 399 bytes
import asyncio, random, time, aiohttp, url_regex, os, datetime, discord
from discord.ext import commands
from discord.ext.commands import BucketType
import subprocess, select
from utils import checks

class other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(other(bot))