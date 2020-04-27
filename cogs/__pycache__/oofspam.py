# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\oofspam.py
# Compiled at: 2020-02-01 02:32:38
# Size of source mod 2**32: 3735 bytes
import os, discord, asyncio
from time import sleep
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import re
from utils import checks

class oofspam(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message2):
        try:
            if message2.guild.id != 411363271568785418:
                return
                if message2.author.bot:
                    return
                if message2.author == self.bot.user:
                    return
                try:
                    if message2.author.guild_permissions.ban_members:
                        return
                except:
                    return
                else:
                    oofer = False
                    if 'oof' == message2.content.lower():
                        oofer = True
            else:
                if 'oof.' == message2.content.lower():
                    oofer = True
                elif 'oof!' == message2.content.lower():
                    oofer = True
                elif 'oof-' == message2.content.lower():
                    oofer = True
                elif 'f' == message2.content.lower():
                    oofer = True
                elif 'oop-' == message2.content.lower():
                    oofer = True
                elif 'oop' == message2.content.lower():
                    oofer = True
                elif 'and i oop' == message2.content.lower():
                    oofer = True
                elif 'oop-' == message2.content.lower():
                    oofer = True
                elif 'and i oop-' == message2.content.lower():
                    oofer = True
                elif 'i-' == message2.content.lower():
                    oofer = True
                elif 'rip' == message2.content.lower():
                    oofer = True
                elif 'ripp' == message2.content.lower():
                    oofer = True
                elif 'ew' == message2.content.lower():
                    oofer = True
                if oofer == True:
                    try:
                        await message2.delete()
                        Warn = f':warning: Deleted "spam" message from **{message2.author.name}**#{message2.author.discriminator} ({message2.author.id}) in <#{message2.channel.id}>.'
                    except:
                        Warn = f':warning: Detected "spam" message from **{message2.author.name}**#{message2.author.discriminator} ({message2.author.id}) in <#{message2.channel.id}>.'

                    await self.bot.get_guild(615881983310036992).get_channel(615882185190408194).send(content=(f"{Warn}"),
                      embed=(discord.Embed().from_dict({'title':'Message Content:', 
                     'description':message2.content, 
                     'color':16737380})))
                    try:
                        await message2.author.send('Non-words like "bruh," "oof," "oop," "rip," "ew," "I-," and "f" don\'t contribute anything meaningful to discussions and are no different from spam. Please don\'t fill the chat with messages like these.')
                    except:
                        await message2.channel.send(f"""{message2.author.mention}, non-words like "bruh," "oof," "oop," "rip," "ew," "I-," and "f" don\'t contribute anything meaningful to discussions and are no different from spam. Please don\'t fill the chat with messages like these.""", delete_after=15)

                else:
                    return
        except:
            return


def setup(bot):
    bot.add_cog(oofspam(bot))