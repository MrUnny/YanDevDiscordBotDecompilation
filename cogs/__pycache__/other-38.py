# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\cogs\other.py
# Compiled at: 2019-12-06 11:01:16
# Size of source mod 2**32: 30566 bytes
import asyncio, random, time, discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils import checks

class other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    @commands.check(checks.disabled_channels)
    async def dischan(self, ctx):
        await ctx.send('yep this disabled channels check works.')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    @commands.check(checks._owners)
    async def yanjoel(self, ctx):
        await ctx.send('yep this owners check for yandere and joel that returns nothing works.')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    @commands.check(checks.owners)
    async def yanjoel2(self, ctx):
        await ctx.send('yep this owners check for yandere and joel that returns something works.')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    @commands.check(checks.is_joel)
    async def joel(self, ctx):
        await ctx.send('yep this joel check for only joel works.')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    @commands.check(checks.disabled_channels)
    async def help(self, ctx):
        HelpDM = await ctx.send('Sending...')
        embed = discord.Embed(title='**Help menu!\nMy available commands!**',
          description='approve - Approve a bug (only usable in bug approval channel, currently disabled)\n            baka - B–Baka! <:OsaPout:585710064661299220>\n            bug - YandereDev, YandereDev! I found a bug!\n            deny <Bug ID> - Deny a bug (only usable in bug approval channel, currently disabled)\n            help <Bug ID> - Show this help message\n            hug [@user] - Hug someone, or get a hug from me! <:HugMidori:586518197642067978>\n            neko - Get a neko, nya~!\n            kiss [@user] - Kiss anyone you want~ or do I have to kiss you? <:YanSmooch:585576522371432461>\n            normie [@user] - Find out how much of a filthy normie someone is\n            pat [@user] - Pet someone, or get petted by me (-pet is an alias)\n            ping - Ping me!\n            poke [@user] - Poke someone, or get poked\n            report [Report] - Report a bug about the game\n            sanity [@user] - Let me judge how sane you are\n            slap [@user] - Slap someone��? or get slapped!\n            suggest [Suggestion] - Suggest a command or feature (for me, not for the game) [CURRENTLY DISABLED!]\n            waifu [Waifu name] - Get a waifu (requested by YandereDev, -w is an alias, 15-second cooldown)!\n            cuddle [@user] -  Huggles and cuddles for that person or for you <:HugMidori:586518197642067978>\n            8ball [Question] - Ask the magic 8ball a question!\n            tickle [@user] - Tickle anyone, or I will tickle you!\n            feed [@user] - Feed a user, or I can feed you~\n            **NOTE: Most commands take about 20 seconds to cool down!**')
        if ctx.author.guild_permissions.manage_messages:
            embed.add_field(name='Moderator commands:',
              value="purge [NUMBER] - Purge the chat (Requires ability to delete messages)\n                nickname [name] (Leave blank to remove) - Rename the bot the easier way (Alias is -nick)\n                announcetwitch - Announce dev's twitch ONLY if mee6 isn't working.\n                warn <@user> <reason> - Warn a user, the logs get located to a logs channel\n                kick <@user> [reason] - Kick a user, Experimental.\n                ban <@user> [reason] - Ban a user, Experimental.\n                These commands are only visible to server moderators.")
        embed.add_field(name='Credits:',
          value='<@396241937658675206> *(Bot owner/main coder)*\n            onceler#2919 *(Assisting with getting statuses and a few other things to work)*\n            iSoheabM#5757 *(Assisting with commands)*\n            <@482943210637754378> *(Helping me get Samus images for the -waifu command)*\n            HarutoHiroki#4000 *(Helping me get Miku, Megumin, and Zero Two images for the -waifu command)*\n            <@523579776749928449> *(Hosting me on a fast, stable server)*\n            <@104632038425903104> *(Proofreading and other writing)*\n            <@135161245941628928> *(Being the best game developer ever and giving me his approval)*\n            <@533473096028389406> *(Giving me a few Yuri (DDLC) waifu pics)*\n            <@197926334180229121> *(Giving me some spank gifs)*\n            [Click here](https://www.youtube.com/watch?v=dQw4w9WgXcQ) for more information!')
        embed.add_field(name='Donations!',
          value='I am not asking for donations at all, but any coin is appreciated,             Non of this will go towards my own needs, this will go to the person that hosts my bot.\n            There is no link available right now, so hold all your coins for yourself! <:YanDerp:591048226719924294>')
        embed.set_footer(text='Midori Bot',
          icon_url=self.bot.user.avatar_url_as(format='png'))
        try:
            await ctx.author.send(embed=embed)
            await HelpDM.edit(content='Sent! Check your DMs!')
        except Exception:
            await HelpDM.edit(content="Hmm. I can't send you a DM. Try checking your settings to make sure DMs are open, and make sure you didn't block me!")

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    @commands.cooldown(1, 30, BucketType.user)
    async def suggest(self, ctx):
        await ctx.send('This command is temporarily disabled, Please try again later! <:YanM:443513610287972373>')

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    @commands.cooldown(1, 30, BucketType.user)
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        message = await ctx.send('Pinging��?')
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong! <:YanM:447212658261753876> `{int(ping)}ms`")
        print(f"Ping��? {int(ping)}ms")

    @commands.command()
    @commands.guild_only()
    @commands.check(checks._owners)
    @commands.cooldown(1, 30, BucketType.user)
    async def poll(self, ctx, *, question):
        embed = discord.Embed(title='**Poll**', description=f"{question}\n            👍 Yes\n            👎 No\n            🤷 I don't know/I don't care'",
          color=(random.randint(0, 16777215)))
        message = await ctx.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')

    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def ownertest(self, ctx):
        if ctx.author.id == 396241937658675206:
            await ctx.send("Hey, Joel! You're definitely my owner.")
        elif ctx.author.id == 135161245941628928:
            await ctx.send("Thanks for creating me, YandereDev! You're the best developer ever! <:YanMidori:421036544854589450> But you're not my owner.")
        elif ctx.author.id == 104632038425903104:
            await ctx.send("No, Rocky. You're not my owner.")
        else:
            await ctx.send("You're not my owner! <:YanPout:439730994162171914>")

    @commands.command()
    @commands.check(checks.disabled_channels)
    @commands.guild_only()
    async def report--- This code section failed: ---

 L. 173         0  LOAD_FAST                'self'
                2  LOAD_ATTR                bot
                4  LOAD_METHOD              get_channel
                6  LOAD_CONST               652209659092008983
                8  CALL_METHOD_1         1  ''
               10  STORE_FAST               'channel'

 L. 174        12  LOAD_FAST                'arg'
               14  LOAD_CONST               None
               16  COMPARE_OP               is
               18  POP_JUMP_IF_FALSE   176  'to 176'

 L. 175        20  SETUP_FINALLY       136  'to 136'

 L. 176        22  LOAD_GLOBAL              discord
               24  LOAD_ATTR                Embed

 L. 177        26  LOAD_STR                 '**🐞 How to Report a Bug (by Midori Gurinu) 🐞**'

 L. 178        28  LOAD_GLOBAL              random
               30  LOAD_METHOD              randint
               32  LOAD_CONST               0
               34  LOAD_CONST               16777215
               36  CALL_METHOD_2         2  ''

 L. 176        38  LOAD_CONST               ('title', 'color')
               40  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               42  STORE_FAST               'embed'

 L. 179        44  LOAD_FAST                'embed'
               46  LOAD_ATTR                add_field

 L. 180        48  LOAD_STR                 'A guide on reporting bugs:'

 L. 181        50  LOAD_STR                 "Please provide steps on how to trigger the bug,\nand the bug must follow these specific criteria:\n- The game must not be modded.\n- There must be no Easter eggs being used (unless they are broken, such as rendering errors, failing to summon demons, etc.).\n- There must be no debug commands being used.\n- The bug has to be reproducable.\n- The bug must not be a launcher bug.\n- The bug must not be a game crash (unless it can be reproduced by normal gameplay).Please ask <#439017534709170187> for assistance.\n\nIf you can report the bug correctly, then please use the following steps:\nAdd a title to the message. Then you must hit the next line. (For PC, you must hit Shift+Enter. For mobile, just hit return.)\nThen write the steps required to reproduce the bug like this:\nStep 1: First, do this.\nStep 2: Then, do this.\nStep 3: Finally, this is what happens.\n(It doesn't matter how many steps there are.)\n\nSound easy? Good! If you want to post a video or photo, just attach it as a link below the steps."

 L. 179        52  LOAD_CONST               ('name', 'value')
               54  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               56  POP_TOP          

 L. 199        58  LOAD_FAST                'embed'
               60  LOAD_ATTR                set_image

 L. 200        62  LOAD_STR                 'https://cdn.discordapp.com/attachments/615142254910111755/615144039267958794/unknown.png'

 L. 199        64  LOAD_CONST               ('url',)
               66  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               68  POP_TOP          

 L. 201        70  LOAD_FAST                'embed'
               72  LOAD_ATTR                set_footer

 L. 202        74  LOAD_STR                 'Midori Bot'

 L. 203        76  LOAD_FAST                'self'
               78  LOAD_ATTR                bot
               80  LOAD_ATTR                user
               82  LOAD_ATTR                avatar_url_as
               84  LOAD_STR                 'png'
               86  LOAD_CONST               ('format',)
               88  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'

 L. 201        90  LOAD_CONST               ('text', 'icon_url')
               92  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               94  POP_TOP          

 L. 205        96  LOAD_FAST                'ctx'
               98  LOAD_ATTR                author
              100  LOAD_ATTR                send
              102  LOAD_FAST                'embed'
              104  LOAD_CONST               ('embed',)
              106  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              108  GET_AWAITABLE    
              110  LOAD_CONST               None
              112  YIELD_FROM       
              114  POP_TOP          

 L. 206       116  LOAD_FAST                'ctx'
              118  LOAD_METHOD              send
              120  LOAD_STR                 'Check your DMs!'
              122  CALL_METHOD_1         1  ''
              124  GET_AWAITABLE    
              126  LOAD_CONST               None
              128  YIELD_FROM       
              130  POP_TOP          
              132  POP_BLOCK        
              134  JUMP_FORWARD        786  'to 786'
            136_0  COME_FROM_FINALLY    20  '20'

 L. 207       136  DUP_TOP          
              138  LOAD_GLOBAL              Exception
              140  COMPARE_OP               exception-match
              142  POP_JUMP_IF_FALSE   170  'to 170'
              144  POP_TOP          
              146  POP_TOP          
              148  POP_TOP          

 L. 208       150  LOAD_FAST                'ctx'
              152  LOAD_METHOD              send
              154  LOAD_STR                 'Your DMs seem to be disabled��? <a:YanQuiver:573635106397224961>\nPlease enable them and try the command again.'
              156  CALL_METHOD_1         1  ''
              158  GET_AWAITABLE    
              160  LOAD_CONST               None
              162  YIELD_FROM       
              164  POP_TOP          
              166  POP_EXCEPT       
              168  JUMP_FORWARD        786  'to 786'
            170_0  COME_FROM           142  '142'
              170  END_FINALLY      
          172_174  JUMP_FORWARD        786  'to 786'
            176_0  COME_FROM            18  '18'

 L. 211       176  LOAD_STR                 'launcher'
              178  LOAD_FAST                'arg'
              180  LOAD_METHOD              lower
              182  CALL_METHOD_0         0  ''
              184  COMPARE_OP               in
          186_188  POP_JUMP_IF_FALSE   296  'to 296'

 L. 212       190  SETUP_FINALLY       242  'to 242'

 L. 213       192  LOAD_FAST                'ctx'
              194  LOAD_ATTR                author
              196  LOAD_METHOD              send
              198  LOAD_STR                 'The current launcher has several problems and is currently being re-designed. Until a better launcher is available, please use one of the download links on this page instead: https://yanderedev.wordpress.com/downloads/'
              200  CALL_METHOD_1         1  ''
              202  GET_AWAITABLE    
              204  LOAD_CONST               None
              206  YIELD_FROM       
              208  POP_TOP          

 L. 216       210  LOAD_FAST                'ctx'
              212  LOAD_METHOD              send
              214  LOAD_STR                 "That's not a valid bug report, "
              216  LOAD_FAST                'ctx'
              218  LOAD_ATTR                author
              220  LOAD_ATTR                name
              222  FORMAT_VALUE          0  ''
              224  LOAD_STR                 '. Please check your DMs.'
              226  BUILD_STRING_3        3  ''
              228  CALL_METHOD_1         1  ''
              230  GET_AWAITABLE    
              232  LOAD_CONST               None
              234  YIELD_FROM       
              236  POP_TOP          
              238  POP_BLOCK        
              240  JUMP_FORWARD        786  'to 786'
            242_0  COME_FROM_FINALLY   190  '190'

 L. 217       242  DUP_TOP          
              244  LOAD_GLOBAL              Exception
              246  COMPARE_OP               exception-match
          248_250  POP_JUMP_IF_FALSE   290  'to 290'
              252  POP_TOP          
              254  POP_TOP          
              256  POP_TOP          

 L. 218       258  LOAD_FAST                'ctx'
              260  LOAD_METHOD              send
              262  LOAD_STR                 "That's not a valid bug report, "
              264  LOAD_FAST                'ctx'
              266  LOAD_ATTR                author
              268  LOAD_ATTR                name
              270  FORMAT_VALUE          0  ''
              272  LOAD_STR                 '. The launcher is being redesigned.'
              274  BUILD_STRING_3        3  ''
              276  CALL_METHOD_1         1  ''
              278  GET_AWAITABLE    
              280  LOAD_CONST               None
              282  YIELD_FROM       
              284  POP_TOP          
              286  POP_EXCEPT       
              288  JUMP_FORWARD        786  'to 786'
            290_0  COME_FROM           248  '248'
              290  END_FINALLY      
          292_294  JUMP_FORWARD        786  'to 786'
            296_0  COME_FROM           186  '186'

 L. 219       296  LOAD_STR                 'download'
              298  LOAD_FAST                'arg'
              300  LOAD_METHOD              lower
              302  CALL_METHOD_0         0  ''
              304  COMPARE_OP               in
          306_308  POP_JUMP_IF_FALSE   416  'to 416'

 L. 220       310  SETUP_FINALLY       362  'to 362'

 L. 221       312  LOAD_FAST                'ctx'
              314  LOAD_ATTR                author
              316  LOAD_METHOD              send
              318  LOAD_STR                 'The current launcher has several problems and is currently being re-designed. Until a better launcher is available, please use one of the download links on this page instead: https://yanderedev.wordpress.com/downloads/'
              320  CALL_METHOD_1         1  ''
              322  GET_AWAITABLE    
              324  LOAD_CONST               None
              326  YIELD_FROM       
              328  POP_TOP          

 L. 224       330  LOAD_FAST                'ctx'
              332  LOAD_METHOD              send
              334  LOAD_STR                 "That's not a valid bug report, "
              336  LOAD_FAST                'ctx'
              338  LOAD_ATTR                author
              340  LOAD_ATTR                name
              342  FORMAT_VALUE          0  ''
              344  LOAD_STR                 '. Please check your DMs.'
              346  BUILD_STRING_3        3  ''
              348  CALL_METHOD_1         1  ''
              350  GET_AWAITABLE    
              352  LOAD_CONST               None
              354  YIELD_FROM       
              356  POP_TOP          
              358  POP_BLOCK        
              360  JUMP_FORWARD        786  'to 786'
            362_0  COME_FROM_FINALLY   310  '310'

 L. 225       362  DUP_TOP          
              364  LOAD_GLOBAL              Exception
              366  COMPARE_OP               exception-match
          368_370  POP_JUMP_IF_FALSE   410  'to 410'
              372  POP_TOP          
              374  POP_TOP          
              376  POP_TOP          

 L. 226       378  LOAD_FAST                'ctx'
              380  LOAD_METHOD              send
              382  LOAD_STR                 "That's not a valid bug report, "
              384  LOAD_FAST                'ctx'
              386  LOAD_ATTR                author
              388  LOAD_ATTR                name
              390  FORMAT_VALUE          0  ''
              392  LOAD_STR                 '. The launcher is being redesigned.'
              394  BUILD_STRING_3        3  ''
              396  CALL_METHOD_1         1  ''
              398  GET_AWAITABLE    
              400  LOAD_CONST               None
              402  YIELD_FROM       
              404  POP_TOP          
              406  POP_EXCEPT       
              408  JUMP_FORWARD        786  'to 786'
            410_0  COME_FROM           368  '368'
              410  END_FINALLY      
          412_414  JUMP_FORWARD        786  'to 786'
            416_0  COME_FROM           306  '306'

 L. 227       416  LOAD_STR                 'crash'
              418  LOAD_FAST                'arg'
              420  LOAD_METHOD              lower
              422  CALL_METHOD_0         0  ''
              424  COMPARE_OP               in
          426_428  POP_JUMP_IF_FALSE   628  'to 628'

 L. 228       430  SETUP_FINALLY       482  'to 482'

 L. 229       432  LOAD_FAST                'ctx'
              434  LOAD_ATTR                author
              436  LOAD_METHOD              send
              438  LOAD_STR                 "There are multiple possiblilities why the game may have crashed.\n1: The game might be in an inaccessible location. Try moving the game somewhere more suitable (for example, your desktop).\n2: You may need at least 4 GB of RAM to run the game correctly. Try lowering your settings or add more RAM to your PC.\n3: The files may be corrupted. Try re-extracting the game. If that doesn't work, try downloading it again."
              440  CALL_METHOD_1         1  ''
              442  GET_AWAITABLE    
              444  LOAD_CONST               None
              446  YIELD_FROM       
              448  POP_TOP          

 L. 234       450  LOAD_FAST                'ctx'
              452  LOAD_METHOD              send

 L. 235       454  LOAD_STR                 'That might not be valid bug report (auto-detected), '
              456  LOAD_FAST                'ctx'
              458  LOAD_ATTR                author
              460  LOAD_ATTR                name
              462  FORMAT_VALUE          0  ''
              464  LOAD_STR                 '. Please check your DMs.\nHowever, for certain reasons, the bug report will be posted anyway.'
              466  BUILD_STRING_3        3  ''

 L. 234       468  CALL_METHOD_1         1  ''
              470  GET_AWAITABLE    
              472  LOAD_CONST               None
              474  YIELD_FROM       
              476  POP_TOP          
              478  POP_BLOCK        
              480  JUMP_FORWARD        626  'to 626'
            482_0  COME_FROM_FINALLY   430  '430'

 L. 238       482  DUP_TOP          
              484  LOAD_GLOBAL              Exception
              486  COMPARE_OP               exception-match
          488_490  POP_JUMP_IF_FALSE   624  'to 624'
              492  POP_TOP          
              494  POP_TOP          
              496  POP_TOP          

 L. 239       498  LOAD_FAST                'ctx'
              500  LOAD_METHOD              send
              502  LOAD_STR                 'That might not be valid bug report (auto-detected), '
              504  LOAD_FAST                'ctx'
              506  LOAD_ATTR                author
              508  LOAD_ATTR                name
              510  FORMAT_VALUE          0  ''
              512  LOAD_STR                 '. Ask <#439017534709170187> for more information.\nHowever, for certain reasons, the bug report will be posted anyway.'
              514  BUILD_STRING_3        3  ''
              516  CALL_METHOD_1         1  ''
              518  GET_AWAITABLE    
              520  LOAD_CONST               None
              522  YIELD_FROM       
              524  POP_TOP          

 L. 243       526  LOAD_GLOBAL              discord
              528  LOAD_ATTR                Embed
              530  LOAD_STR                 '**New bug 🐞**'
              532  LOAD_GLOBAL              random
              534  LOAD_METHOD              randint
              536  LOAD_CONST               0
              538  LOAD_CONST               16777215
              540  CALL_METHOD_2         2  ''
              542  LOAD_CONST               ('title', 'color')
              544  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              546  STORE_FAST               'embed'

 L. 244       548  LOAD_FAST                'embed'
              550  LOAD_ATTR                add_field

 L. 245       552  LOAD_STR                 'New bug report by '
              554  LOAD_FAST                'ctx'
              556  LOAD_ATTR                author
              558  LOAD_ATTR                name
              560  FORMAT_VALUE          0  ''
              562  LOAD_STR                 ':'
              564  BUILD_STRING_3        3  ''

 L. 246       566  LOAD_FAST                'arg'
              568  FORMAT_VALUE          0  ''

 L. 244       570  LOAD_CONST               ('name', 'value')
              572  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              574  POP_TOP          

 L. 247       576  LOAD_FAST                'embed'
              578  LOAD_ATTR                set_footer
              580  LOAD_STR                 'Midori Bot'
              582  LOAD_FAST                'self'
              584  LOAD_ATTR                bot
              586  LOAD_ATTR                user
              588  LOAD_ATTR                avatar_url_as
              590  LOAD_STR                 'png'
              592  LOAD_CONST               ('format',)
              594  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              596  LOAD_CONST               ('text', 'icon_url')
              598  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              600  POP_TOP          

 L. 248       602  LOAD_FAST                'channel'
              604  LOAD_ATTR                send
              606  LOAD_FAST                'embed'
              608  LOAD_CONST               ('embed',)
              610  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              612  GET_AWAITABLE    
              614  LOAD_CONST               None
              616  YIELD_FROM       
              618  POP_TOP          
              620  POP_EXCEPT       
              622  JUMP_FORWARD        626  'to 626'
            624_0  COME_FROM           488  '488'
              624  END_FINALLY      
            626_0  COME_FROM           622  '622'
            626_1  COME_FROM           480  '480'
              626  JUMP_FORWARD        786  'to 786'
            628_0  COME_FROM           426  '426'

 L. 249       628  LOAD_STR                 'step 1'
              630  LOAD_FAST                'arg'
              632  LOAD_METHOD              lower
              634  CALL_METHOD_0         0  ''
              636  COMPARE_OP               not-in
          638_640  POP_JUMP_IF_FALSE   672  'to 672'

 L. 250       642  LOAD_FAST                'ctx'
              644  LOAD_METHOD              send
              646  LOAD_STR                 "That's not a valid bug report, "
              648  LOAD_FAST                'ctx'
              650  LOAD_ATTR                author
              652  LOAD_ATTR                name
              654  FORMAT_VALUE          0  ''
              656  LOAD_STR                 '.Please use `-report` to learn how to properly report a bug.\nYou may be missing stuff like "Step 1", "Step 2", etc.\nI can\'t accept reports unless they\'re written clearly.'
              658  BUILD_STRING_3        3  ''
              660  CALL_METHOD_1         1  ''
              662  GET_AWAITABLE    
              664  LOAD_CONST               None
              666  YIELD_FROM       
              668  POP_TOP          
              670  JUMP_FORWARD        786  'to 786'
            672_0  COME_FROM           638  '638'

 L. 255       672  LOAD_GLOBAL              discord
              674  LOAD_ATTR                Embed
              676  LOAD_STR                 '**New bug 🐞**'
              678  LOAD_GLOBAL              random
              680  LOAD_METHOD              randint
              682  LOAD_CONST               0
              684  LOAD_CONST               16777215
              686  CALL_METHOD_2         2  ''
              688  LOAD_CONST               ('title', 'color')
              690  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              692  STORE_FAST               'embed'

 L. 256       694  LOAD_FAST                'embed'
              696  LOAD_ATTR                add_field
              698  LOAD_STR                 'New bug report by '
              700  LOAD_FAST                'ctx'
              702  LOAD_ATTR                author
              704  LOAD_ATTR                name
              706  FORMAT_VALUE          0  ''
              708  LOAD_STR                 ':'
              710  BUILD_STRING_3        3  ''
              712  LOAD_FAST                'arg'
              714  FORMAT_VALUE          0  ''
              716  LOAD_CONST               ('name', 'value')
              718  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              720  POP_TOP          

 L. 257       722  LOAD_FAST                'embed'
              724  LOAD_ATTR                set_footer
              726  LOAD_STR                 'Midori Bot'
              728  LOAD_FAST                'self'
              730  LOAD_ATTR                bot
            732_0  COME_FROM           360  '360'
            732_1  COME_FROM           240  '240'
              732  LOAD_ATTR                user
              734  LOAD_ATTR                avatar_url_as
              736  LOAD_STR                 'png'
              738  LOAD_CONST               ('format',)
              740  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              742  LOAD_CONST               ('text', 'icon_url')
              744  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
            746_0  COME_FROM           134  '134'
              746  POP_TOP          

 L. 258       748  LOAD_FAST                'channel'
              750  LOAD_ATTR                send
              752  LOAD_FAST                'embed'
              754  LOAD_CONST               ('embed',)
              756  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              758  GET_AWAITABLE    
              760  LOAD_CONST               None
              762  YIELD_FROM       
              764  POP_TOP          

 L. 259       766  LOAD_FAST                'ctx'
              768  LOAD_ATTR                send
              770  LOAD_STR                 'Thanks for the report! Time for me to annoy YandereDev! 🐞'
              772  LOAD_CONST               15
              774  LOAD_CONST               ('delete_after',)
              776  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              778  GET_AWAITABLE    
            780_0  COME_FROM           408  '408'
            780_1  COME_FROM           288  '288'
            780_2  COME_FROM           168  '168'
              780  LOAD_CONST               None
              782  YIELD_FROM       
              784  POP_TOP          
            786_0  COME_FROM           670  '670'
            786_1  COME_FROM           626  '626'
            786_2  COME_FROM           412  '412'
            786_3  COME_FROM           292  '292'
            786_4  COME_FROM           172  '172'

Parse error at or near `COME_FROM' instruction at offset 732_0

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def accept(self, ctx, reportid):
        reportchannel = self.bot.get_channel(652209659092008983)
        acceptchannel = self.bot.get_channel(652209705179021316)
        reportmsg = await reportchannel.fetch_message(reportid)
        report = reportmsg.embeds[0].copy()
        report.title = '✅ **Accepted Bug**'
        await reportmsg.delete()
        await acceptchannel.send(embed=report)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def deny(self, ctx, reportid):
        reportchannel = self.bot.get_channel(652209659092008983)
        denychannel = self.bot.get_channel(652209684668874806)
        reportmsg = await reportchannel.fetch_message(reportid)
        report = reportmsg.embeds[0].copy()
        report.title = '❌ **Denied Bug**'
        await reportmsg.delete()
        await denychannel.send(embed=report)

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.manage_message_owner)
    async def warn(self, ctx, member: discord.Member=None, *, reason):
        if member.id == ctx.author.id:
            return await ctx.send("Don't warn yourself. silly!")
            if member.id == 396241937658675206:
                return await ctx.send("You can't warn my developer!")
            Warn = f":warning: Warning logged for {member}"
            Warnchannel = self.bot.get_channel(615882185190408194)
            embed = discord.Embed(title='Warn reason: ', description=(f"{reason}"), color=16737380)
            embed.add_field(name='Moderator: ', value=(f"{ctx.author.mention}"), inline=True)
            await Warnchannel.send((f"{Warn}"), embed=embed)
            try:
                await member.send(f"You were warned in {ctx.guild.name}, Reason: {reason}")
                await ctx.send(f"Warning logged for {member}, they were warned! :white_check_mark:", delete_after=10)
            except Exception:
                await ctx.send(f"Warning logged for {member}, :white_check_mark:\n                However, they were not warned in DMs. Most likely their DMs are                 disabled or maybe they blocked me!", delete_after=10)

        else:
            try:
                await asyncio.sleep(10)
                await ctx.message.delete()
            except Exception:
                pass

    @commands.command(aliases=['nickname'])
    @commands.guild_only()
    @commands.check(checks.manage_message_owner)
    async def nick(self, ctx, *, name: str=None):
        nickperm = False
        if nickperm:
            try:
                await ctx.guild.me.edit(nick=name)
                if name:
                    await ctx.send(f"Successfully changed nickname to **{name}**")
                else:
                    await ctx.send('Successfully removed nickname')
            except Exception as err:
                try:
                    await ctx.send(f"An error has occurred, {err}")
                finally:
                    err = None
                    del err

    @commands.command(aliases=['at'])
    @commands.guild_only()
    @commands.check(checks.manage_message_owner)
    async def announcetwitch(self, ctx):
        channel = self.bot.get_channel(528025733130485760)
        embed = discord.Embed(title='**YandereDev is streaming!**', color=(random.randint(0, 16777215)))
        embed.add_field(name='Come and join the stream! <a:YanYay:595606256945725470>',
          value='[Click here](https://twitch.tv/yanderedev) or click the link below!')
        embed.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
        await channel.send(embed=embed)
        await channel.send('https://twitch.tv/yanderedev')
        await ctx.send('Successfully sent twitch link!', delete_after=60)

    @commands.command(aliases=['tc'])
    @commands.guild_only()
    @commands.check(checks.is_joel)
    async def twitchchat(self, ctx, *, arg):
        channel = self.bot.get_channel(650389092252778579)
        embed = discord.Embed(color=(random.randint(0, 16777215)))
        embed.add_field(name='**Announcement!** <a:YanYay:595606256945725470>',
          value=(f"{arg}"))
        embed.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
        await channel.trigger_typing()
        await asyncio.sleep(5)
        await channel.send(embed=embed)
        await ctx.send('Successfully sent!')

    @commands.command()
    @commands.guild_only()
    @commands.check(checks._owners)
    async def say--- This code section failed: ---

 L. 359         0  SETUP_FINALLY        22  'to 22'

 L. 360         2  LOAD_FAST                'ctx'
                4  LOAD_ATTR                message
                6  LOAD_METHOD              delete
                8  CALL_METHOD_0         0  ''
               10  GET_AWAITABLE    
               12  LOAD_CONST               None
               14  YIELD_FROM       
               16  POP_TOP          
               18  POP_BLOCK        
               20  JUMP_FORWARD         44  'to 44'
             22_0  COME_FROM_FINALLY     0  '0'

 L. 361        22  DUP_TOP          
               24  LOAD_GLOBAL              discord
               26  LOAD_ATTR                Forbidden
               28  COMPARE_OP               exception-match
               30  POP_JUMP_IF_FALSE    42  'to 42'
               32  POP_TOP          
               34  POP_TOP          
               36  POP_TOP          

 L. 362        38  POP_EXCEPT       
               40  JUMP_FORWARD         44  'to 44'
             42_0  COME_FROM            30  '30'
               42  END_FINALLY      
             44_0  COME_FROM            40  '40'
             44_1  COME_FROM            20  '20'

 L. 363        44  LOAD_FAST                'ctx'
               46  LOAD_METHOD              typing
               48  CALL_METHOD_0         0  ''
               50  BEFORE_ASYNC_WITH
               52  GET_AWAITABLE    
               54  LOAD_CONST               None
               56  YIELD_FROM       
               58  SETUP_ASYNC_WITH     82  'to 82'
               60  POP_TOP          

 L. 364        62  LOAD_FAST                'ctx'
               64  LOAD_METHOD              send
               66  LOAD_FAST                'arg'
               68  CALL_METHOD_1         1  ''
               70  GET_AWAITABLE    
               72  LOAD_CONST               None
               74  YIELD_FROM       
               76  POP_TOP          
               78  POP_BLOCK        
               80  BEGIN_FINALLY    
             82_0  COME_FROM_ASYNC_WITH    58  '58'
               82  WITH_CLEANUP_START
               84  GET_AWAITABLE    
               86  LOAD_CONST               None
               88  YIELD_FROM       
               90  WITH_CLEANUP_FINISH
               92  END_FINALLY      

Parse error at or near `COME_FROM_ASYNC_WITH' instruction at offset 82_0

    @commands.command()
    @commands.guild_only()
    @commands.check(checks._owners)
    async def embed(self, ctx, *, arg):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        else:
            await ctx.trigger_typing()
            await asyncio.sleep(5)
            embed = discord.Embed(color=(random.randint(0, 16777215)))
            embed.add_field(name='New email!', value=arg)
            embed.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.check(checks._owners)
    async def dm--- This code section failed: ---

 L. 386         0  LOAD_FAST                'member'
                2  LOAD_FAST                'ctx'
                4  LOAD_ATTR                bot
                6  COMPARE_OP               ==
                8  POP_JUMP_IF_FALSE    26  'to 26'

 L. 387        10  LOAD_FAST                'ctx'
               12  LOAD_METHOD              send
               14  LOAD_STR                 "Nice one. Trying to tell a bot to DM itself. Wow, I bet nobody's ever thought of that before. <a:Clap:463638092746850326>"
               16  CALL_METHOD_1         1  ''
               18  GET_AWAITABLE    
               20  LOAD_CONST               None
               22  YIELD_FROM       
               24  RETURN_VALUE     
             26_0  COME_FROM             8  '8'

 L. 390        26  SETUP_FINALLY       134  'to 134'

 L. 391        28  LOAD_FAST                'member'
               30  LOAD_METHOD              send
               32  LOAD_FAST                'message'
               34  FORMAT_VALUE          0  ''
               36  LOAD_STR                 "\n> I can't see DMs, so there's no point in replying."
               38  BUILD_STRING_2        2  ''
               40  CALL_METHOD_1         1  ''
               42  GET_AWAITABLE    
               44  LOAD_CONST               None
               46  YIELD_FROM       
               48  POP_TOP          

 L. 392        50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                send
               54  LOAD_STR                 'Direct message sent!'
               56  LOAD_CONST               5
               58  LOAD_CONST               ('delete_after',)
               60  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               62  GET_AWAITABLE    
               64  LOAD_CONST               None
               66  YIELD_FROM       
               68  POP_TOP          

 L. 393        70  LOAD_GLOBAL              asyncio
               72  LOAD_METHOD              sleep
               74  LOAD_CONST               5
               76  CALL_METHOD_1         1  ''
               78  GET_AWAITABLE    
               80  LOAD_CONST               None
               82  YIELD_FROM       
               84  POP_TOP          

 L. 394        86  SETUP_FINALLY       108  'to 108'

 L. 395        88  LOAD_FAST                'ctx'
               90  LOAD_ATTR                message
               92  LOAD_METHOD              delete
               94  CALL_METHOD_0         0  ''
               96  GET_AWAITABLE    
               98  LOAD_CONST               None
              100  YIELD_FROM       
              102  POP_TOP          
              104  POP_BLOCK        
              106  JUMP_FORWARD        128  'to 128'
            108_0  COME_FROM_FINALLY    86  '86'

 L. 396       108  DUP_TOP          
              110  LOAD_GLOBAL              Exception
              112  COMPARE_OP               exception-match
              114  POP_JUMP_IF_FALSE   126  'to 126'
              116  POP_TOP          
              118  POP_TOP          
              120  POP_TOP          

 L. 397       122  POP_EXCEPT       
              124  JUMP_FORWARD        128  'to 128'
            126_0  COME_FROM           114  '114'
              126  END_FINALLY      
            128_0  COME_FROM           124  '124'
            128_1  COME_FROM           106  '106'

 L. 398       128  POP_BLOCK        
              130  LOAD_CONST               None
              132  RETURN_VALUE     
            134_0  COME_FROM_FINALLY    26  '26'

 L. 399       134  DUP_TOP          
              136  LOAD_GLOBAL              Exception
              138  COMPARE_OP               exception-match
          140_142  POP_JUMP_IF_FALSE   340  'to 340'
              144  POP_TOP          
              146  POP_TOP          
              148  POP_TOP          

 L. 400       150  LOAD_FAST                'ctx'
              152  LOAD_ATTR                send
              154  LOAD_STR                 "Direct message failed!\nPlease make their DMs are open and I'm not blocked!"

 L. 401       156  LOAD_CONST               5

 L. 400       158  LOAD_CONST               ('delete_after',)
              160  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              162  GET_AWAITABLE    
              164  LOAD_CONST               None
              166  YIELD_FROM       
              168  POP_TOP          

 L. 402       170  LOAD_GLOBAL              asyncio
              172  LOAD_METHOD              sleep
              174  LOAD_CONST               5
              176  CALL_METHOD_1         1  ''
              178  GET_AWAITABLE    
              180  LOAD_CONST               None
              182  YIELD_FROM       
              184  POP_TOP          

 L. 403       186  SETUP_FINALLY       208  'to 208'

 L. 404       188  LOAD_FAST                'ctx'
              190  LOAD_ATTR                message
              192  LOAD_METHOD              delete
              194  CALL_METHOD_0         0  ''
              196  GET_AWAITABLE    
              198  LOAD_CONST               None
              200  YIELD_FROM       
              202  POP_TOP          
              204  POP_BLOCK        
              206  JUMP_FORWARD        336  'to 336'
            208_0  COME_FROM_FINALLY   186  '186'

 L. 405       208  DUP_TOP          
              210  LOAD_GLOBAL              Exception
              212  COMPARE_OP               exception-match
          214_216  POP_JUMP_IF_FALSE   334  'to 334'
              218  POP_TOP          
              220  POP_TOP          
              222  POP_TOP          

 L. 406       224  LOAD_GLOBAL              asyncio
              226  LOAD_METHOD              sleep
              228  LOAD_CONST               1
              230  CALL_METHOD_1         1  ''
              232  GET_AWAITABLE    
              234  LOAD_CONST               None
              236  YIELD_FROM       
              238  POP_TOP          

 L. 407       240  LOAD_FAST                'ctx'
              242  LOAD_ATTR                send
              244  LOAD_STR                 "**Error:** I can't delete that message. Let me see what the problem is��?"

 L. 408       246  LOAD_CONST               10.5

 L. 407       248  LOAD_CONST               ('delete_after',)
              250  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              252  GET_AWAITABLE    
              254  LOAD_CONST               None
              256  YIELD_FROM       
              258  POP_TOP          

 L. 409       260  LOAD_GLOBAL              asyncio
              262  LOAD_METHOD              sleep
              264  LOAD_CONST               0.5
              266  CALL_METHOD_1         1  ''
              268  GET_AWAITABLE    
              270  LOAD_CONST               None
              272  YIELD_FROM       
              274  POP_TOP          

 L. 410       276  LOAD_FAST                'ctx'
              278  LOAD_ATTR                me
              280  LOAD_ATTR                guild_permissions
              282  LOAD_ATTR                manage_messages
          284_286  POP_JUMP_IF_FALSE   310  'to 310'

 L. 411       288  LOAD_FAST                'ctx'
              290  LOAD_ATTR                send

 L. 412       292  LOAD_STR                 "**Problem found!** Most likely, the channel has declining message managing. Theoretically, this permission isn't necessary to decline if roles already decline it."

 L. 415       294  LOAD_CONST               10

 L. 411       296  LOAD_CONST               ('delete_after',)
              298  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              300  GET_AWAITABLE    
              302  LOAD_CONST               None
              304  YIELD_FROM       
              306  POP_TOP          
              308  JUMP_FORWARD        330  'to 330'
            310_0  COME_FROM           284  '284'

 L. 417       310  LOAD_FAST                'ctx'
              312  LOAD_ATTR                send

 L. 418       314  LOAD_STR                 '**Problem found!** Forbidden permission: `MANAGE_MESSAGES`.\nThis permission is required to delete your command.'

 L. 420       316  LOAD_CONST               10

 L. 417       318  LOAD_CONST               ('delete_after',)
              320  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              322  GET_AWAITABLE    
              324  LOAD_CONST               None
              326  YIELD_FROM       
              328  POP_TOP          
            330_0  COME_FROM           308  '308'
              330  POP_EXCEPT       
              332  JUMP_FORWARD        336  'to 336'
            334_0  COME_FROM           214  '214'
              334  END_FINALLY      
            336_0  COME_FROM           332  '332'
            336_1  COME_FROM           206  '206'
              336  POP_EXCEPT       
              338  JUMP_FORWARD        342  'to 342'
            340_0  COME_FROM           140  '140'
              340  END_FINALLY      
            342_0  COME_FROM           338  '338'

Parse error at or near `RETURN_VALUE' instruction at offset 132

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.disabled_channels)
    @commands.cooldown(1, 20, BucketType.user)
    async def bug(self, ctx):
        e = discord.Embed(title='**I found a bug!**',
          color=(random.randint(0, 16777215)))
        e.set_image(url='https://cdn.discordapp.com/attachments/615881983310036994/617631348730888192/Screenshot_731.png')
        e.set_footer(text='Midori Bot', icon_url=self.bot.user.avatar_url_as(format='png'))
        try:
            await ctx.send(embed=e)
        except discord.Forbidden:
            await ctx.send('**Error!**\nMissing permissions `embed_links`!')

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.manage_message_owner)
    async def purge--- This code section failed: ---

 L. 442         0  SETUP_FINALLY       138  'to 138'

 L. 443         2  LOAD_FAST                'ctx'
                4  LOAD_ATTR                message
                6  LOAD_METHOD              delete
                8  CALL_METHOD_0         0  ''
               10  GET_AWAITABLE    
               12  LOAD_CONST               None
               14  YIELD_FROM       
               16  POP_TOP          

 L. 444        18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                channel
               22  LOAD_ATTR                purge
               24  LOAD_FAST                'amount'
               26  LOAD_CONST               ('limit',)
               28  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               30  GET_AWAITABLE    
               32  LOAD_CONST               None
               34  YIELD_FROM       
               36  STORE_FAST               'deleted'

 L. 445        38  LOAD_FAST                'ctx'
               40  LOAD_ATTR                send
               42  LOAD_STR                 'Deleted '
               44  LOAD_GLOBAL              len
               46  LOAD_FAST                'deleted'
               48  CALL_FUNCTION_1       1  ''
               50  FORMAT_VALUE          0  ''
               52  LOAD_STR                 ' messages!'
               54  BUILD_STRING_3        3  ''
               56  LOAD_CONST               3
               58  LOAD_CONST               ('delete_after',)
               60  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               62  GET_AWAITABLE    
               64  LOAD_CONST               None
               66  YIELD_FROM       
               68  POP_TOP          

 L. 446        70  LOAD_GLOBAL              asyncio
               72  LOAD_METHOD              sleep
               74  LOAD_CONST               3
               76  CALL_METHOD_1         1  ''
               78  GET_AWAITABLE    
               80  LOAD_CONST               None
               82  YIELD_FROM       
               84  POP_TOP          

 L. 447        86  LOAD_FAST                'ctx'
               88  LOAD_METHOD              trigger_typing
               90  CALL_METHOD_0         0  ''
               92  GET_AWAITABLE    
               94  LOAD_CONST               None
               96  YIELD_FROM       
               98  POP_TOP          

 L. 448       100  LOAD_GLOBAL              asyncio
              102  LOAD_METHOD              sleep
              104  LOAD_CONST               3
              106  CALL_METHOD_1         1  ''
              108  GET_AWAITABLE    
              110  LOAD_CONST               None
              112  YIELD_FROM       
              114  POP_TOP          

 L. 449       116  LOAD_FAST                'ctx'
              118  LOAD_METHOD              send
              120  LOAD_STR                 "Oh my. What happened here? It seems we've gone back in time. What should we talk about?"
              122  CALL_METHOD_1         1  ''
              124  GET_AWAITABLE    
              126  LOAD_CONST               None
              128  YIELD_FROM       
              130  POP_TOP          

 L. 450       132  POP_BLOCK        
              134  LOAD_CONST               None
              136  RETURN_VALUE     
            138_0  COME_FROM_FINALLY     0  '0'

 L. 451       138  DUP_TOP          
              140  LOAD_GLOBAL              Exception
              142  COMPARE_OP               exception-match
              144  POP_JUMP_IF_FALSE   212  'to 212'
              146  POP_TOP          
              148  POP_TOP          
              150  POP_TOP          

 L. 452       152  LOAD_FAST                'ctx'
              154  LOAD_ATTR                me
              156  LOAD_ATTR                guild_permissions
              158  LOAD_ATTR                manage_messages
              160  LOAD_CONST               True
              162  COMPARE_OP               is
              164  POP_JUMP_IF_FALSE   188  'to 188'

 L. 453       166  LOAD_FAST                'ctx'
              168  LOAD_ATTR                send

 L. 454       170  LOAD_STR                 "**Error:** I can't purge the channel. Most likely, the channel has declining message managing."

 L. 455       172  LOAD_CONST               10

 L. 453       174  LOAD_CONST               ('delete_after',)
              176  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              178  GET_AWAITABLE    
              180  LOAD_CONST               None
              182  YIELD_FROM       
              184  POP_TOP          
              186  JUMP_FORWARD        208  'to 208'
            188_0  COME_FROM           164  '164'

 L. 457       188  LOAD_FAST                'ctx'
              190  LOAD_ATTR                send

 L. 458       192  LOAD_STR                 "**Error:** I can't purge the channel. Most likely, I don't have message managing in roles."

 L. 459       194  LOAD_CONST               10

 L. 457       196  LOAD_CONST               ('delete_after',)
              198  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              200  GET_AWAITABLE    
              202  LOAD_CONST               None
              204  YIELD_FROM       
              206  POP_TOP          
            208_0  COME_FROM           186  '186'
              208  POP_EXCEPT       
              210  JUMP_FORWARD        214  'to 214'
            212_0  COME_FROM           144  '144'
              212  END_FINALLY      
            214_0  COME_FROM           210  '210'

Parse error at or near `RETURN_VALUE' instruction at offset 136

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.manage_message_owner)
    async def ban--- This code section failed: ---

 L. 465         0  LOAD_FAST                'member'
                2  LOAD_CONST               None
                4  COMPARE_OP               is
                6  POP_JUMP_IF_FALSE    56  'to 56'

 L. 466         8  LOAD_GLOBAL              discord
               10  LOAD_ATTR                Embed
               12  LOAD_STR                 'ban usage'
               14  LOAD_STR                 '-ban @user [Reason]'

 L. 467        16  LOAD_GLOBAL              random
               18  LOAD_METHOD              randint
               20  LOAD_CONST               0
               22  LOAD_CONST               16777215
               24  CALL_METHOD_2         2  ''

 L. 466        26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'embed'

 L. 468        32  LOAD_FAST                'ctx'
               34  LOAD_ATTR                send
               36  LOAD_STR                 'Usage to ban users:'
               38  LOAD_FAST                'embed'
               40  LOAD_CONST               ('embed',)
               42  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               44  GET_AWAITABLE    
               46  LOAD_CONST               None
               48  YIELD_FROM       
               50  POP_TOP          

 L. 469        52  LOAD_CONST               None
               54  RETURN_VALUE     
             56_0  COME_FROM             6  '6'

 L. 470        56  SETUP_FINALLY       264  'to 264'

 L. 471        58  LOAD_FAST                'member'
               60  LOAD_ATTR                guild_permissions
               62  LOAD_ATTR                manage_messages
               64  LOAD_CONST               True
               66  COMPARE_OP               is
               68  POP_JUMP_IF_FALSE    92  'to 92'

 L. 472        70  LOAD_GLOBAL              print
               72  LOAD_STR                 'trigger'
               74  CALL_FUNCTION_1       1  ''
               76  POP_TOP          

 L. 473        78  LOAD_GLOBAL              ValueError
               80  LOAD_STR                 'Moderator was attempted to ban'
               82  CALL_FUNCTION_1       1  ''
               84  RAISE_VARARGS_1       1  ''

 L. 474        86  POP_BLOCK        
               88  LOAD_CONST               None
               90  RETURN_VALUE     
             92_0  COME_FROM            68  '68'

 L. 476        92  LOAD_FAST                'member'
               94  LOAD_ATTR                ban
               96  LOAD_FAST                'reason'
               98  LOAD_CONST               ('reason',)
              100  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              102  GET_AWAITABLE    
              104  LOAD_CONST               None
              106  YIELD_FROM       
              108  POP_TOP          

 L. 477       110  LOAD_FAST                'ctx'
              112  LOAD_ATTR                send
              114  LOAD_STR                 'banned '
              116  LOAD_FAST                'member'
              118  LOAD_ATTR                name
              120  FORMAT_VALUE          0  ''
              122  LOAD_STR                 '#'
              124  LOAD_FAST                'member'
              126  LOAD_ATTR                discriminator
              128  FORMAT_VALUE          0  ''
              130  BUILD_STRING_4        4  ''
              132  LOAD_CONST               10
              134  LOAD_CONST               ('delete_after',)
              136  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              138  GET_AWAITABLE    
              140  LOAD_CONST               None
              142  YIELD_FROM       
              144  POP_TOP          

 L. 478       146  SETUP_FINALLY       246  'to 246'

 L. 479       148  LOAD_GLOBAL              asyncio
              150  LOAD_METHOD              sleep
              152  LOAD_CONST               10
              154  CALL_METHOD_1         1  ''
              156  GET_AWAITABLE    
              158  LOAD_CONST               None
              160  YIELD_FROM       
              162  POP_TOP          

 L. 480       164  LOAD_FAST                'ctx'
              166  LOAD_ATTR                message
              168  LOAD_METHOD              delete
              170  CALL_METHOD_0         0  ''
              172  GET_AWAITABLE    
              174  LOAD_CONST               None
              176  YIELD_FROM       
              178  POP_TOP          

 L. 481       180  LOAD_GLOBAL              asyncio
              182  LOAD_METHOD              sleep
              184  LOAD_CONST               3
              186  CALL_METHOD_1         1  ''
              188  GET_AWAITABLE    
              190  LOAD_CONST               None
              192  YIELD_FROM       
              194  POP_TOP          

 L. 482       196  LOAD_FAST                'ctx'
              198  LOAD_METHOD              trigger_typing
              200  CALL_METHOD_0         0  ''
              202  GET_AWAITABLE    
              204  LOAD_CONST               None
              206  YIELD_FROM       
              208  POP_TOP          

 L. 483       210  LOAD_GLOBAL              asyncio
              212  LOAD_METHOD              sleep
              214  LOAD_CONST               3
              216  CALL_METHOD_1         1  ''
              218  GET_AWAITABLE    
              220  LOAD_CONST               None
              222  YIELD_FROM       
              224  POP_TOP          

 L. 484       226  LOAD_FAST                'ctx'
              228  LOAD_METHOD              send

 L. 485       230  LOAD_STR                 "Oh my. What happened here? It seems we've gone back in time. What should we talk about?"

 L. 484       232  CALL_METHOD_1         1  ''
              234  GET_AWAITABLE    
              236  LOAD_CONST               None
              238  YIELD_FROM       
              240  POP_TOP          
              242  POP_BLOCK        
              244  JUMP_FORWARD        258  'to 258'
            246_0  COME_FROM_FINALLY   146  '146'

 L. 486       246  POP_TOP          
              248  POP_TOP          
              250  POP_TOP          

 L. 487       252  POP_EXCEPT       
              254  JUMP_FORWARD        258  'to 258'
              256  END_FINALLY      
            258_0  COME_FROM           254  '254'
            258_1  COME_FROM           244  '244'
              258  POP_BLOCK        
          260_262  JUMP_FORWARD        552  'to 552'
            264_0  COME_FROM_FINALLY    56  '56'

 L. 488       264  POP_TOP          
              266  POP_TOP          
              268  POP_TOP          

 L. 489       270  LOAD_FAST                'member'
              272  LOAD_ATTR                id
              274  LOAD_CONST               396241937658675206
              276  COMPARE_OP               ==
          278_280  POP_JUMP_IF_FALSE   300  'to 300'

 L. 490       282  LOAD_FAST                'ctx'
              284  LOAD_METHOD              send
              286  LOAD_STR                 'You cannot ban Joel, The bot coder <:YanWink:425913980809379850>'
              288  CALL_METHOD_1         1  ''
              290  GET_AWAITABLE    
              292  LOAD_CONST               None
              294  YIELD_FROM       
              296  POP_TOP          
              298  JUMP_FORWARD        546  'to 546'
            300_0  COME_FROM           278  '278'

 L. 491       300  LOAD_FAST                'member'
              302  LOAD_ATTR                id
              304  LOAD_CONST               135161245941628928
              306  COMPARE_OP               ==
          308_310  POP_JUMP_IF_FALSE   330  'to 330'

 L. 492       312  LOAD_FAST                'ctx'
              314  LOAD_METHOD              send
              316  LOAD_STR                 'You cannot ban our beloved YandereDev <:YanWink:425913980809379850>'
              318  CALL_METHOD_1         1  ''
              320  GET_AWAITABLE    
              322  LOAD_CONST               None
              324  YIELD_FROM       
              326  POP_TOP          
              328  JUMP_FORWARD        546  'to 546'
            330_0  COME_FROM           308  '308'

 L. 493       330  LOAD_FAST                'member'
              332  LOAD_ATTR                id
              334  LOAD_CONST               614730255672016896
              336  COMPARE_OP               ==
          338_340  POP_JUMP_IF_FALSE   360  'to 360'

 L. 494       342  LOAD_FAST                'ctx'
              344  LOAD_METHOD              send
              346  LOAD_STR                 'I cannot ban myself, <:YanWink:425913980809379850>'
              348  CALL_METHOD_1         1  ''
              350  GET_AWAITABLE    
              352  LOAD_CONST               None
              354  YIELD_FROM       
              356  POP_TOP          
              358  JUMP_FORWARD        546  'to 546'
            360_0  COME_FROM           338  '338'

 L. 495       360  LOAD_FAST                'member'
              362  LOAD_ATTR                guild_permissions
              364  LOAD_ATTR                manage_messages
              366  LOAD_CONST               True
              368  COMPARE_OP               is
          370_372  POP_JUMP_IF_FALSE   392  'to 392'

 L. 496       374  LOAD_FAST                'ctx'
              376  LOAD_METHOD              send
              378  LOAD_STR                 'You cannot ban moderators <:YanWink:425913980809379850>'
              380  CALL_METHOD_1         1  ''
              382  GET_AWAITABLE    
              384  LOAD_CONST               None
              386  YIELD_FROM       
              388  POP_TOP          
              390  JUMP_FORWARD        546  'to 546'
            392_0  COME_FROM           370  '370'

 L. 497       392  LOAD_FAST                'ctx'
              394  LOAD_ATTR                me
              396  LOAD_ATTR                guild_permissions
              398  LOAD_ATTR                ban_members
          400_402  POP_JUMP_IF_TRUE    476  'to 476'

 L. 498       404  LOAD_FAST                'ctx'
              406  LOAD_ATTR                send

 L. 499       408  LOAD_STR                 "I cannot ban that person, I don't have the correct permission or my role is too low..."

 L. 500       410  LOAD_CONST               10

 L. 498       412  LOAD_CONST               ('delete_after',)
              414  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              416  GET_AWAITABLE    
              418  LOAD_CONST               None
              420  YIELD_FROM       
              422  POP_TOP          

 L. 501       424  SETUP_FINALLY       462  'to 462'

 L. 502       426  LOAD_GLOBAL              asyncio
              428  LOAD_METHOD              sleep
              430  LOAD_CONST               10
              432  CALL_METHOD_1         1  ''
              434  GET_AWAITABLE    
              436  LOAD_CONST               None
              438  YIELD_FROM       
              440  POP_TOP          

 L. 503       442  LOAD_FAST                'ctx'
              444  LOAD_ATTR                message
              446  LOAD_METHOD              delete
              448  CALL_METHOD_0         0  ''
              450  GET_AWAITABLE    
              452  LOAD_CONST               None
              454  YIELD_FROM       
              456  POP_TOP          
              458  POP_BLOCK        
              460  JUMP_FORWARD        474  'to 474'
            462_0  COME_FROM_FINALLY   424  '424'

 L. 504       462  POP_TOP          
              464  POP_TOP          
              466  POP_TOP          

 L. 505       468  POP_EXCEPT       
              470  JUMP_FORWARD        474  'to 474'
              472  END_FINALLY      
            474_0  COME_FROM           470  '470'
            474_1  COME_FROM           460  '460'
              474  JUMP_FORWARD        546  'to 546'
            476_0  COME_FROM           400  '400'

 L. 507       476  LOAD_FAST                'ctx'
              478  LOAD_ATTR                send
              480  LOAD_STR                 'An unknown issue occured... I cannot ban that person'
              482  LOAD_CONST               10
              484  LOAD_CONST               ('delete_after',)
              486  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              488  GET_AWAITABLE    
              490  LOAD_CONST               None
              492  YIELD_FROM       
              494  POP_TOP          

 L. 508       496  SETUP_FINALLY       534  'to 534'

 L. 509       498  LOAD_GLOBAL              asyncio
              500  LOAD_METHOD              sleep
              502  LOAD_CONST               10
              504  CALL_METHOD_1         1  ''
              506  GET_AWAITABLE    
              508  LOAD_CONST               None
              510  YIELD_FROM       
              512  POP_TOP          

 L. 510       514  LOAD_FAST                'ctx'
              516  LOAD_ATTR                message
              518  LOAD_METHOD              delete
              520  CALL_METHOD_0         0  ''
              522  GET_AWAITABLE    
              524  LOAD_CONST               None
              526  YIELD_FROM       
              528  POP_TOP          
              530  POP_BLOCK        
              532  JUMP_FORWARD        546  'to 546'
            534_0  COME_FROM_FINALLY   496  '496'

 L. 511       534  POP_TOP          
              536  POP_TOP          
              538  POP_TOP          

 L. 512       540  POP_EXCEPT       
              542  JUMP_FORWARD        546  'to 546'
              544  END_FINALLY      
            546_0  COME_FROM           542  '542'
            546_1  COME_FROM           532  '532'
            546_2  COME_FROM           474  '474'
            546_3  COME_FROM           390  '390'
            546_4  COME_FROM           358  '358'
            546_5  COME_FROM           328  '328'
            546_6  COME_FROM           298  '298'
              546  POP_EXCEPT       
              548  JUMP_FORWARD        552  'to 552'
              550  END_FINALLY      
            552_0  COME_FROM           548  '548'
            552_1  COME_FROM           260  '260'

Parse error at or near `LOAD_CONST' instruction at offset 88

    @commands.command(aliases=['hb'])
    @commands.check(checks.manage_message_owner)
    async def hackban(self, ctx, ID=None, *, reason=None):
        if ID is None:
            embed = discord.Embed(title='hackban usage', description='-hackban <user ID> [Reason]', color=(random.randint(0, 16777215)))
            await ctx.send('Usage to hackban users:', embed=embed)
            return
        try:
            await ctx.guild.ban(discord.Object(id=ID), reason=reason)
            name = await self.bot.fetch_user(ID)
            await ctx.send(f"I have hackbanned {name}", delete_after=10)
            await asyncio.sleep(10)
            await ctx.message.delete()
            await asyncio.sleep(3)
            await ctx.trigger_typing()
            await asyncio.sleep(3)
            await ctx.send("Oh my. What happened here? It seems we've gone back in time. What should we talk about?")
        except:
            await ctx.send('Sorry, I could not do that, am I missing the `BAN_MEMBERS` permission?', delete_after=10)

    @commands.command()
    @commands.guild_only()
    @commands.check(checks.manage_message_owner)
    async def kick--- This code section failed: ---

 L. 539         0  LOAD_FAST                'member'
                2  LOAD_CONST               None
                4  COMPARE_OP               is
                6  POP_JUMP_IF_FALSE    56  'to 56'

 L. 540         8  LOAD_GLOBAL              discord
               10  LOAD_ATTR                Embed
               12  LOAD_STR                 'Kick usage'
               14  LOAD_STR                 '-kick @user [Reason]'

 L. 541        16  LOAD_GLOBAL              random
               18  LOAD_METHOD              randint
               20  LOAD_CONST               0
               22  LOAD_CONST               16777215
               24  CALL_METHOD_2         2  ''

 L. 540        26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'embed'

 L. 542        32  LOAD_FAST                'ctx'
               34  LOAD_ATTR                send
               36  LOAD_STR                 'Usage to kick users:'
               38  LOAD_FAST                'embed'
               40  LOAD_CONST               ('embed',)
               42  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               44  GET_AWAITABLE    
               46  LOAD_CONST               None
               48  YIELD_FROM       
               50  POP_TOP          

 L. 543        52  LOAD_CONST               None
               54  RETURN_VALUE     
             56_0  COME_FROM             6  '6'

 L. 544        56  SETUP_FINALLY       274  'to 274'

 L. 545        58  LOAD_FAST                'member'
               60  LOAD_ATTR                guild_permissions
               62  LOAD_ATTR                manage_messages
               64  LOAD_CONST               True
               66  COMPARE_OP               is
               68  POP_JUMP_IF_FALSE    92  'to 92'

 L. 546        70  LOAD_GLOBAL              print
               72  LOAD_STR                 'trigger'
               74  CALL_FUNCTION_1       1  ''
               76  POP_TOP          

 L. 547        78  LOAD_GLOBAL              ValueError
               80  LOAD_STR                 'Moderator was attempted to kick'
               82  CALL_FUNCTION_1       1  ''
               84  RAISE_VARARGS_1       1  ''

 L. 548        86  POP_BLOCK        
               88  LOAD_CONST               None
               90  RETURN_VALUE     
             92_0  COME_FROM            68  '68'

 L. 550        92  LOAD_FAST                'member'
               94  LOAD_ATTR                kick
               96  LOAD_FAST                'reason'
               98  LOAD_CONST               ('reason',)
              100  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              102  GET_AWAITABLE    
              104  LOAD_CONST               None
              106  YIELD_FROM       
              108  POP_TOP          

 L. 551       110  LOAD_FAST                'ctx'
              112  LOAD_ATTR                send
              114  LOAD_STR                 'Kicked '
              116  LOAD_FAST                'member'
              118  LOAD_ATTR                name
              120  FORMAT_VALUE          0  ''
              122  LOAD_STR                 '#'
              124  LOAD_FAST                'member'
              126  LOAD_ATTR                discriminator
              128  FORMAT_VALUE          0  ''
              130  BUILD_STRING_4        4  ''
              132  LOAD_CONST               10
              134  LOAD_CONST               ('delete_after',)
              136  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              138  GET_AWAITABLE    
              140  LOAD_CONST               None
              142  YIELD_FROM       
              144  POP_TOP          

 L. 552       146  SETUP_FINALLY       246  'to 246'

 L. 553       148  LOAD_GLOBAL              asyncio
              150  LOAD_METHOD              sleep
              152  LOAD_CONST               10
              154  CALL_METHOD_1         1  ''
              156  GET_AWAITABLE    
              158  LOAD_CONST               None
              160  YIELD_FROM       
              162  POP_TOP          

 L. 554       164  LOAD_FAST                'ctx'
              166  LOAD_ATTR                message
              168  LOAD_METHOD              delete
              170  CALL_METHOD_0         0  ''
              172  GET_AWAITABLE    
              174  LOAD_CONST               None
              176  YIELD_FROM       
              178  POP_TOP          

 L. 555       180  LOAD_GLOBAL              asyncio
              182  LOAD_METHOD              sleep
              184  LOAD_CONST               3
              186  CALL_METHOD_1         1  ''
              188  GET_AWAITABLE    
              190  LOAD_CONST               None
              192  YIELD_FROM       
              194  POP_TOP          

 L. 556       196  LOAD_FAST                'ctx'
              198  LOAD_METHOD              trigger_typing
              200  CALL_METHOD_0         0  ''
              202  GET_AWAITABLE    
              204  LOAD_CONST               None
              206  YIELD_FROM       
              208  POP_TOP          

 L. 557       210  LOAD_GLOBAL              asyncio
              212  LOAD_METHOD              sleep
              214  LOAD_CONST               3
              216  CALL_METHOD_1         1  ''
              218  GET_AWAITABLE    
              220  LOAD_CONST               None
              222  YIELD_FROM       
              224  POP_TOP          

 L. 558       226  LOAD_FAST                'ctx'
              228  LOAD_METHOD              send

 L. 559       230  LOAD_STR                 "Oh my. What happened here? It seems we've gone back in time. What should we talk about?"

 L. 558       232  CALL_METHOD_1         1  ''
              234  GET_AWAITABLE    
              236  LOAD_CONST               None
              238  YIELD_FROM       
              240  POP_TOP          
              242  POP_BLOCK        
              244  JUMP_FORWARD        268  'to 268'
            246_0  COME_FROM_FINALLY   146  '146'

 L. 560       246  DUP_TOP          
              248  LOAD_GLOBAL              Exception
              250  COMPARE_OP               exception-match
          252_254  POP_JUMP_IF_FALSE   266  'to 266'
              256  POP_TOP          
              258  POP_TOP          
              260  POP_TOP          

 L. 561       262  POP_EXCEPT       
              264  JUMP_FORWARD        268  'to 268'
            266_0  COME_FROM           252  '252'
              266  END_FINALLY      
            268_0  COME_FROM           264  '264'
            268_1  COME_FROM           244  '244'
              268  POP_BLOCK        
          270_272  JUMP_FORWARD        572  'to 572'
            274_0  COME_FROM_FINALLY    56  '56'

 L. 562       274  DUP_TOP          
              276  LOAD_GLOBAL              Exception
              278  COMPARE_OP               exception-match
          280_282  POP_JUMP_IF_FALSE   570  'to 570'
              284  POP_TOP          
              286  POP_TOP          
              288  POP_TOP          

 L. 563       290  LOAD_FAST                'member'
              292  LOAD_ATTR                id
              294  LOAD_CONST               396241937658675206
              296  COMPARE_OP               ==
          298_300  POP_JUMP_IF_FALSE   320  'to 320'

 L. 564       302  LOAD_FAST                'ctx'
              304  LOAD_METHOD              send
              306  LOAD_STR                 'You cannot kick Joel, The bot coder <:YanWink:425913980809379850>'
              308  CALL_METHOD_1         1  ''
              310  GET_AWAITABLE    
              312  LOAD_CONST               None
              314  YIELD_FROM       
              316  POP_TOP          
              318  JUMP_FORWARD        566  'to 566'
            320_0  COME_FROM           298  '298'

 L. 565       320  LOAD_FAST                'member'
              322  LOAD_ATTR                id
              324  LOAD_CONST               135161245941628928
              326  COMPARE_OP               ==
          328_330  POP_JUMP_IF_FALSE   350  'to 350'

 L. 566       332  LOAD_FAST                'ctx'
              334  LOAD_METHOD              send
              336  LOAD_STR                 'You cannot kick our beloved YandereDev <:YanWink:425913980809379850>'
              338  CALL_METHOD_1         1  ''
              340  GET_AWAITABLE    
              342  LOAD_CONST               None
              344  YIELD_FROM       
              346  POP_TOP          
              348  JUMP_FORWARD        566  'to 566'
            350_0  COME_FROM           328  '328'

 L. 567       350  LOAD_FAST                'member'
              352  LOAD_ATTR                id
              354  LOAD_CONST               614730255672016896
              356  COMPARE_OP               ==
          358_360  POP_JUMP_IF_FALSE   380  'to 380'

 L. 568       362  LOAD_FAST                'ctx'
              364  LOAD_METHOD              send
              366  LOAD_STR                 'I cannot kick myself, <:YanWink:425913980809379850>'
              368  CALL_METHOD_1         1  ''
              370  GET_AWAITABLE    
              372  LOAD_CONST               None
              374  YIELD_FROM       
              376  POP_TOP          
              378  JUMP_FORWARD        566  'to 566'
            380_0  COME_FROM           358  '358'

 L. 569       380  LOAD_FAST                'member'
              382  LOAD_ATTR                guild_permissions
              384  LOAD_ATTR                manage_messages
              386  LOAD_CONST               True
              388  COMPARE_OP               is
          390_392  POP_JUMP_IF_FALSE   412  'to 412'

 L. 570       394  LOAD_FAST                'ctx'
              396  LOAD_METHOD              send
              398  LOAD_STR                 'You cannot kick moderators <:YanWink:425913980809379850>'
              400  CALL_METHOD_1         1  ''
              402  GET_AWAITABLE    
              404  LOAD_CONST               None
              406  YIELD_FROM       
              408  POP_TOP          
              410  JUMP_FORWARD        566  'to 566'
            412_0  COME_FROM           390  '390'

 L. 571       412  LOAD_FAST                'ctx'
              414  LOAD_ATTR                me
              416  LOAD_ATTR                guild_permissions
              418  LOAD_ATTR                kick_members
          420_422  POP_JUMP_IF_TRUE    496  'to 496'

 L. 572       424  LOAD_FAST                'ctx'
              426  LOAD_ATTR                send

 L. 573       428  LOAD_STR                 "I cannot kick that person, I don't have the correct permission or my role is too low..."

 L. 574       430  LOAD_CONST               10

 L. 572       432  LOAD_CONST               ('delete_after',)
              434  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              436  GET_AWAITABLE    
              438  LOAD_CONST               None
              440  YIELD_FROM       
              442  POP_TOP          

 L. 575       444  SETUP_FINALLY       482  'to 482'

 L. 576       446  LOAD_GLOBAL              asyncio
              448  LOAD_METHOD              sleep
              450  LOAD_CONST               10
              452  CALL_METHOD_1         1  ''
              454  GET_AWAITABLE    
              456  LOAD_CONST               None
              458  YIELD_FROM       
              460  POP_TOP          

 L. 577       462  LOAD_FAST                'ctx'
              464  LOAD_ATTR                message
              466  LOAD_METHOD              delete
              468  CALL_METHOD_0         0  ''
              470  GET_AWAITABLE    
              472  LOAD_CONST               None
              474  YIELD_FROM       
              476  POP_TOP          
              478  POP_BLOCK        
              480  JUMP_FORWARD        494  'to 494'
            482_0  COME_FROM_FINALLY   444  '444'

 L. 578       482  POP_TOP          
              484  POP_TOP          
              486  POP_TOP          

 L. 579       488  POP_EXCEPT       
              490  JUMP_FORWARD        494  'to 494'
              492  END_FINALLY      
            494_0  COME_FROM           490  '490'
            494_1  COME_FROM           480  '480'
              494  JUMP_FORWARD        566  'to 566'
            496_0  COME_FROM           420  '420'

 L. 581       496  LOAD_FAST                'ctx'
              498  LOAD_ATTR                send
              500  LOAD_STR                 'An unknown issue occured...'
              502  LOAD_CONST               10
              504  LOAD_CONST               ('delete_after',)
              506  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              508  GET_AWAITABLE    
              510  LOAD_CONST               None
              512  YIELD_FROM       
              514  POP_TOP          

 L. 582       516  SETUP_FINALLY       554  'to 554'

 L. 583       518  LOAD_GLOBAL              asyncio
              520  LOAD_METHOD              sleep
              522  LOAD_CONST               10
              524  CALL_METHOD_1         1  ''
              526  GET_AWAITABLE    
              528  LOAD_CONST               None
              530  YIELD_FROM       
              532  POP_TOP          

 L. 584       534  LOAD_FAST                'ctx'
              536  LOAD_ATTR                message
              538  LOAD_METHOD              delete
              540  CALL_METHOD_0         0  ''
              542  GET_AWAITABLE    
              544  LOAD_CONST               None
              546  YIELD_FROM       
              548  POP_TOP          
              550  POP_BLOCK        
              552  JUMP_FORWARD        566  'to 566'
            554_0  COME_FROM_FINALLY   516  '516'

 L. 585       554  POP_TOP          
              556  POP_TOP          
              558  POP_TOP          

 L. 586       560  POP_EXCEPT       
              562  JUMP_FORWARD        566  'to 566'
              564  END_FINALLY      
            566_0  COME_FROM           562  '562'
            566_1  COME_FROM           552  '552'
            566_2  COME_FROM           494  '494'
            566_3  COME_FROM           410  '410'
            566_4  COME_FROM           378  '378'
            566_5  COME_FROM           348  '348'
            566_6  COME_FROM           318  '318'
              566  POP_EXCEPT       
              568  JUMP_FORWARD        572  'to 572'
            570_0  COME_FROM           280  '280'
              570  END_FINALLY      
            572_0  COME_FROM           568  '568'
            572_1  COME_FROM           270  '270'

Parse error at or near `LOAD_CONST' instruction at offset 88


def setup(bot):
    bot.add_cog(other(bot))