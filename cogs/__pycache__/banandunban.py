# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\banandunban.py
# Compiled at: 2020-02-01 01:27:54
# Size of source mod 2**32: 3021 bytes
import asyncio, json, discord
from discord.ext import commands
from discord.ext.commands import BucketType
from io import BytesIO
import subprocess, select
from utils import checks

class banandunban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ownerping):
        ping = False
        if '<@396241937658675206>' in ownerping.content.lower():
            if ownerping.author.id == 396241937658675206:
                return
            ping = True
        elif ping == True:
            Warn = f":warning: Detected ping from **{ownerping.author.name}**#{ownerping.author.discriminator} ({ownerping.author.id}) in <#{ownerping.channel.id}>."
            await self.bot.get_guild(486400307321110531).get_channel(639275263716229120).send(content=(f"{Warn}"),
              embed=(discord.Embed().from_dict({'title':'Message Content:', 
             'description':ownerping.content, 
             'color':16737380})))
        else:
            return

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        if guild.id != 411363271568785418:
            return
        channel = self.bot.get_channel(665147416688721921)
        await channel.send(f":warning: **{user.name} ({user.id}) was banned from {guild.name}.**")

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        if guild.id != 411363271568785418:
            return
        Warn = f":warning: **{user.name} ({user.id}) was unbanned from {guild.name}.**"
        deletembed = discord.Embed(title='Reason:', description='The ban was revoked.', color=16737380)
        await self.bot.get_guild(615881983310036992).get_channel(665147416688721921).send(content=(f"{Warn}"),
          embed=deletembed)

    @commands.Cog.listener()
    async def on_message_delete(self, deletthis):
        if deletthis.guild.id != 411363271568785418:
            return
        try:
            attachment = None
        except:
            pass

        Warn = f":warning: A message was deleted from **{deletthis.author.name}**#{deletthis.author.discriminator} ({deletthis.author.id}) in <#{deletthis.channel.id}>."
        deletembed = discord.Embed(title='Message Content:', description=f"{deletthis.content},\nAttachments: {attachment}", color=16737380)
        await self.bot.get_guild(615881983310036992).get_channel(651377196685852702).send(content=(f"{Warn}"),
          embed=deletembed)


def setup(bot):
    bot.add_cog(banandunban(bot))