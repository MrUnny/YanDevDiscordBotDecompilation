# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\autorole2.py
# Compiled at: 2020-02-01 17:26:27
# Size of source mod 2**32: 1510 bytes
import asyncio, re, traceback, typing, datetime, discord
from discord.ext import commands
from discord.ext.commands import errors
import time, subprocess, select

class autorole2(commands.Cog):
    """autorole2"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def auto_role2(self):
        guild = self.bot.get_guild(411363271568785418)
        role2 = guild.get_role(672750684722167818)
        while True:
            try:
                for member in role2.members:
                    s = member.joined_at.__format__('%d/%m/%Y %H:%M:%S')
                    date = time.mktime(datetime.datetime.strptime(s, '%d/%m/%Y %H:%M:%S').utctimetuple()) + 86400
                    dt = datetime.datetime.today()
                    seconds = dt.utcnow().timestamp() + 43620
                    Test1 = int(round(date))
                    Test2 = int(round(seconds))
                    if Test1 < Test2:
                        await member.remove_roles(role2, reason=f"24 hours up, {member.name} is free!!!")
                        await asyncio.sleep(2)
                    else:
                        await asyncio.sleep(0.5)

            except:
                pass

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.auto_role2())


def setup(bot):
    bot.add_cog(autorole2(bot))