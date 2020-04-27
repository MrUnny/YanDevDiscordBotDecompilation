# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\advert.py
# Compiled at: 2020-01-31 02:25:33
# Size of source mod 2**32: 2685 bytes
import os, discord, asyncio
from time import sleep
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import re
from utils import checks

class advert(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, advert):
        try:
            if advert.guild.id != 411363271568785418:
                return
                if advert.author == self.bot.user:
                    return
                try:
                    if advert.author.guild_permissions.ban_members:
                        return
                except:
                    pass

                AD = False
                if 'discord.gg/' in advert.content.lower():
                    AD = True
            elif 'discord gg/' in advert.content.lower():
                AD = True
            elif AD == True:
                if 'discord.gg/yandere' in advert.content.lower():
                    return
                    if 'discord gg/yandere' in advert.content.lower():
                        return
                else:
                    try:
                        await message2.delete()
                        Warn = f":warning: Deleted server advertisement from **{advert.author.name}**#{advert.author.discriminator} ({advert.author.id}) in <#{advert.channel.id}>."
                    except:
                        Warn = f":warning: Detected server advertisement from **{advert.author.name}**#{advert.author.discriminator} ({advert.author.id}) in <#{advert.channel.id}>."

                    self.bot.get_guild(615881983310036992).get_channel(647565593649610772).send(content=(f"{Warn}"),
                      embed=(discord.Embed().from_dict({'title':'Message Content:', 
                     'description':advert.content, 
                     'color':16737380})))
                    try:
                        await advert.author.send("Hey! The rules say you can't advertise Discord servers here. If you want an invite link to this server, please use the `!discord` command instead.")
                    except:
                        await advert.channel.send(f"Hey, {advert.author.mention}! The rules say you can't advertise Discord servers here. If you want an invite link to this server, please use the `!discord` command instead.", delete_after=15)

            else:
                return
        except:
            return


def setup(bot):
    bot.add_cog(advert(bot))