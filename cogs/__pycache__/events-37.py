# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot - Copy\cogs\events.py
# Compiled at: 2020-04-13 19:20:34
# Size of source mod 2**32: 2862 bytes
import asyncio, re, traceback, typing, datetime, discord
from discord.ext import commands
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

    @commands.Cog.listener()
    async def status_task(self, delay: int, statuses: typing.Tuple[(discord.Activity, discord.Streaming)]) -> None:
        while 1:
            for status in statuses:
                await self.bot.change_presence(activity=status)
                await asyncio.sleep(delay)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            await send_cmd_help(ctx)
        elif isinstance(err, errors.CommandInvokeError):
            err = err.original
            _traceback = traceback.format_tb(err.__traceback__)
            _traceback = ''.join(_traceback)
            error = '```py\n{2}{0}: {3}\n```'.format(type(err).__name__, ctx.message.content, _traceback, err)
            await ctx.send(f"There was an error processing the command ;-;\n{error}")
        elif isinstance(err, errors.CheckFailure):
            pass
        elif isinstance(err, errors.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown... try again in {err.retry_after:.2f} seconds.", delete_after=10)
        elif isinstance(err, errors.CommandNotFound):
            pass
        elif isinstance(err, errors.MissingRole):
            await ctx.send(f"This command requires to be subscribed to YandereDev on twitch, {ctx.author.name}.")

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            print(f"Command: {ctx.message.clean_content} || Member: {ctx.author}|{ctx.author.id} || Server:{ctx.guild}|{ctx.guild.id}\n-----------------")
        except AttributeError:
            print(f"Private message> {ctx.author}> {ctx.message.clean_content}")

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')
        print("I'm ready!")
        print(f"{len(set(self.bot.get_all_members()))} members!")
        self.bot.loop.create_task(self.status_task(20, checks.status_list))


def setup(bot):
    bot.add_cog(events(bot))