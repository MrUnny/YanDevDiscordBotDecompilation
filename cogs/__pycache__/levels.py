# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot - Copy\cogs\levels.py
# Compiled at: 2020-04-08 18:14:54
# Size of source mod 2**32: 1923 bytes
import asyncio, re, traceback, typing, datetime, discord
from discord.ext import commands, tasks
from discord.ext.commands import errors
import time, subprocess, select
from utils import checks

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class events(commands.Cog):
    """events"""

    def __init__(self, bot):
        self.bot = bot
        self.level_task.start()

    @tasks.loop(seconds=5)
    async def level_task(self):
        guild = self.bot.get_guild(486400307321110531)
        level1 = guild.get_role(697488638509842496)
        level2 = guild.get_role(697488678536347690)
        while True:
            print('loop start')
            for member in guild.members:
                s = member.joined_at.__format__('%d/%m/%Y %H:%M:%S')
                date = time.mktime(datetime.datetime.strptime(s, '%d/%m/%Y %H:%M:%S').utctimetuple())
                date1 = date + 100
                dt = datetime.datetime.utcnow()
                seconds = dt.timestamp()
                print('pass1')
                if date1 <= seconds:
                    print('pass2')
                    if member in level1.members:
                        if member not in level2.members:
                            print('pass3')
                            await member.add_roles(level2, reason='passed level1')
                            await member.remove_roles(level1)

            await asyncio.sleep(3)
            print('loop end')

    @level_task.before_loop
    async def before_task(self):
        print('waiting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(events(bot))