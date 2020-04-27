# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\autobanyoutube.py
# Compiled at: 2020-01-31 15:06:37
# Size of source mod 2**32: 1598 bytes
import asyncio, json, discord
from discord.ext import commands
from discord.ext.commands import BucketType
from io import BytesIO
from utils import checks, autobanfilter
ytbanned_words = autobanfilter.bannedlinksyt

class autobanyoutube(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ban1):
        try:
            if ban1.author.guild_permissions.ban_members:
                return
                channel = self.bot.get_channel(665147416688721921)
                if 'youtube.com' in ban1.content.lower():
                    if any((word in ban1.content for word in ytbanned_words)):
                        await asyncio.sleep(0.3)
                        try:
                            await ban1.author.ban(reason='Posting a gremlin link. ~MidoriBot')
                            await channel.send('Banned that motherfucker! (Posted gremlin links)')
                        except:
                            return

                if 'youtu.be' in ban1.content.lower():
                    if any((word in ban1.content for word in ytbanned_words)):
                        await asyncio.sleep(0.3)
                        try:
                            await ban1.author.ban(reason='Posting a gremlin link. ~MidoriBot')
                            await channel.send('Banned that motherfucker! (Posted gremlin links)')
                        except:
                            return

            else:
                return
        except:
            return


def setup(bot):
    bot.add_cog(autobanyoutube(bot))