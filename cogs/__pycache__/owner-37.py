# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\AkaneBot\cogs\owner.py
# Compiled at: 2020-04-14 04:37:01
# Size of source mod 2**32: 4548 bytes
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils import checks, default
import random, asyncio, importlib, subprocess, select

class other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(checks.is_joel)
    async def reload(self, ctx, name: str):
        """Reloads a extension."""
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except commands.ExtensionError as e:
            try:
                await ctx.send(f"```diff\n- {e}```")
            finally:
                e = None
                del e

        else:
            await ctx.send(f"Reloaded extension **{name}.py**")

    @commands.command()
    @commands.check(checks.is_joel)
    async def load(self, ctx, name: str):
        try:
            self.bot.load_extension(f"cogs.{name}")
        except commands.ExtensionError as e:
            try:
                await ctx.send(f"```diff\n- {e}```")
            finally:
                e = None
                del e

        else:
            await ctx.send(f"Loaded extension **{name}.py**")

    @commands.command()
    @commands.check(checks.is_joel)
    async def unload(self, ctx, name: str):
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except commands.ExtensionError as e:
            try:
                await ctx.send(f"```diff\n- {e}```")
            finally:
                e = None
                del e

        else:
            await ctx.send(f"Unloaded extension **{name}.py**")

    @commands.command()
    @commands.check(checks.is_joel)
    async def reloadutils(self, ctx, name: str):
        """ Reloads a utils module. """
        name_maker = f"utils/{name}.py"
        try:
            module_name = importlib.import_module(f"utils.{name}")
            importlib.reload(module_name)
        except ModuleNotFoundError:
            return await ctx.send(f"Couldn't find module named **{name_maker}**")
        except Exception as e:
            try:
                error = default.traceback_maker(e)
                return await ctx.send(f"Module **{name_maker}** returned error and was not reloaded...\n{error}")
            finally:
                e = None
                del e

        await ctx.send(f"Reloaded module **{name_maker}**")

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.owners)
    @commands.cooldown(1, 60, BucketType.user)
    async def ownerhelp(self, ctx):
        embed = discord.Embed(title='**Owner help menu!**', color=(random.randint(0, 16777215)))
        embed.add_field(name='Here are your owner commands!',
          value='null - No commands')
        embed.add_field(name='Fun hidden commands:',
          value='null - No commands.')
        embed.set_footer(text='Aoi Bot',
          icon_url=self.bot.user.avatar_url_as(format='png'))
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.check(checks.is_joel)
    async def servers(self, ctx):
        em = discord.Embed()
        for server in self.bot.guilds:
            em.add_field(name=f"**Name**: {server.name}\n                **ID**: {server.id}\n                **Members**: {len(server.members)}",
              value='-----')

        await ctx.send(embed=em)

    @commands.command()
    @commands.check(checks.is_joel)
    async def shutdown(self, ctx):
        await ctx.send('Fine.. Bye...')
        print('Shutdown called. The script will now close')
        exit()

    @commands.command()
    @commands.check(checks.is_joel)
    async def reboot(self, ctx):
        await ctx.send("Alright! I'll be right back!")
        exit()

    @commands.command()
    @commands.check(checks.allowed_ids)
    async def game(self, ctx, *, arg):
        try:
            channel = self.bot.get_channel(439017534709170187)
            await channel.trigger_typing()
            await asyncio.sleep(random.randint(3, 5))
            await channel.send(arg)
            await ctx.send('Successfully sent!')
        except:
            await ctx.send('error...')

    @commands.command()
    @commands.check(checks.allowed_ids)
    async def off(self, ctx, *, arg):
        try:
            channel = self.bot.get_channel(673513111185260554)
            await channel.trigger_typing()
            await asyncio.sleep(random.randint(3, 5))
            await channel.send(arg)
            await ctx.send('Successfully sent!')
        except:
            await ctx.send('error...')


def setup(bot):
    bot.add_cog(other(bot))