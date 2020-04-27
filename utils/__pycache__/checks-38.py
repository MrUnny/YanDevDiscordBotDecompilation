# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\utils\checks.py
# Compiled at: 2019-12-06 13:55:06
# Size of source mod 2**32: 6834 bytes
import discord
disallow_channels = [
 411363271568785420, 606549827077144589, 575234510682193930,
 602454748406480916, 508668937035186186, 438529996223545344,
 439016971749556234, 439017534709170187, 439019287370530817,
 439149789058433024, 439018413701201930]
twitch = [
 411363271568785420, 606549827077144589, 575234510682193930,
 602454748406480916, 508668937035186186]
user_blacklist = []
guild_blacklist = []
owners_ids = [
 396241937658675206, 135161245941628928, 150665783268212746]

def is_joel(ctx):
    return ctx.author.id == 396241937658675206


def is_soheab(ctx):
    return ctx.author.id == 150665783268212746


def manage_message_owner(ctx):
    if not ctx.author.guild_permissions.manage_messages:
        if ctx.author.id == 396241937658675206:
            return not ctx.author.guild_permissions.manage_messages and ctx.author.id == 396241937658675206


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
 discord.Activity(name='with Adolfin.exe', type=0),
 discord.Activity(name='a fighting game with YandereDev', type=0),
 discord.Activity(name='"Annoy YandereDev"', type=0),
 discord.Activity(name='"Blame the Delinquents"', type=0),
 discord.Activity(name='with the Gaming Club', type=0),
 discord.Activity(name="with YandereDev's sanity", type=0),
 discord.Activity(name='YandereDev.exe with Adolfin', type=0),
 discord.Activity(name='"Green Greens" from Kirby', type=2),
 discord.Activity(name='YandereDev ASMR at 3AM in bed', type=2),
 discord.Activity(name='YandereDev yell at me', type=2),
 discord.Activity(name="all of YandereDev's old videos", type=3),
 discord.Activity(name='a video about annoying YandereDev with dumb questions', type=3),
 discord.Activity(name='for the next update', type=3),
 discord.Activity(name='people use the -help command', type=3),
 discord.Activity(name='self-insert fan-fiction about YandereDev', type=3),
 discord.Activity(name='Spritza bully YandereDev (and taking notes)', type=3),
 discord.Activity(name="Spritza enjoy YandereDev's two bananas", type=3),
 discord.Activity(name='THAT DUDE.', type=3),
 discord.Activity(name='the development of Yandere Simulator', type=3),
 discord.Activity(name='Yan-chan coming towards me with a knife', type=3),
 discord.Activity(name='Yan-chan suspiciously run around the school', type=3),
 discord.Activity(name='YandereDev add more bushes', type=3),
 discord.Activity(name='YandereDev from outside his window', type=3),
 discord.Activity(name='YandereDev from the corner of his room', type=3),
 discord.Activity(name='YandereDev have a mental breakdown', type=3),
 discord.Activity(name='YandereDev ignore my emails', type=3),
 discord.Activity(name="Ayano's Lovesick Labyrinth", type=0),
 discord.Activity(name='Burning Love', type=0),
 discord.Activity(name='Crush Crush', type=0),
 discord.Activity(name='Go All Out', type=0),
 discord.Activity(name='Kuudere Simulator', type=0),
 discord.Activity(name='Kuudere Simulator 2', type=0),
 discord.Activity(name='Kuudere Simulator 3', type=0),
 discord.Activity(name='LoveSick: Yandere Simulator', type=0),
 discord.Activity(name='Magical Girl Pretty Miyuki', type=0),
 discord.Activity(name='Mandere Simulator', type=0),
 discord.Activity(name='Midori Forest', type=0),
 discord.Activity(name='Moonlit Warrior Selene', type=0),
 discord.Activity(name='Pretty Guardian Miyuki', type=0),
 discord.Activity(name='Senpai Fighter', type=0),
 discord.Activity(name='Super Yandere 64', type=0),
 discord.Activity(name='Yandere Clicker', type=0),
 discord.Activity(name='Yandere Simulator', type=0),
 discord.Activity(name='Yanderetale', type=0),
 discord.Activity(name='Yanvania: Senpai of the Night', type=0),
 discord.Activity(name='Epic Rap Battles of Akademi', type=2),
 discord.Activity(name='Michaela Laws', type=2),
 discord.Activity(name='mom0ki', type=2),
 discord.Activity(name='Yandere Simulator Christmas carols', type=2),
 discord.Activity(name='Yandere Simulator Soundtrack', type=2),
 discord.Activity(name='"Delinquent Theme" by Simon Amiot', type=2),
 discord.Activity(name='"My Senpai" by Endigo & Bijuu Mike', type=2),
 discord.Activity(name='"Notice Me Senpai" by iHasCupquake', type=2),
 discord.Activity(name='"Senpai Notice Me" by Random Encounters', type=2),
 discord.Activity(name='"Senpai Won\'t You Notice Me?" by Fandroid', type=2),
 discord.Activity(name='"Star-Crossed Lovers" by Andy Yoon & M.W.', type=2),
 discord.Activity(name='"The Blackest Balloon" by Denzel Curry', type=2),
 discord.Activity(name='"YandereDev YandereDev" by mom0ki', type=2),
 discord.Activity(name='Bijuu Mike', type=3),
 discord.Activity(name='Dank Midori', type=3),
 discord.Activity(name='Jay from the Kubz Scouts', type=3),
 discord.Activity(name='Juno', type=3),
 discord.Activity(name='LaurenzSide', type=3),
 discord.Activity(name='Razzbowski', type=3),
 discord.Activity(name='Veggie Gamer', type=3),
 discord.Activity(name='YandereDev', type=3),
 discord.Activity(name='YandereDevFan', type=3),
 discord.Activity(name='yanderesimulator.com for the next update!', type=3),
 discord.Activity(name='yanderedev.wordpress.com for those juicy updates!', type=3),
 discord.Activity(name='youtube.com/YandereDev', type=3),
 discord.Activity(name='The midori song', type=2),
 discord.Activity(name='and conspiring with Spritza how to bulli YanDev', type=3),
 discord.Activity(name="Day 1245 YandereDev hasn't replied to my emails", type=0),
 discord.Activity(name='Ayano walk suspiciously around the school', type=3),
 discord.Activity(name='the player slowly come towards me to murder me brutally', type=3),
 discord.Streaming(name='Sending YandereDev 500 more e-mails!', url='https://twitch.tv/YandereDev'),
 discord.Streaming(name='twitch.tv/YandereDev', url='https://twitch.tv/YandereDev')]