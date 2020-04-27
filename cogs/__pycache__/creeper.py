# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\creeper.py
# Compiled at: 2020-01-31 02:25:33
# Size of source mod 2**32: 3539 bytes
import os, discord, asyncio
from time import sleep
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import re
from utils import checks

class creeper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.guild.id != 411363271568785418:
                return
                if message.author.bot:
                    return
                if message.author == self.bot.user:
                    return
                try:
                    if not message.author.guild_permissions.ban_members:
                        passing = True
                    else:
                        return
                except:
                    return

                if passing == True:
                    regexes = ['^.{0,5}c\\s*r\\s*e\\s*e?\\s*e?\\s*p{1,2}\\s*e\\s*r\\s*,*\\s*a*w*\\s*m*\\s*a*\\s*n*\\s*',
                     '🇨\\s*🇷\\s*🇪\\s*🇪?\\s*🇵{1,2}\\s*🇪\\s*🇷',
                     '.*so\\s*we\\s*(b|🅱)ac(c|k)\\s*in\\s*the\\s*mine',
                     '.*got\\s*our\\s*pickaxe\\s*swinging\\s*from\\s*side\\s*to\\s*side',
                     'side to side',
                     '^.{0,5}i\\s*used\\s*to\\s*rule\\s*the\\s*world']
                    match = False
                    for regex in regexes:
                        try:
                            if re.search(regex, (message.content), flags=(re.IGNORECASE)):
                                if 'hugcreeper' in message.content.lower():
                                    match = False
                                elif 'joel_creeper' in message.content.lower():
                                    match = False
                                else:
                                    match = True
                        except:
                            print('fail')

                    if match:
                        try:
                            await message.delete()
                            Warn = f':warning: Deleted "Creeper" meme from **{message.author.name}**#{message.author.discriminator} ({message.author.id}) in <#{message.channel.id}>.'
                        except:
                            Warn = f':warning: Detected "Creeper" meme from **{message.author.name}**#{message.author.discriminator} ({message.author.id}) in <#{message.channel.id}>.'

                        self.bot.get_guild(615881983310036992).get_channel(615882185190408194).send(content=(f"{Warn}"),
                          embed=(discord.Embed().from_dict({'title':'Message Content:', 
                         'description':message.content, 
                         'color':16737380})))
                        try:
                            await message.author.send('Please don\'t do that "Creeper" meme. It\'s so spammy that even **I\'m** annoyed by it!')
                        except:
                            await message.channel.send(f"""{message.author.mention}, please don\'t do that "Creeper" meme. It\'s so spammy that even **I\'m** annoyed by it!""", delete_after=15)

                    else:
                        return
            else:
                return
        except:
            return


def setup(bot):
    bot.add_cog(creeper(bot))