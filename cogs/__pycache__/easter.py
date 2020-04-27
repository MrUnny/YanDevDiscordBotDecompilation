# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot\cogs\easter.py
# Compiled at: 2020-03-24 16:56:50
# Size of source mod 2**32: 2054 bytes
import os, discord, asyncio
from time import sleep
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import re
from utils import checks

class easter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, easteregg):
        if easteregg.content.startswith('-'):
            return
            if 'Kill… Kill… Kill… 🔪' in easteregg.content:
                if easteregg.author.id == 614730255672016896:
                    await asyncio.sleep(2)
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(2)
                    await easteregg.channel.send('Calm down, <@614730255672016896>. No need to get so angry.')
                    await asyncio.sleep(6)
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(2)
                    await easteregg.channel.send('Wait... What is that in your hand?')
                    await asyncio.sleep(8)
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(2)
                    await easteregg.channel.send('Heh. Go to the counsellor office.')
            if ':kiwiblep:' in easteregg.content:
                if easteregg.author.id == 186907414270967808:
                    await easteregg.add_reaction('<:YanPet:619472223115280385>')
            if ':blep:' in easteregg.content:
                if easteregg.author.id == 186907414270967808:
                    await easteregg.add_reaction('<:YanPet:619472223115280385>')
        else:
            if ':yandComfy:' in easteregg.content:
                if easteregg.author.id == 135161245941628928:
                    await easteregg.add_reaction('<:YanPet:619472223115280385>')
            if ':YanCat:' in easteregg.content and easteregg.author.id == 135161245941628928:
                await easteregg.add_reaction('<:YanPet:619472223115280385>')


def setup(bot):
    bot.add_cog(easter(bot))