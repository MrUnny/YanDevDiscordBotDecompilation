import os
import discord
import asyncio
from time import sleep
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import re
  
def limit_memory(maxsize): 
    soft, hard = resource.getrlimit(resource.RLIMIT_AS) 
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard)) 

from utils.discordbot import DiscordBot

description = """
Weeeeeeeeeeeeeeeeeeeeeeeb
"""
token = "TOKEN"

print("logging in...")
bot = DiscordBot(case_insensitive=True, description=description, command_prefix="!", help_command=None, max_messages=5000)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(token)