# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\cogs\owner.py
# Compiled at: 2019-12-06 10:56:10
# Size of source mod 2**32: 4176 bytes
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils import checks, default
import random, asyncio, importlib

class other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"cogs.{name}")
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```\n{e}```")
        else:
            await ctx.send(f"Reloaded extension **{name}.py**")

    @commands.command()
    async def reloadutils--- This code section failed: ---

 L.  27         0  LOAD_STR                 'utils/'
                2  LOAD_FAST                'name'
                4  FORMAT_VALUE          0  ''
                6  LOAD_STR                 '.py'
                8  BUILD_STRING_3        3  ''
               10  STORE_FAST               'name_maker'

 L.  28        12  SETUP_FINALLY        44  'to 44'

 L.  29        14  LOAD_GLOBAL              importlib
               16  LOAD_METHOD              import_module
               18  LOAD_STR                 'utils.'
               20  LOAD_FAST                'name'
               22  FORMAT_VALUE          0  ''
               24  BUILD_STRING_2        2  ''
               26  CALL_METHOD_1         1  ''
               28  STORE_FAST               'module_name'

 L.  30        30  LOAD_GLOBAL              importlib
               32  LOAD_METHOD              reload
               34  LOAD_FAST                'module_name'
               36  CALL_METHOD_1         1  ''
               38  POP_TOP          
               40  POP_BLOCK        
               42  JUMP_FORWARD        162  'to 162'
             44_0  COME_FROM_FINALLY    12  '12'

 L.  31        44  DUP_TOP          
               46  LOAD_GLOBAL              ModuleNotFoundError
               48  COMPARE_OP               exception-match
               50  POP_JUMP_IF_FALSE    86  'to 86'
               52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L.  32        58  LOAD_FAST                'ctx'
               60  LOAD_METHOD              send
               62  LOAD_STR                 "Couldn't find module named **"
               64  LOAD_FAST                'name_maker'
               66  FORMAT_VALUE          0  ''
               68  LOAD_STR                 '**'
               70  BUILD_STRING_3        3  ''
               72  CALL_METHOD_1         1  ''
               74  GET_AWAITABLE    
               76  LOAD_CONST               None
               78  YIELD_FROM       
               80  ROT_FOUR         
               82  POP_EXCEPT       
               84  RETURN_VALUE     
             86_0  COME_FROM            50  '50'

 L.  33        86  DUP_TOP          
               88  LOAD_GLOBAL              Exception
               90  COMPARE_OP               exception-match
               92  POP_JUMP_IF_FALSE   160  'to 160'
               94  POP_TOP          
               96  STORE_FAST               'e'
               98  POP_TOP          
              100  SETUP_FINALLY       148  'to 148'

 L.  34       102  LOAD_GLOBAL              default
              104  LOAD_METHOD              traceback_maker
              106  LOAD_FAST                'e'
              108  CALL_METHOD_1         1  ''
              110  STORE_FAST               'error'

 L.  35       112  LOAD_FAST                'ctx'
              114  LOAD_METHOD              send
              116  LOAD_STR                 'Module **'
              118  LOAD_FAST                'name_maker'
              120  FORMAT_VALUE          0  ''
              122  LOAD_STR                 '** returned error and was not reloaded...\n'
              124  LOAD_FAST                'error'
              126  FORMAT_VALUE          0  ''
              128  BUILD_STRING_4        4  ''
              130  CALL_METHOD_1         1  ''
              132  GET_AWAITABLE    
              134  LOAD_CONST               None
              136  YIELD_FROM       
              138  ROT_FOUR         
              140  POP_BLOCK        
              142  POP_EXCEPT       
              144  CALL_FINALLY        148  'to 148'
              146  RETURN_VALUE     
            148_0  COME_FROM           144  '144'
            148_1  COME_FROM_FINALLY   100  '100'
              148  LOAD_CONST               None
              150  STORE_FAST               'e'
              152  DELETE_FAST              'e'
              154  END_FINALLY      
              156  POP_EXCEPT       
              158  JUMP_FORWARD        162  'to 162'
            160_0  COME_FROM            92  '92'
              160  END_FINALLY      
            162_0  COME_FROM           158  '158'
            162_1  COME_FROM            42  '42'

 L.  36       162  LOAD_FAST                'ctx'
              164  LOAD_METHOD              send
              166  LOAD_STR                 'Reloaded module **'
              168  LOAD_FAST                'name_maker'
              170  FORMAT_VALUE          0  ''
              172  LOAD_STR                 '**'
              174  BUILD_STRING_3        3  ''
              176  CALL_METHOD_1         1  ''
              178  GET_AWAITABLE    
              180  LOAD_CONST               None
              182  YIELD_FROM       
              184  POP_TOP          

Parse error at or near `ROT_FOUR' instruction at offset 80

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.owners)
    @commands.cooldown(1, 60, BucketType.user)
    async def ownerhelp(self, ctx):
        embed = discord.Embed(title='**Owner help menu!**', color=(random.randint(0, 16777215)))
        embed.add_field(name='Here are your owner commands!',
          value="dm - DM any user of your choice with anything (YandereDev has access)\n            embed - Similar to `-say` except embedded with a random color (YandereDev has access)\n            ownertest - Test if I see you as my owner (works on other members)\n            say - Make me say stuff! (YandereDev has access)\n            servers - See all the servers I'm in\n            shutdown - Please don't turn me off! Keep me on!\n            spam - Enable/disable spam detection (currently disabled)")
        embed.add_field(name='Fun hidden commands:',
          value="fap - **FAP FAP FAP!**\n            hoard - Budo is hoarding all the children!\n            petadolfin - Pet our sweet Dolfy! <:HugMidori:586518197642067978>\n            petayano - Pet ayano with a flying hand down (YandereDev's request)\n            spritza - Fuck you, Spritza! <:YanPout:439730994162171914> (Not available)\n            spritzaegg - Drop an egg from Spritza's chicken (Not available)")
        embed.set_footer(text='Midori Bot',
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
    @commands.guild_only()
    @commands.check(checks.is_joel)
    async def play(self, ctx, *, arg: commands.clean_content=None):
        voicechannel = ctx.author.voice.channel
        vc = await voicechannel.connect()
        await ctx.send(f'Attempting to play "{arg}" :play_pause:')
        vc.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/bin/ffmpeg.exe', source=f"data/bot-songs/{arg}"))
        await asyncio.sleep(243)
        await vc.disconnect()

    @commands.command()
    @commands.check(checks.is_joel)
    async def shutdown(self, ctx):
        await ctx.send('<:YanSigh:585576476569501716> Oooookaaaaay��? Bye��?')
        print('Shutdown called. The script will now close')
        exit()


def setup(bot):
    bot.add_cog(other(bot))