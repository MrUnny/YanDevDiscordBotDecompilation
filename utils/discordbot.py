from discord.ext.commands import AutoShardedBot

from utils import checks, default


class DiscordBot(AutoShardedBot):
    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot or not default.can_send(msg):
            return

        if msg.author.id in checks.user_blacklist:
            return

        if msg.guild is not None and msg.guild.id in checks.guild_blacklist:
            return

        await self.process_commands(msg)
