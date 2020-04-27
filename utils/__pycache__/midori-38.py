# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\utils\midori.py
# Compiled at: 2019-12-06 13:39:51
# Size of source mod 2**32: 630 bytes
from discord.ext.commands import AutoShardedBot
from utils import checks, default

class Midori(AutoShardedBot):

    def __init__(self, *args, prefix=None, **kwargs):
        (super().__init__)(*args, **kwargs)

    async def on_message(self, msg):
        if not (self.is_ready() and msg.author.bot or default.can_send(msg)):
            return
            if msg.command is None:
                return
            if msg.author.id in checks.user_blacklist:
                return
            if msg.guild is not None:
                if msg.guild.id in checks.guild_blacklist:
                    return
        await self.process_commands(msg)