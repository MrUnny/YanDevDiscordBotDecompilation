# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\cogs\weeb.py
# Compiled at: 2019-12-06 13:43:24
# Size of source mod 2**32: 36780 bytes
import asyncio, random
from datetime import datetime
from io import BytesIO
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils import checks, responses, default

class weeb(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def fap(self, ctx):
        embed = discord.Embed(title='**FAP FAP FAP**', color=(random.randint(0, 16777215)))
        embed.set_image(url='https://media1.tenor.com/images/865a3386e667cee3bb95c43ed6e3724b/tenor.gif?itemid=13819761')
        embed.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    @commands.cooldown(3, 20, BucketType.user)
    async def normie(self, ctx, member: discord.Member=None):
        if member is None:
            if ctx.author.id in checks.owners:
                dt = datetime.today()
                seconds = dt.timestamp()
                await ctx.send(f"{ctx.author.name}, You're about -{int(round(seconds))}% normie!")
        else:
            num = random.randint(0, 100)
            if num == 69:
                return await ctx.send(f"{ctx.author.name}, You're about 69% normie! ( ͡° ͜ʖ ͡°)")
                return await ctx.send(f"{ctx.author.name}, You're about {num}% normie!")
            else:
                num = random.randint(0, 100)
                if num == 69:
                    return await ctx.send(f"{member.name} is about 69% normie! ( ͡° ͜ʖ ͡°)")
                elif member.id in checks.owners:
                    dt = datetime.today()
                    seconds = dt.timestamp()
                    await ctx.send(f"{member.name} is about -{int(round(seconds))}% normie!")
                else:
                    await ctx.send(f"{member.name} is about {num}% normie!")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    @commands.check(checks.disabled_channels)
    async def bust(self, ctx, member: discord.Member=None):
        return await ctx.send('until I have a better way to have this command, it will be disabled temporary. Sorry for any inconvenient.')

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def meme--- This code section failed: ---

 L.  72         0  LOAD_FAST                'ctx'
                2  LOAD_METHOD              send
                4  LOAD_STR                 'Please wait... Loading meme...'
                6  CALL_METHOD_1         1  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  STORE_FAST               'memedelete'

 L.  73        16  LOAD_FAST                'ctx'
               18  LOAD_ATTR                channel
               20  LOAD_METHOD              typing
               22  CALL_METHOD_0         0  ''
               24  BEFORE_ASYNC_WITH
               26  GET_AWAITABLE    
               28  LOAD_CONST               None
               30  YIELD_FROM       
               32  SETUP_ASYNC_WITH    172  'to 172'
               34  POP_TOP          

 L.  74        36  LOAD_GLOBAL              default
               38  LOAD_ATTR                get
               40  LOAD_STR                 'https://some-random-api.ml/meme'
               42  LOAD_STR                 'read'
               44  LOAD_CONST               ('res_method',)
               46  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               48  GET_AWAITABLE    
               50  LOAD_CONST               None
               52  YIELD_FROM       
               54  STORE_FAST               'req'

 L.  75        56  LOAD_FAST                'req'
               58  LOAD_CONST               None
               60  COMPARE_OP               is
               62  POP_JUMP_IF_FALSE    98  'to 98'

 L.  76        64  LOAD_FAST                'ctx'
               66  LOAD_METHOD              send
               68  LOAD_STR                 'The API died or something.......'
               70  CALL_METHOD_1         1  ''
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_BLOCK        
               80  ROT_TWO          
               82  BEGIN_FINALLY    
               84  WITH_CLEANUP_START
               86  GET_AWAITABLE    
               88  LOAD_CONST               None
               90  YIELD_FROM       
               92  WITH_CLEANUP_FINISH
               94  POP_FINALLY           0  ''
               96  RETURN_VALUE     
             98_0  COME_FROM            62  '62'

 L.  78        98  LOAD_GLOBAL              BytesIO
              100  LOAD_FAST                'req'
              102  LOAD_STR                 'image'
              104  BINARY_SUBSCR    
              106  CALL_FUNCTION_1       1  ''
              108  STORE_FAST               'bio'

 L.  79       110  LOAD_FAST                'bio'
              112  LOAD_METHOD              seek
              114  LOAD_CONST               0
              116  CALL_METHOD_1         1  ''
              118  POP_TOP          

 L.  80       120  LOAD_FAST                'ctx'
              122  LOAD_ATTR                send
              124  LOAD_FAST                'req'
              126  LOAD_STR                 'caption'
              128  BINARY_SUBSCR    
              130  LOAD_GLOBAL              discord
              132  LOAD_ATTR                File
              134  LOAD_FAST                'bio'
              136  LOAD_STR                 'meme.png'
              138  LOAD_CONST               ('filename',)
              140  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              142  LOAD_CONST               ('content', 'file')
              144  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              146  GET_AWAITABLE    
              148  LOAD_CONST               None
              150  YIELD_FROM       
              152  POP_TOP          

 L.  81       154  LOAD_FAST                'memedelete'
              156  LOAD_METHOD              delete
              158  CALL_METHOD_0         0  ''
              160  GET_AWAITABLE    
              162  LOAD_CONST               None
              164  YIELD_FROM       
              166  POP_TOP          
              168  POP_BLOCK        
              170  BEGIN_FINALLY    
            172_0  COME_FROM_ASYNC_WITH    32  '32'
              172  WITH_CLEANUP_START
              174  GET_AWAITABLE    
              176  LOAD_CONST               None
              178  YIELD_FROM       
              180  WITH_CLEANUP_FINISH
              182  END_FINALLY      

Parse error at or near `POP_BLOCK' instruction at offset 78

    @commands.command(name='8ball')
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    @commands.cooldown(3, 20, BucketType.user)
    async def _8ball(self, ctx, *, question=None):
        if question is None:
            return await ctx.send('Please ask a question `-8ball [question]` then I shall answer it!')
            rannum = random.randint(1, 3)
            if rannum == 1:
                hug = discord.Embed(title='**8-ball 🎱**', color=65280)
                hug.add_field(name=(f"{random.choice(responses.ball8yes)}"),
                  value=f"\n**Original question:**\n{question}")
                hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
        else:
            if rannum == 2:
                hug = discord.Embed(title='**8-ball 🎱**', color=16776960)
                hug.add_field(name=(f"{random.choice(responses.ball8maybe)}"),
                  value=f"\n**Original question:**\n{question}")
                hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            elif rannum == 3:
                hug = discord.Embed(title='**8-ball 🎱**', color=16711680)
                hug.add_field(name=(f"{random.choice(responses.ball8no)}"),
                  value=f"\n**Original question:**\n{question}")
                hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            try:
                await ctx.send(embed=hug)
            except Exception:
                await ctx.send('**Error!**\nMissing permission: `embed_links`!')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, BucketType.user)
    @commands.check(checks.disabled_channels)
    async def petadolfin(self, ctx):
        await ctx.send('<:comfydolfin:600814828344442895>            <:YanPet:619472223115280385>\n<:petadolfin:624760208081682462>            <:petadolfin:624760208081682462><:petadolfin:624760208081682462>')

    @commands.cooldown(1, 69, BucketType.user)
    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def spankadolfin(self, ctx):
        spank = discord.Embed(title=f"**{ctx.author.name}** has spanked adolfin!",
          color=(random.randint(0, 16777215)))
        spank.set_image(url='https://media.discordapp.net/attachments/411363271568785420/643048792114987017/Spank_5.gif')
        await ctx.send(embed=spank)

    @commands.cooldown(1, 30, BucketType.user)
    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def spritzaegg(self, ctx):
        message = await ctx.send(':rooster:\n\n\n\n\n\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster::egg:\n\n\n\n\n\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n      :egg:\n\n\n\n\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n      :egg:\n\n\n\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n\n      :egg:\n\n\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n\n\n      :egg:\n\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n\n\n\n      :cooking:\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n\n\n\n      :cooking:"."\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n\n\n\n      :cooking:".."\n======the=bench========')
        await asyncio.sleep(0.8)
        await message.edit(content=':rooster:\n\n\n\n\n      :cooking:"..."\n======the=bench========')
        await asyncio.sleep(1)
        await message.edit(content=':rooster:\n\n\n\n\n      :cooking:"Fuck you, spritza!"\n======the=bench========', delete_after=180.0)

    @commands.cooldown(1, 30, BucketType.user)
    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def petayano(self, ctx):
        message = await ctx.send('<:DevRage:592992433902583828>\n\n\n\n\n\n<:YanComfy:633122689216675859>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828><:YanPet:619472223115280385>\n\n\n\n\n\n<:YanComfy:633122689216675859>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n      <:YanPet:619472223115280385>\n\n\n\n\n<:YanComfy:633122689216675859>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n      <:YanPet:619472223115280385>\n\n\n\n<:YanComfy:633122689216675859>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n      <:YanPet:619472223115280385>\n\n\n<:YanComfy:633122689216675859>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n\n      <:YanPet:619472223115280385>\n\n<:YanComfy:633122689216675859>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n\n\n      <:YanPet:619472223115280385>\n<:YanGasp:633122689141440523>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n\n\n      <:YanPet:619472223115280385>"."\n<:YanGasp:633122689141440523>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n\n\n      <:YanPet:619472223115280385>".."\n<:YanGasp:633122689141440523>')
        await asyncio.sleep(0.8)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n\n\n      <:YanPet:619472223115280385>"..."\n<:YanGasp:633122689141440523>')
        await asyncio.sleep(1)
        await message.edit(content='<:DevRage:592992433902583828>\n\n\n\n\n      "*purr*"\n<:PetAyano:615874425778339840>',
          delete_after=180.0)

    @commands.cooldown(3, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def sanity(self, ctx, member: discord.Member=None):
        num = random.randint(0, 100)
        if member is None:
            if ctx.author.id == 396241937658675206:
                dt = datetime.today()
                seconds = dt.timestamp()
                await ctx.send(f"{ctx.author.name}, your sanity is currently -{int(round(seconds))}%.")
            elif ctx.author.id == 135161245941628928:
                message = await ctx.send(content=f"{ctx.author.name}, your sanity is currently jf98wnacqwa380f3j%.")
                await asyncio.sleep(0.5)
                await message.edit(content=f"{ctx.author.name}, your sanity is currently wohf093wncwf4398%.")
                await asyncio.sleep(0.5)
                await message.edit(content=f"{ctx.author.name}, your sanity is currently r3290acm93w8c0hv%.")
                await asyncio.sleep(0.5)
                await message.edit(content=f"{ctx.author.name}, your sanity is currently 120983ufjww9884rj%.")
                await asyncio.sleep(0.5)
                await message.edit(content=f"{ctx.author.name}, your sanity is currently `[ERROR]YandereSanity raised an invalid number`%.")
                await asyncio.sleep(3)
                await message.edit(content=f"{ctx.author.name}, your sanity is currently correcting...%.")
                await asyncio.sleep(2)
                dt = datetime.today()
                seconds = dt.timestamp()
                await message.edit(content=f"{ctx.author.name}, your sanity is currently -{int(round(seconds))}%.")
            else:
                if num == 69:
                    await ctx.send(f"{ctx.author.name}, your sanity is currently 69%. ( ͡° ͜ʖ ͡°)")
                    return
                await ctx.send(f"{ctx.author.name}, your sanity is currently {num}%.")
        elif member.id in (396241937658675206, 135161245941628928):
            dt = datetime.today()
            seconds = dt.timestamp()
            await ctx.send(f"{member.name}'s sanity is currently -{int(round(seconds))}%.")
        elif num == 69:
            await ctx.send(f"{member.name} 's sanity is currently 69%. ( ͡° ͜ʖ ͡°)")
        else:
            await ctx.send(f"{member.name} 's sanity is currently {num}%.")

    @commands.cooldown(1, 5, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def bestdoki(self, ctx, Dokiname=None):
        if Dokiname is None:
            await ctx.send('Enter a doki name after `-bestdoki [DokiName]`')
        elif 'natsuki' in Dokiname.lower():
            await ctx.send('No.')
        elif 'sayori' in Dokiname.lower():
            await ctx.send('No.')
        elif 'monika' in Dokiname.lower():
            await ctx.send('No.')
        elif 'yuri' in Dokiname.lower():
            await ctx.send('Yes, Yuri is best doki!')
        elif 'yanderedev' in Dokiname.lower():
            await ctx.send('If it is possible for YandereDev to be a doki, then the answer is yes!')
        elif 'adolfin' in Dokiname.lower():
            await ctx.send('Yes, Adolfin can be a doki-dolfin')
        else:
            await ctx.send('Non-existant doki or invalid argument, but no.')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def hug(self, ctx, member: discord.Member=None):
        """ Hug a user! """
        randomhug = [
         'https://weebs4life.ga/api/hug/', 'https://nekos.life/api/v2/img/hug']
        hg = await default.get(url=(random.choice(randomhug)), res_method='json')
        if member is None:
            hug = discord.Embed(title=f"*hugs **{ctx.author.name}***, <:HugMidori:586518197642067978>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        elif member is ctx.author:
            hug = discord.Embed(title=f"**{ctx.author.name}**, you hugged yourself, very lonely... <:HugMidori:586518197642067978>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(title=f"**{ctx.author.name}** hugged **{member.name}** <:HugMidori:586518197642067978>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`!')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def kiss(self, ctx, member: discord.Member=None):
        """ Kiss a user! """
        ks = await default.get('https://nekos.life/api/v2/img/kiss', res_method='json')
        if member is None:
            kiss = discord.Embed(title=f"ooo... oh **{ctx.author.name}**~ *smooch*~ <:YanSmooch:585576522371432461>",
              color=(random.randint(0, 16777215)))
            kiss.set_image(url=(ks['url']))
        elif member is ctx.author:
            kiss = discord.Embed(title=f"**{ctx.author.name}**, you managed to kiss yourself and broke physics! <:YanSmooch:585576522371432461>",
              color=(random.randint(0, 16777215)))
            kiss.set_image(url=(ks['url']))
        else:
            kiss = discord.Embed(title=f"**{ctx.author.name}** kissed **{member.name}**~ <:YanSmooch:585576522371432461>",
              color=(random.randint(0, 16777215)))
            kiss.set_image(url=(ks['url']))
        try:
            kiss.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=kiss)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`!')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def poke(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/poke', res_method='json')
        if member is None:
            hug = discord.Embed(title=f"*pokes **{ctx.author.name}*** <:annePoint:620574727689207808>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        elif member is ctx.author:
            hug = discord.Embed(title=f"**{ctx.author.name}**, you poked youself... but why? <:annePoint:620574727689207808>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(title=f"**{ctx.author.name}** poked **{member.name}**. <:annePoint:620574727689207808>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permission: `embed_links`!')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command(aliases=['pet'])
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def pat(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/pat', res_method='json')
        if member is None:
            hug = discord.Embed(title=f"*pats **{ctx.author.name}*** <:HugMidori:586518197642067978>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        elif member == ctx.author:
            hug = discord.Embed(title=f"**{ctx.author.name}**, you have pet yourself... are you just scratching your head? <:HugMidori:586518197642067978>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(title=f"**{ctx.author.name}** patted **{member.name}**! <:HugMidori:586518197642067978>",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permission: `embed_links`!')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def slap(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/slap', res_method='json')
        if member is None:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"*slaps **{ctx.author.name}***")
            hug.set_image(url=(hg['url']))
        elif member is ctx.author:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"**{ctx.author.name}**, you slapped yourself, ouch!")
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"**{ctx.author.name}** slapped **{member.name}**!")
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command(aliases=['cuddles'])
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def cuddle(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/cuddle', res_method='json')
        if member is None:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"*Cuddles and snuggles for **{ctx.author.name}***")
            hug.set_image(url=(hg['url']))
        elif member is ctx.author:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title='*Cuddles and snuggles for... yourself?*')
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"**{ctx.author.name}** has given cuddles and snuggles to **{member.name}**!")
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def feed(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/feed', res_method='json')
        if member is None:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"*feeds **{ctx.author.name}***")
            hug.set_image(url=(hg['url']))
        elif member is ctx.author:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title='*You have fed yourself*')
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(color=(random.randint(0, 16777215)), title=f"**{ctx.author.name}** has fed **{member.name}**!")
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command(aliases=['gecfdo'])
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def gecf(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/gecg', res_method='json')
        hug = discord.Embed(title=f"**{ctx.author.name}** here is a gecfdo!", color=(random.randint(0, 16777215)))
        hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def tickle(self, ctx, member: discord.Member=None):
        hg = await default.get('https://nekos.life/api/v2/img/tickle', res_method='json')
        if member is None:
            hug = discord.Embed(title=f"*tickles **{ctx.author.name}***", color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        elif member is ctx.author:
            hug = discord.Embed(title='*You have tickled... yourself?*', color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        else:
            hug = discord.Embed(title=f"**{ctx.author.name}** has tickled **{member.name}**!", color=(random.randint(0, 16777215)))
            hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.has_role('Twitch Subscriber')
    @commands.command()
    @commands.guild_only()
    async def spank--- This code section failed: ---

 L. 494         0  LOAD_CONST               493745285714149390
                2  BUILD_LIST_1          1 
                4  STORE_FAST               'tms'

 L. 495         6  LOAD_FAST                'ctx'
                8  LOAD_ATTR                channel
               10  LOAD_ATTR                id
               12  LOAD_FAST                'tms'
               14  COMPARE_OP               not-in
               16  POP_JUMP_IF_FALSE    56  'to 56'

 L. 496        18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                author
               22  LOAD_ATTR                id
               24  LOAD_CONST               (396241937658675206, 135161245941628928)
               26  COMPARE_OP               in
               28  POP_JUMP_IF_FALSE    32  'to 32'

 L. 497        30  JUMP_FORWARD        326  'to 326'
             32_0  COME_FROM            28  '28'

 L. 499        32  LOAD_FAST                'ctx'
               34  LOAD_ATTR                send
               36  LOAD_STR                 'Sorry, this command cannot be used here.'
               38  LOAD_CONST               10
               40  LOAD_CONST               ('delete_after',)
               42  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               44  GET_AWAITABLE    
               46  LOAD_CONST               None
               48  YIELD_FROM       
               50  RETURN_VALUE     
            52_54  JUMP_FORWARD        326  'to 326'
             56_0  COME_FROM            16  '16'

 L. 502        56  LOAD_FAST                'member'
               58  LOAD_CONST               None
               60  COMPARE_OP               is
               62  POP_JUMP_IF_FALSE   120  'to 120'

 L. 503        64  LOAD_GLOBAL              discord
               66  LOAD_ATTR                Embed
               68  LOAD_STR                 '*spanks **'
               70  LOAD_FAST                'ctx'
               72  LOAD_ATTR                author
               74  LOAD_ATTR                name
               76  FORMAT_VALUE          0  ''
               78  LOAD_STR                 '***'
               80  BUILD_STRING_3        3  ''
               82  LOAD_GLOBAL              random
               84  LOAD_METHOD              randint
               86  LOAD_CONST               0
               88  LOAD_CONST               16777215
               90  CALL_METHOD_2         2  ''
               92  LOAD_CONST               ('title', 'color')
               94  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               96  STORE_FAST               'hug'

 L. 504        98  LOAD_FAST                'hug'
              100  LOAD_ATTR                set_image
              102  LOAD_GLOBAL              random
              104  LOAD_METHOD              choice
              106  LOAD_GLOBAL              responses
              108  LOAD_ATTR                spankimg
              110  CALL_METHOD_1         1  ''
              112  LOAD_CONST               ('url',)
              114  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              116  POP_TOP          
              118  JUMP_FORWARD        236  'to 236'
            120_0  COME_FROM            62  '62'

 L. 505       120  LOAD_FAST                'member'
              122  LOAD_FAST                'ctx'
              124  LOAD_ATTR                author
              126  COMPARE_OP               is
              128  POP_JUMP_IF_FALSE   174  'to 174'

 L. 506       130  LOAD_GLOBAL              discord
              132  LOAD_ATTR                Embed
              134  LOAD_STR                 '*You spanked yourself*'
              136  LOAD_GLOBAL              random
              138  LOAD_METHOD              randint
              140  LOAD_CONST               0
              142  LOAD_CONST               16777215
              144  CALL_METHOD_2         2  ''
              146  LOAD_CONST               ('title', 'color')
              148  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              150  STORE_FAST               'hug'

 L. 507       152  LOAD_FAST                'hug'
              154  LOAD_ATTR                set_image
              156  LOAD_GLOBAL              random
              158  LOAD_METHOD              choice
              160  LOAD_GLOBAL              responses
              162  LOAD_ATTR                spankimg
              164  CALL_METHOD_1         1  ''
              166  LOAD_CONST               ('url',)
              168  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              170  POP_TOP          
              172  JUMP_FORWARD        236  'to 236'
            174_0  COME_FROM           128  '128'

 L. 509       174  LOAD_GLOBAL              discord
              176  LOAD_ATTR                Embed
              178  LOAD_STR                 '**'
              180  LOAD_FAST                'ctx'
              182  LOAD_ATTR                author
              184  LOAD_ATTR                name
              186  FORMAT_VALUE          0  ''
              188  LOAD_STR                 '** has spanked **'
              190  LOAD_FAST                'member'
              192  LOAD_ATTR                name
              194  FORMAT_VALUE          0  ''
              196  LOAD_STR                 '**!'
              198  BUILD_STRING_5        5  ''

 L. 510       200  LOAD_GLOBAL              random
              202  LOAD_METHOD              randint
              204  LOAD_CONST               0
              206  LOAD_CONST               16777215
              208  CALL_METHOD_2         2  ''

 L. 509       210  LOAD_CONST               ('title', 'color')
              212  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              214  STORE_FAST               'hug'

 L. 511       216  LOAD_FAST                'hug'
              218  LOAD_ATTR                set_image
              220  LOAD_GLOBAL              random
              222  LOAD_METHOD              choice
              224  LOAD_GLOBAL              responses
              226  LOAD_ATTR                spankimg
              228  CALL_METHOD_1         1  ''
              230  LOAD_CONST               ('url',)
              232  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              234  POP_TOP          
            236_0  COME_FROM           172  '172'
            236_1  COME_FROM           118  '118'

 L. 512       236  SETUP_FINALLY       286  'to 286'

 L. 513       238  LOAD_FAST                'hug'
              240  LOAD_ATTR                set_footer
              242  LOAD_STR                 'Midori Bot'
              244  LOAD_FAST                'self'
              246  LOAD_ATTR                bot
              248  LOAD_ATTR                user
              250  LOAD_ATTR                avatar_url_as
              252  LOAD_STR                 'png'
              254  LOAD_CONST               ('format',)
              256  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              258  LOAD_CONST               ('text', 'icon_url')
              260  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              262  POP_TOP          

 L. 514       264  LOAD_FAST                'ctx'
              266  LOAD_ATTR                send
              268  LOAD_FAST                'hug'
              270  LOAD_CONST               ('embed',)
              272  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              274  GET_AWAITABLE    
              276  LOAD_CONST               None
              278  YIELD_FROM       
              280  POP_TOP          
              282  POP_BLOCK        
              284  JUMP_FORWARD        326  'to 326'
            286_0  COME_FROM_FINALLY   236  '236'

 L. 515       286  DUP_TOP          
              288  LOAD_GLOBAL              discord
              290  LOAD_ATTR                Forbidden
              292  COMPARE_OP               exception-match
          294_296  POP_JUMP_IF_FALSE   324  'to 324'
              298  POP_TOP          
              300  POP_TOP          
            302_0  COME_FROM            30  '30'
              302  POP_TOP          

 L. 516       304  LOAD_FAST                'ctx'
              306  LOAD_METHOD              send
              308  LOAD_STR                 '**Error!**\nMissing permissions `embed_links`'
              310  CALL_METHOD_1         1  ''
              312  GET_AWAITABLE    
              314  LOAD_CONST               None
              316  YIELD_FROM       
              318  POP_TOP          
              320  POP_EXCEPT       
              322  JUMP_FORWARD        326  'to 326'
            324_0  COME_FROM           294  '294'
              324  END_FINALLY      
            326_0  COME_FROM           322  '322'
            326_1  COME_FROM           284  '284'
            326_2  COME_FROM            52  '52'

Parse error at or near `COME_FROM' instruction at offset 302_0

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def neko(self, ctx):
        hg = await default.get('https://nekos.life/api/v2/img/neko', res_method='json')
        hug = discord.Embed(title=f"Purr~ *rubs against **{ctx.author.name}**'s leg* Nya~ <:YanCat:437357869201883138>",
          color=(random.randint(0, 16777215)))
        hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permission: `embed_links`!')

    @commands.cooldown(1, 20, BucketType.user)
    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    async def baka(self, ctx):
        hg = await default.get('https://nekos.life/api/v2/img/baka', res_method='json')
        hug = discord.Embed(title=f"**{ctx.author.name}! Y–YOU BAKA!**", color=(random.randint(0, 16777215)))
        hug.set_image(url=(hg['url']))
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permission: `embed_links`!')

    @commands.cooldown(5, 20, BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def why(self, ctx):
        why = await default.get('https://nekos.life/api/v2/why', res_method='json')
        await ctx.send(why['why'])

    @commands.command()
    @commands.guild_only()
    async def hoard(self, ctx):
        await ctx.send(f"Budokas has hoarded {len(bot.users)} characters as his children")

    @commands.cooldown(3, 15, BucketType.user)
    @commands.command(aliases=['w'])
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def waifu(ctx, Waifuname=None, *, arg=None):
        if Waifuname is None:
            hug = discord.Embed(color=(random.randint(0, 16777215)))
            hug.add_field(name='**Arguments for "-waifu":**',
              value='- Samus\n- Neptune\n- Morrigan\n- IO\n- Cammy\n- Megumin\n- Zero Two\n- Komi san\n- Satou\n- Miku Hatsune\n- Yuri (DDLC)\n- Pichu girl\nMore waifus will be added soon.\nTo see the list of upcoming waifus, use `-waifu queue`!')
            hug.add_field(name='Note to original artists/photographers:',
              value='I do not claim ownership of these images. If you own any of these pictures and wish to take them down or make modifications, please contact the owner of the bot using the `-help` or `-waifu suggest` command.')
        elif 'samus' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Samus!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.samusimg)))
        elif 'nep' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Neptunia!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.neptuneimg)))
        elif 'morrigan' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Morrigan!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.morriganimg)))
        elif 'io' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is an Io, from <:Co:624763665505058821><:de:624763666507759626><:Ve:624763665169514547><:in:624763667770245120>!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.iocodeveinimg)))
        elif 'cammy' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Cammy!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.cammyimg)))
        elif 'megu' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Megumin!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.meguimg)))
        elif 'zero' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Zero Two!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.zerotwoimg)))
        elif 'komi' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Komi-san!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.komisanimg)))
        elif 'celestia' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, Here is a Celestia Ludenberg!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.celestiaimg)))
        elif 'satou' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Satou Matsuzaka!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.satouimg)))
        elif 'miku' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Miku Hatsune!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.mikuimg)))
        elif 'yuri' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Yuri from Doki Doki Literature Club!",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.yuriimg)))
        elif 'pichu' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Pichu girl! *(LIMITED IMAGES)*",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.pichuimg)))
        elif 'cirno' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, here is a Cirno Fairy! *(LIMITED IMAGES)*",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.cirnoimg)))
        elif 'dev' in Waifuname.lower():
            hug = discord.Embed(title=f"**{ctx.author.name}**, Here is a YandereDev! *(LIMITED IMAGES, suggested by Adolfin)*",
              color=(random.randint(0, 16777215)))
            hug.set_image(url=(random.choice(responses.devimg)))
        elif 'queue' in Waifuname.lower():
            hug = discord.Embed(name='**Here is the list:**',
              color=(random.randint(0, 16777215)))
            hug.add_field(name='**Here is the list:**', value=('**Currently working on:** Kotoko utsugi\n' + '\n'.join(responses.waifuqueue)))
            hug.add_field(name='**Help wanted:**',
              value="If you have an entire collection of images, or even a few, every image helps towards this command, if you would like to help, please use `-waifu suggest [message]`, Example: ```-waifu suggest I have 169 images of 2B you can use!``` and I will get hold of you, you *don't* have to put your username in, my bot tells me who sends what. Usually I keep my DMs disabld due to DM advertisements <:YanDerp:591048226719924294>")
        elif 'suggest' in Waifuname.lower():
            if arg is None:
                await ctx.send('You have to type your waifu suggestion after `-waifu suggest [waifu name]`.')
            else:
                try:
                    channel = bot.get_channel(636078349814595585)
                    await channel.send(f"Waifu suggestion by {ctx.author.name}: {arg}")
                    await ctx.send('OK! Waifu name sent!\n                        Please wait for approval before being added to the queue.')
                except Exception:
                    await ctx.send("Sorry. I couldn't send your waifu suggestion. I'm not sure why it isn't working��?")

        else:
            hug = discord.Embed(color=(random.randint(0, 16777215)))
            hug.add_field(name='**Arguments for "-waifu":**',
              value=f"""Unfortunately, "{Waifuname}" isn\'t recognised or not found. here are the valid waifus:\n- Samus\n- Neptune\n- Morrigan\n- Io\n- Cammy\n- Megumin\n- Zero Two\n- Komi san\n- Satou\n- Miku Hatsune\n- Yuri (DDLC)\n- Pichu Girl\nMore waifus will be added soon.\n                      To see the list of upcoming waifus, use `-waifu queue`!""")
            hug.add_field(name='Note:',
              value='Try using the `-waifu suggest` command followed by a waifu name. Then the developer of this bot will try doing something.')
            hug.add_field(name='Note to original artists/photographers:',
              value='I do not claim ownership of these images. If you own any of these pictures and wish to take them down or make modifications, please contact the owner of the bot using the `-help` or `-waifu suggest` command.')
        try:
            hug.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=hug)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permission: `embed_links`!')


def setup(bot):
    bot.add_cog(weeb(bot))