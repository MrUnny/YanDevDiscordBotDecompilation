# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\joelt\Desktop\midori-bot\cogs\blacklist.py
# Compiled at: 2020-01-19 15:25:30
# Size of source mod 2**32: 1511 bytes
import asyncio, json, discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils import checks

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + fileName + '.json'
    with open(filePathNameWExt, 'w') as (fp):
        json.dump(data, fp)


def readTheJSONFile(path, filename, data):
    filePathNameWExt = './' + path + fileName + '.json'
    with open(filePathNameWExt, 'r') as (fp):
        JSONList = json.load(fp)


path = './'
fileName = 'blacklist'
data = {}

class blacklist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(checks.is_joel)
    async def blacklist(self, ctx, member: discord.Member=None):
        try:
            blacklistuser = member.id
            data['users'] = ['users', blacklistuser]
            writeToJSONFile(path, fileName, data)
            await ctx.send('File writing successful, now you need to add a function for me to read it!')
        except:
            await ctx.send('File writing failed.')


def setup(bot):
    bot.add_cog(blacklist(bot))