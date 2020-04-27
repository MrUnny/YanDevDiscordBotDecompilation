# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot\cogs\autobanmessage.py
# Compiled at: 2020-04-06 19:17:25
# Size of source mod 2**32: 3556 bytes
import discord, asyncio, discord
from asyncio import sleep
from discord.ext import commands
from discord.ext.commands import BucketType
from discord.utils import get
from utils import filters, checks
from utils.filters import *
import os, json
from urllib.request import urlopen, Request, urlretrieve, URLopener
import requests
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent}

class Autobanmessage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.channel = self.bot.get_channel(685446255681339428)
        self.ban_reasons = {'link':'Posting a gremlin link. ~AoiBot', 
         'ytlink':'Posting a gremlin youtube video. ~AoiBot', 
         'badword':'Saying a banned phrase (Are you coding, racial, etc) ~AoiBot', 
         'milk':'Milk emoji ~AoiBot', 
         'name':'Illegal name', 
         'forceban':'Force ban: troll in #mission-mode ~AoiBot'}

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        checking for explicit content in messages and then banning
        """
        try:
            if message.author.guild_permissions.ban_members:
                return
            if message.author.bot:
                return
        except:
            return
        else:
            await sleep(0.1)
            if 'braincell' in message.content.lower():
                return
            if mission_re.search(message.content):
                if message.channel.id == 679263796371521537:
                    await message.author.ban(reason=(self.ban_reasons['forceban']))
                    return
            if links_re.search(message.content):
                await message.author.ban(reason=(self.ban_reasons['link']))
                return
            if yt_links_re.search(message.content):
                await message.author.ban(reason=(self.ban_reasons['ytlink']))
                return
            if milk_re.search(message.content):
                await message.author.ban(reason=(self.ban_reasons['milk']))
                return
            if words_re.search(message.content):
                await message.author.ban(reason=(self.ban_reasons['badword']))
                return
            if slurs_re.search(message.content):
                await message.author.ban(reason=(self.ban_reasons['badword']))
                return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await sleep(0.1)
        if words_re.search(member.display_name) or milk_re.search(member.display_name):
            await member.ban(reason=f"Innapropriate username ({member.name}) ~AoiBot")
        elif slurs_re.search(member.display_name):
            await member.ban(reason=f"Racial slur in username ({member.name}) ~AoiBot")

    @commands.Cog.listener()
    async def on_member_ban--- This code section failed: ---

 L.  90         0  LOAD_CONST               None
                2  RETURN_VALUE     

 L.  98         4  WITH_CLEANUP_START
                6  WITH_CLEANUP_FINISH
                8  END_FINALLY      

Parse error at or near `WITH_CLEANUP_START' instruction at offset 4


def setup(bot):
    bot.add_cog(Autobanmessage(bot))