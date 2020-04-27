# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot - Copy\utils\checks.py
# Compiled at: 2020-04-13 19:23:43
# Size of source mod 2**32: 1954 bytes
import discord
disallow_channels = [
 411363271568785420, 606549827077144589, 575234510682193930,
 602454748406480916, 508668937035186186, 438529996223545344,
 439016971749556234, 439017534709170187, 439019287370530817,
 439149789058433024, 653906879357124609]
twitch = [
 411363271568785420, 606549827077144589, 575234510682193930,
 602454748406480916, 508668937035186186]
user_blacklist = []
guild_blacklist = []
owners_ids = [
 396241937658675206, 135161245941628928]

def is_joel(ctx):
    return ctx.author.id == 396241937658675206


def manage_message_owner(ctx):
    if not ctx.author.guild_permissions.manage_messages or ctx.author.id == 396241937658675206:
        return ctx.author.guild_permissions.manage_messages or 


def allowed_ids(ctx):
    return ctx.author.id in (199004056310513674, 396241937658675206, 104632038425903104,
                             135161245941628928)


async def owners(ctx):
    if ctx.author.id in owners_ids:
        return ctx.author.id in owners_ids
    await ctx.send(f"Sorry, {ctx.author.name}. You're not allowed to use that command.")
    return


def _owners(ctx):
    return ctx.author.id in owners_ids


async def disabled_channels(ctx):
    if ctx.channel.id not in disallow_channels:
        return ctx.channel.id not in disallow_channels
    await ctx.send('Sorry, this command cannot be used here.', delete_after=10)
    return


status_list = [
 discord.Activity(name='myself being pretty around the school', type=3),
 discord.Activity(name='Ayano act suspicously', type=3),
 discord.Streaming(name='twitch.tv/YandereDev', url='https://twitch.tv/YandereDev')]