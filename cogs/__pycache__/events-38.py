# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\cogs\events.py
# Compiled at: 2019-12-06 13:53:28
# Size of source mod 2**32: 19358 bytes
import asyncio, re, traceback, typing, discord
from discord.ext import commands
from discord.ext.commands import errors
from utils import checks

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class events(commands.Cog):
    """events"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def status_task(self, delay: int, statuses: typing.Tuple[(discord.Activity, discord.Streaming)]) -> None:
        while True:
            for status in statuses:
                await self.bot.change_presence(activity=status)
                await asyncio.sleep(delay)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            await send_cmd_help(ctx)
        elif isinstance(err, errors.CommandInvokeError):
            err = err.original
            _traceback = traceback.format_tb(err.__traceback__)
            _traceback = ''.join(_traceback)
            error = '```py\n{2}{0}: {3}\n```'.format(type(err).__name__, ctx.message.content, _traceback, err)
            await ctx.send(f"There was an error processing the command ;-;\n{error}")
        elif isinstance(err, errors.CheckFailure):
            pass
        elif isinstance(err, errors.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown... try again in {err.retry_after:.2f} seconds.")
        elif isinstance(err, errors.CommandNotFound):
            pass

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            print(f"Command: {ctx.message.clean_content} || Member: {ctx.author}|{ctx.author.id} || Server:{ctx.guild}|{ctx.guild.id}\n-----------------")
        except AttributeError:
            print(f"Private message> {ctx.author}> {ctx.message.clean_content}")

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')
        print("I'm ready!")
        print(f"{len(set(self.bot.get_all_members()))} members!")
        self.bot.loop.create_task(self.status_task(20, checks.status_list))

    @commands.Cog.listener(name='message')
    @commands.guild_only()
    async def on_message--- This code section failed: ---

 L.  79         0  LOAD_FAST                'message'
                2  LOAD_ATTR                author
                4  LOAD_ATTR                bot
                6  POP_JUMP_IF_FALSE    12  'to 12'

 L.  80         8  LOAD_CONST               None
               10  RETURN_VALUE     
             12_0  COME_FROM             6  '6'

 L.  81        12  LOAD_FAST                'message'
               14  LOAD_ATTR                author
               16  LOAD_FAST                'self'
               18  LOAD_ATTR                bot
               20  LOAD_ATTR                user
               22  COMPARE_OP               ==
               24  POP_JUMP_IF_FALSE    30  'to 30'

 L.  82        26  LOAD_CONST               None
               28  RETURN_VALUE     
             30_0  COME_FROM            24  '24'

 L.  83        30  SETUP_FINALLY        58  'to 58'

 L.  84        32  LOAD_FAST                'message'
               34  LOAD_ATTR                author
               36  LOAD_ATTR                guild_permissions
               38  LOAD_ATTR                ban_members
               40  POP_JUMP_IF_TRUE     48  'to 48'

 L.  85        42  LOAD_CONST               True
               44  STORE_FAST               'passing'
               46  JUMP_FORWARD         54  'to 54'
             48_0  COME_FROM            40  '40'

 L.  87        48  POP_BLOCK        
               50  LOAD_CONST               None
               52  RETURN_VALUE     
             54_0  COME_FROM            46  '46'
               54  POP_BLOCK        
               56  JUMP_FORWARD         80  'to 80'
             58_0  COME_FROM_FINALLY    30  '30'

 L.  88        58  DUP_TOP          
               60  LOAD_GLOBAL              Exception
               62  COMPARE_OP               exception-match
               64  POP_JUMP_IF_FALSE    78  'to 78'
               66  POP_TOP          
               68  POP_TOP          
               70  POP_TOP          

 L.  89        72  POP_EXCEPT       
               74  LOAD_CONST               None
               76  RETURN_VALUE     
             78_0  COME_FROM            64  '64'
               78  END_FINALLY      
             80_0  COME_FROM            56  '56'

 L.  90        80  LOAD_FAST                'passing'
            82_84  POP_JUMP_IF_FALSE   474  'to 474'

 L.  92        86  LOAD_STR                 '^.{0,5}c\\s*r\\s*(e|3)\\s*(e|3)?\\s*(e|3)?\\s*p{1,2}\\s*(e|3)\\s*r\\s*,*\\s*a*w*\\s*m*\\s*a*\\s*n*\\s*'

 L.  93        88  LOAD_STR                 '^.{0,5}🇨\\s*🇷\\s*(🇪|3)\\s*(🇪|3)?\\s*🇵{1,2}\\s*(🇪|3)\\s*🇷'

 L.  94        90  LOAD_STR                 '^.{0,5}*so\\s*we\\s*(b|🅱)ac(c|k)\\s*in\\s*the\\s*mine'

 L.  95        92  LOAD_STR                 '^.{0,5}*got\\s*our\\s*pickaxe\\s*swinging\\s*from\\s*side\\s*to\\s*side'

 L.  96        94  LOAD_STR                 '^.{0,5}side to side'

 L.  97        96  LOAD_STR                 '^.{0,5}i\\s*used\\s*to\\s*rule\\s*the\\s*world'

 L.  91        98  BUILD_LIST_6          6 
              100  STORE_FAST               'regexes'

 L.  99       102  LOAD_CONST               False
              104  STORE_FAST               'match'

 L. 100       106  LOAD_FAST                'regexes'
              108  GET_ITER         
              110  FOR_ITER            186  'to 186'
              112  STORE_FAST               'regex'

 L. 101       114  SETUP_FINALLY       164  'to 164'

 L. 102       116  LOAD_GLOBAL              re
              118  LOAD_ATTR                search
              120  LOAD_FAST                'regex'
              122  LOAD_FAST                'message'
              124  LOAD_ATTR                content
              126  LOAD_GLOBAL              re
              128  LOAD_ATTR                IGNORECASE
              130  LOAD_CONST               ('flags',)
              132  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              134  POP_JUMP_IF_FALSE   160  'to 160'

 L. 103       136  LOAD_STR                 'hugcreeper'
              138  LOAD_FAST                'message'
              140  LOAD_ATTR                content
              142  LOAD_METHOD              lower
              144  CALL_METHOD_0         0  ''
              146  COMPARE_OP               in
              148  POP_JUMP_IF_FALSE   156  'to 156'

 L. 104       150  LOAD_CONST               False
              152  STORE_FAST               'match'
              154  JUMP_FORWARD        160  'to 160'
            156_0  COME_FROM           148  '148'

 L. 106       156  LOAD_CONST               True
              158  STORE_FAST               'match'
            160_0  COME_FROM           154  '154'
            160_1  COME_FROM           134  '134'
              160  POP_BLOCK        
              162  JUMP_BACK           110  'to 110'
            164_0  COME_FROM_FINALLY   114  '114'

 L. 107       164  DUP_TOP          
              166  LOAD_GLOBAL              Exception
              168  COMPARE_OP               exception-match
              170  POP_JUMP_IF_FALSE   182  'to 182'
              172  POP_TOP          
              174  POP_TOP          
              176  POP_TOP          

 L. 108       178  POP_EXCEPT       
              180  JUMP_BACK           110  'to 110'
            182_0  COME_FROM           170  '170'
              182  END_FINALLY      
              184  JUMP_BACK           110  'to 110'

 L. 109       186  LOAD_FAST                'match'
          188_190  POP_JUMP_IF_FALSE   468  'to 468'

 L. 110       192  SETUP_FINALLY       262  'to 262'

 L. 111       194  LOAD_FAST                'message'
              196  LOAD_METHOD              delete
              198  CALL_METHOD_0         0  ''
              200  GET_AWAITABLE    
              202  LOAD_CONST               None
              204  YIELD_FROM       
              206  POP_TOP          

 L. 112       208  LOAD_STR                 ':warning: Deleted "Creeper" meme from '
              210  STORE_FAST               'Warn'

 L. 113       212  LOAD_STR                 '**'
              214  LOAD_FAST                'message'
              216  LOAD_ATTR                author
              218  LOAD_ATTR                name
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 '**#'
              224  LOAD_FAST                'message'
              226  LOAD_ATTR                author
              228  LOAD_ATTR                discriminator
              230  FORMAT_VALUE          0  ''
              232  LOAD_STR                 ' ('
              234  LOAD_FAST                'message'
              236  LOAD_ATTR                author
              238  LOAD_ATTR                id
              240  FORMAT_VALUE          0  ''
              242  LOAD_STR                 ') in <#'
              244  LOAD_FAST                'message'
              246  LOAD_ATTR                channel
              248  LOAD_ATTR                id
              250  FORMAT_VALUE          0  ''
              252  LOAD_STR                 '>.'
              254  BUILD_STRING_9        9  ''
              256  POP_TOP          
              258  POP_BLOCK        
              260  JUMP_FORWARD        334  'to 334'
            262_0  COME_FROM_FINALLY   192  '192'

 L. 114       262  DUP_TOP          
              264  LOAD_GLOBAL              Exception
              266  COMPARE_OP               exception-match
          268_270  POP_JUMP_IF_FALSE   332  'to 332'
              272  POP_TOP          
              274  POP_TOP          
              276  POP_TOP          

 L. 115       278  LOAD_STR                 ':warning: Detected "Creeper" meme from '
              280  STORE_FAST               'Warn'

 L. 116       282  LOAD_STR                 '**'
              284  LOAD_FAST                'message'
              286  LOAD_ATTR                author
              288  LOAD_ATTR                name
              290  FORMAT_VALUE          0  ''
              292  LOAD_STR                 '**#'
              294  LOAD_FAST                'message'
              296  LOAD_ATTR                author
              298  LOAD_ATTR                discriminator
              300  FORMAT_VALUE          0  ''
              302  LOAD_STR                 ' ('
              304  LOAD_FAST                'message'
              306  LOAD_ATTR                author
              308  LOAD_ATTR                id
              310  FORMAT_VALUE          0  ''
              312  LOAD_STR                 ') in <#'
              314  LOAD_FAST                'message'
              316  LOAD_ATTR                channel
              318  LOAD_ATTR                id
              320  FORMAT_VALUE          0  ''
              322  LOAD_STR                 '>.'
              324  BUILD_STRING_9        9  ''
              326  POP_TOP          
              328  POP_EXCEPT       
              330  JUMP_FORWARD        334  'to 334'
            332_0  COME_FROM           268  '268'
              332  END_FINALLY      
            334_0  COME_FROM           330  '330'
            334_1  COME_FROM           260  '260'

 L. 117       334  LOAD_FAST                'self'
              336  LOAD_ATTR                bot
              338  LOAD_METHOD              get_channel
              340  LOAD_CONST               615882185190408194
              342  CALL_METHOD_1         1  ''
              344  STORE_FAST               'channel'

 L. 118       346  LOAD_FAST                'channel'
              348  LOAD_ATTR                send

 L. 119       350  LOAD_FAST                'Warn'
              352  FORMAT_VALUE          0  ''

 L. 120       354  LOAD_GLOBAL              discord
              356  LOAD_METHOD              Embed
              358  CALL_METHOD_0         0  ''
              360  LOAD_METHOD              from_dict

 L. 122       362  LOAD_STR                 'Message Content:'

 L. 123       364  LOAD_FAST                'message'
              366  LOAD_ATTR                content

 L. 124       368  LOAD_CONST               16737380

 L. 121       370  LOAD_CONST               ('title', 'description', 'color')
              372  BUILD_CONST_KEY_MAP_3     3 

 L. 120       374  CALL_METHOD_1         1  ''

 L. 118       376  LOAD_CONST               ('content', 'embed')
              378  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              380  GET_AWAITABLE    
              382  LOAD_CONST               None
              384  YIELD_FROM       
              386  POP_TOP          

 L. 128       388  SETUP_FINALLY       412  'to 412'

 L. 129       390  LOAD_FAST                'message'
              392  LOAD_ATTR                author
              394  LOAD_METHOD              send
              396  LOAD_STR                 'Please don\'t do that "Creeper" meme. It\'s so spammy that even **I\'m** annoyed by it!'
              398  CALL_METHOD_1         1  ''
              400  GET_AWAITABLE    
              402  LOAD_CONST               None
              404  YIELD_FROM       
              406  POP_TOP          
              408  POP_BLOCK        
              410  JUMP_FORWARD        466  'to 466'
            412_0  COME_FROM_FINALLY   388  '388'

 L. 131       412  DUP_TOP          
              414  LOAD_GLOBAL              Exception
              416  COMPARE_OP               exception-match
          418_420  POP_JUMP_IF_FALSE   464  'to 464'
              422  POP_TOP          
              424  POP_TOP          
              426  POP_TOP          

 L. 132       428  LOAD_FAST                'message'
              430  LOAD_ATTR                channel
              432  LOAD_ATTR                send
              434  LOAD_FAST                'message'
              436  LOAD_ATTR                author
              438  LOAD_ATTR                mention
              440  FORMAT_VALUE          0  ''
              442  LOAD_STR                 ', please don\'t do that "Creeper" meme. It\'s so spammy that even **I\'m** annoyed by it!'
              444  BUILD_STRING_2        2  ''

 L. 134       446  LOAD_CONST               15

 L. 132       448  LOAD_CONST               ('delete_after',)
              450  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              452  GET_AWAITABLE    
              454  LOAD_CONST               None
              456  YIELD_FROM       
              458  POP_TOP          
              460  POP_EXCEPT       
              462  JUMP_FORWARD        466  'to 466'
            464_0  COME_FROM           418  '418'
              464  END_FINALLY      
            466_0  COME_FROM           462  '462'
            466_1  COME_FROM           410  '410'
              466  JUMP_FORWARD        472  'to 472'
            468_0  COME_FROM           188  '188'

 L. 136       468  LOAD_CONST               None
              470  RETURN_VALUE     
            472_0  COME_FROM           466  '466'
              472  JUMP_FORWARD        478  'to 478'
            474_0  COME_FROM            82  '82'

 L. 138       474  LOAD_CONST               None
              476  RETURN_VALUE     
            478_0  COME_FROM           472  '472'

Parse error at or near `LOAD_CONST' instruction at offset 50

    @commands.Cog.listener(name='advert')
    async def on_message--- This code section failed: ---

 L. 142         0  LOAD_FAST                'advert'
                2  LOAD_ATTR                author
                4  LOAD_ATTR                bot
                6  POP_JUMP_IF_FALSE    12  'to 12'

 L. 143         8  LOAD_CONST               None
               10  RETURN_VALUE     
             12_0  COME_FROM             6  '6'

 L. 144        12  LOAD_FAST                'advert'
               14  LOAD_ATTR                author
               16  LOAD_FAST                'self'
               18  LOAD_ATTR                bot
               20  LOAD_ATTR                user
               22  COMPARE_OP               ==
               24  POP_JUMP_IF_FALSE    30  'to 30'

 L. 145        26  LOAD_CONST               None
               28  RETURN_VALUE     
             30_0  COME_FROM            24  '24'

 L. 146        30  SETUP_FINALLY        52  'to 52'

 L. 147        32  LOAD_FAST                'advert'
               34  LOAD_ATTR                author
               36  LOAD_ATTR                guild_permissions
               38  LOAD_ATTR                ban_members
               40  POP_JUMP_IF_FALSE    48  'to 48'

 L. 148        42  POP_BLOCK        
               44  LOAD_CONST               None
               46  RETURN_VALUE     
             48_0  COME_FROM            40  '40'
               48  POP_BLOCK        
               50  JUMP_FORWARD         72  'to 72'
             52_0  COME_FROM_FINALLY    30  '30'

 L. 149        52  DUP_TOP          
               54  LOAD_GLOBAL              Exception
               56  COMPARE_OP               exception-match
               58  POP_JUMP_IF_FALSE    70  'to 70'
               60  POP_TOP          
               62  POP_TOP          
               64  POP_TOP          

 L. 150        66  POP_EXCEPT       
               68  JUMP_FORWARD         72  'to 72'
             70_0  COME_FROM            58  '58'
               70  END_FINALLY      
             72_0  COME_FROM            68  '68'
             72_1  COME_FROM            50  '50'

 L. 151        72  LOAD_CONST               False
               74  STORE_FAST               'AD'

 L. 152        76  LOAD_STR                 'discord.gg/'
               78  LOAD_FAST                'advert'
               80  LOAD_ATTR                content
               82  LOAD_METHOD              lower
               84  CALL_METHOD_0         0  ''
               86  COMPARE_OP               in
               88  POP_JUMP_IF_FALSE    96  'to 96'

 L. 153        90  LOAD_CONST               True
               92  STORE_FAST               'AD'
               94  JUMP_FORWARD        114  'to 114'
             96_0  COME_FROM            88  '88'

 L. 154        96  LOAD_STR                 'discord gg/'
               98  LOAD_FAST                'advert'
              100  LOAD_ATTR                content
              102  LOAD_METHOD              lower
              104  CALL_METHOD_0         0  ''
              106  COMPARE_OP               in
              108  POP_JUMP_IF_FALSE   114  'to 114'

 L. 155       110  LOAD_CONST               True
              112  STORE_FAST               'AD'
            114_0  COME_FROM           108  '108'
            114_1  COME_FROM            94  '94'

 L. 156       114  LOAD_FAST                'AD'
          116_118  POP_JUMP_IF_FALSE   388  'to 388'

 L. 157       120  SETUP_FINALLY       186  'to 186'

 L. 158       122  LOAD_FAST                'advert'
              124  LOAD_METHOD              delete
              126  CALL_METHOD_0         0  ''
              128  GET_AWAITABLE    
              130  LOAD_CONST               None
              132  YIELD_FROM       
              134  POP_TOP          

 L. 159       136  LOAD_STR                 ':warning: Deleted server advertisement from **'
              138  LOAD_FAST                'advert'
              140  LOAD_ATTR                author
              142  LOAD_ATTR                name
              144  FORMAT_VALUE          0  ''
              146  LOAD_STR                 '**#'
              148  LOAD_FAST                'advert'
              150  LOAD_ATTR                author
              152  LOAD_ATTR                discriminator
              154  FORMAT_VALUE          0  ''
              156  LOAD_STR                 ' ('
              158  LOAD_FAST                'advert'
              160  LOAD_ATTR                author
              162  LOAD_ATTR                id
              164  FORMAT_VALUE          0  ''
              166  LOAD_STR                 ') in <#'
              168  LOAD_FAST                'advert'
              170  LOAD_ATTR                channel
              172  LOAD_ATTR                id
              174  FORMAT_VALUE          0  ''
              176  LOAD_STR                 '>.'
              178  BUILD_STRING_9        9  ''
              180  STORE_FAST               'Warn'
              182  POP_BLOCK        
              184  JUMP_FORWARD        252  'to 252'
            186_0  COME_FROM_FINALLY   120  '120'

 L. 160       186  DUP_TOP          
              188  LOAD_GLOBAL              Exception
              190  COMPARE_OP               exception-match
              192  POP_JUMP_IF_FALSE   250  'to 250'
              194  POP_TOP          
              196  POP_TOP          
              198  POP_TOP          

 L. 161       200  LOAD_STR                 ':warning: Detected server advertisement from **'
              202  LOAD_FAST                'advert'
              204  LOAD_ATTR                author
              206  LOAD_ATTR                name
              208  FORMAT_VALUE          0  ''
              210  LOAD_STR                 '**#'
              212  LOAD_FAST                'advert'
              214  LOAD_ATTR                author
              216  LOAD_ATTR                discriminator
              218  FORMAT_VALUE          0  ''
              220  LOAD_STR                 ' ('
              222  LOAD_FAST                'advert'
              224  LOAD_ATTR                author
              226  LOAD_ATTR                id
              228  FORMAT_VALUE          0  ''
              230  LOAD_STR                 ') in <#'
              232  LOAD_FAST                'advert'
              234  LOAD_ATTR                channel
              236  LOAD_ATTR                id
              238  FORMAT_VALUE          0  ''
              240  LOAD_STR                 '>.'
              242  BUILD_STRING_9        9  ''
              244  STORE_FAST               'Warn'
              246  POP_EXCEPT       
              248  JUMP_FORWARD        252  'to 252'
            250_0  COME_FROM           192  '192'
              250  END_FINALLY      
            252_0  COME_FROM           248  '248'
            252_1  COME_FROM           184  '184'

 L. 162       252  LOAD_FAST                'self'
              254  LOAD_ATTR                bot
              256  LOAD_METHOD              get_channel
              258  LOAD_CONST               647565593649610772
              260  CALL_METHOD_1         1  ''
              262  STORE_FAST               'channel'

 L. 163       264  LOAD_FAST                'channel'
              266  LOAD_ATTR                send

 L. 164       268  LOAD_FAST                'Warn'
              270  FORMAT_VALUE          0  ''

 L. 165       272  LOAD_GLOBAL              discord
              274  LOAD_METHOD              Embed
              276  CALL_METHOD_0         0  ''
              278  LOAD_METHOD              from_dict

 L. 167       280  LOAD_STR                 'Message Content:'

 L. 168       282  LOAD_FAST                'advert'
              284  LOAD_ATTR                content

 L. 169       286  LOAD_CONST               16737380

 L. 166       288  LOAD_CONST               ('title', 'description', 'color')
              290  BUILD_CONST_KEY_MAP_3     3 

 L. 165       292  CALL_METHOD_1         1  ''

 L. 163       294  LOAD_CONST               ('content', 'embed')
              296  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              298  GET_AWAITABLE    
              300  LOAD_CONST               None
              302  YIELD_FROM       
              304  POP_TOP          

 L. 173       306  SETUP_FINALLY       330  'to 330'

 L. 174       308  LOAD_FAST                'advert'
              310  LOAD_ATTR                author
              312  LOAD_METHOD              send
              314  LOAD_STR                 "Hey! The rules say you can't advertise Discord servers here. If you want an invite link to this server, please use the `!invite` command instead."
              316  CALL_METHOD_1         1  ''
              318  GET_AWAITABLE    
              320  LOAD_CONST               None
              322  YIELD_FROM       
              324  POP_TOP          
              326  POP_BLOCK        
              328  JUMP_FORWARD        386  'to 386'
            330_0  COME_FROM_FINALLY   306  '306'

 L. 177       330  DUP_TOP          
              332  LOAD_GLOBAL              Exception
              334  COMPARE_OP               exception-match
          336_338  POP_JUMP_IF_FALSE   384  'to 384'
              340  POP_TOP          
              342  POP_TOP          
              344  POP_TOP          

 L. 178       346  LOAD_FAST                'advert'
              348  LOAD_ATTR                channel
              350  LOAD_ATTR                send
              352  LOAD_STR                 'Hey, '
              354  LOAD_FAST                'advert'
              356  LOAD_ATTR                author
              358  LOAD_ATTR                mention
              360  FORMAT_VALUE          0  ''
              362  LOAD_STR                 "! The rules say you can't advertise Discord servers here. If you want an invite link to this server, please use the `!invite` command instead."
              364  BUILD_STRING_3        3  ''

 L. 180       366  LOAD_CONST               15

 L. 178       368  LOAD_CONST               ('delete_after',)
              370  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              372  GET_AWAITABLE    
              374  LOAD_CONST               None
              376  YIELD_FROM       
              378  POP_TOP          
              380  POP_EXCEPT       
              382  JUMP_FORWARD        386  'to 386'
            384_0  COME_FROM           336  '336'
              384  END_FINALLY      
            386_0  COME_FROM           382  '382'
            386_1  COME_FROM           328  '328'
              386  JUMP_FORWARD        392  'to 392'
            388_0  COME_FROM           116  '116'

 L. 182       388  LOAD_CONST               None
              390  RETURN_VALUE     
            392_0  COME_FROM           386  '386'

Parse error at or near `LOAD_CONST' instruction at offset 44

    @commands.Cog.listener(name='message2')
    async def on_message--- This code section failed: ---

 L. 186         0  LOAD_FAST                'message2'
                2  LOAD_ATTR                author
                4  LOAD_ATTR                bot
                6  POP_JUMP_IF_FALSE    12  'to 12'

 L. 187         8  LOAD_CONST               None
               10  RETURN_VALUE     
             12_0  COME_FROM             6  '6'

 L. 188        12  LOAD_FAST                'message2'
               14  LOAD_ATTR                author
               16  LOAD_FAST                'self'
               18  LOAD_ATTR                bot
               20  LOAD_ATTR                user
               22  COMPARE_OP               ==
               24  POP_JUMP_IF_FALSE    30  'to 30'

 L. 189        26  LOAD_CONST               None
               28  RETURN_VALUE     
             30_0  COME_FROM            24  '24'

 L. 190        30  SETUP_FINALLY        52  'to 52'

 L. 191        32  LOAD_FAST                'message2'
               34  LOAD_ATTR                author
               36  LOAD_ATTR                guild_permissions
               38  LOAD_ATTR                ban_members
               40  POP_JUMP_IF_FALSE    48  'to 48'

 L. 192        42  POP_BLOCK        
               44  LOAD_CONST               None
               46  RETURN_VALUE     
             48_0  COME_FROM            40  '40'
               48  POP_BLOCK        
               50  JUMP_FORWARD         74  'to 74'
             52_0  COME_FROM_FINALLY    30  '30'

 L. 193        52  DUP_TOP          
               54  LOAD_GLOBAL              Exception
               56  COMPARE_OP               exception-match
               58  POP_JUMP_IF_FALSE    72  'to 72'
               60  POP_TOP          
               62  POP_TOP          
               64  POP_TOP          

 L. 194        66  POP_EXCEPT       
               68  LOAD_CONST               None
               70  RETURN_VALUE     
             72_0  COME_FROM            58  '58'
               72  END_FINALLY      
             74_0  COME_FROM            50  '50'

 L. 195        74  LOAD_CONST               False
               76  STORE_FAST               'oofer'

 L. 196        78  LOAD_STR                 'oof'
               80  LOAD_FAST                'message2'
               82  LOAD_ATTR                content
               84  LOAD_METHOD              lower
               86  CALL_METHOD_0         0  ''
               88  COMPARE_OP               ==
               90  POP_JUMP_IF_FALSE    98  'to 98'

 L. 197        92  LOAD_CONST               True
               94  STORE_FAST               'oofer'
               96  JUMP_FORWARD        156  'to 156'
             98_0  COME_FROM            90  '90'

 L. 198        98  LOAD_STR                 'oof.'
              100  LOAD_FAST                'message2'
              102  LOAD_ATTR                content
              104  LOAD_METHOD              lower
              106  CALL_METHOD_0         0  ''
              108  COMPARE_OP               ==
              110  POP_JUMP_IF_FALSE   118  'to 118'

 L. 199       112  LOAD_CONST               True
              114  STORE_FAST               'oofer'
              116  JUMP_FORWARD        156  'to 156'
            118_0  COME_FROM           110  '110'

 L. 200       118  LOAD_STR                 'oof!'
              120  LOAD_FAST                'message2'
              122  LOAD_ATTR                content
              124  LOAD_METHOD              lower
              126  CALL_METHOD_0         0  ''
              128  COMPARE_OP               ==
              130  POP_JUMP_IF_FALSE   138  'to 138'

 L. 201       132  LOAD_CONST               True
              134  STORE_FAST               'oofer'
              136  JUMP_FORWARD        156  'to 156'
            138_0  COME_FROM           130  '130'

 L. 202       138  LOAD_STR                 'oof-'
              140  LOAD_FAST                'message2'
              142  LOAD_ATTR                content
              144  LOAD_METHOD              lower
              146  CALL_METHOD_0         0  ''
              148  COMPARE_OP               ==
              150  POP_JUMP_IF_FALSE   156  'to 156'

 L. 203       152  LOAD_CONST               True
              154  STORE_FAST               'oofer'
            156_0  COME_FROM           150  '150'
            156_1  COME_FROM           136  '136'
            156_2  COME_FROM           116  '116'
            156_3  COME_FROM            96  '96'

 L. 204       156  LOAD_FAST                'oofer'
          158_160  POP_JUMP_IF_FALSE   430  'to 430'

 L. 205       162  SETUP_FINALLY       228  'to 228'

 L. 206       164  LOAD_FAST                'message2'
              166  LOAD_METHOD              delete
              168  CALL_METHOD_0         0  ''
              170  GET_AWAITABLE    
              172  LOAD_CONST               None
              174  YIELD_FROM       
              176  POP_TOP          

 L. 207       178  LOAD_STR                 ':warning: Deleted "oof" message from **'
              180  LOAD_FAST                'message2'
              182  LOAD_ATTR                author
              184  LOAD_ATTR                name
              186  FORMAT_VALUE          0  ''
              188  LOAD_STR                 '**#'
              190  LOAD_FAST                'message2'
              192  LOAD_ATTR                author
              194  LOAD_ATTR                discriminator
              196  FORMAT_VALUE          0  ''
              198  LOAD_STR                 ' ('
              200  LOAD_FAST                'message2'
              202  LOAD_ATTR                author
              204  LOAD_ATTR                id
              206  FORMAT_VALUE          0  ''
              208  LOAD_STR                 ') in <#'
              210  LOAD_FAST                'message2'
              212  LOAD_ATTR                channel
              214  LOAD_ATTR                id
              216  FORMAT_VALUE          0  ''
              218  LOAD_STR                 '>.'
              220  BUILD_STRING_9        9  ''
              222  STORE_FAST               'Warn'
              224  POP_BLOCK        
              226  JUMP_FORWARD        296  'to 296'
            228_0  COME_FROM_FINALLY   162  '162'

 L. 208       228  DUP_TOP          
              230  LOAD_GLOBAL              Exception
              232  COMPARE_OP               exception-match
          234_236  POP_JUMP_IF_FALSE   294  'to 294'
              238  POP_TOP          
              240  POP_TOP          
              242  POP_TOP          

 L. 209       244  LOAD_STR                 ':warning: Detected "oof" message from **'
              246  LOAD_FAST                'message2'
              248  LOAD_ATTR                author
              250  LOAD_ATTR                name
              252  FORMAT_VALUE          0  ''
              254  LOAD_STR                 '**#'
              256  LOAD_FAST                'message2'
              258  LOAD_ATTR                author
              260  LOAD_ATTR                discriminator
              262  FORMAT_VALUE          0  ''
              264  LOAD_STR                 ' ('
              266  LOAD_FAST                'message2'
              268  LOAD_ATTR                author
              270  LOAD_ATTR                id
              272  FORMAT_VALUE          0  ''
              274  LOAD_STR                 ') in <#'
              276  LOAD_FAST                'message2'
              278  LOAD_ATTR                channel
              280  LOAD_ATTR                id
              282  FORMAT_VALUE          0  ''
              284  LOAD_STR                 '>.'
              286  BUILD_STRING_9        9  ''
              288  STORE_FAST               'Warn'
              290  POP_EXCEPT       
              292  JUMP_FORWARD        296  'to 296'
            294_0  COME_FROM           234  '234'
              294  END_FINALLY      
            296_0  COME_FROM           292  '292'
            296_1  COME_FROM           226  '226'

 L. 210       296  LOAD_FAST                'self'
              298  LOAD_ATTR                bot
              300  LOAD_METHOD              get_channel
              302  LOAD_CONST               615882185190408194
              304  CALL_METHOD_1         1  ''
              306  STORE_FAST               'channel'

 L. 211       308  LOAD_FAST                'channel'
              310  LOAD_ATTR                send

 L. 212       312  LOAD_FAST                'Warn'
              314  FORMAT_VALUE          0  ''

 L. 213       316  LOAD_GLOBAL              discord
              318  LOAD_METHOD              Embed
              320  CALL_METHOD_0         0  ''
              322  LOAD_METHOD              from_dict

 L. 215       324  LOAD_STR                 'Message Content:'

 L. 216       326  LOAD_FAST                'message2'
              328  LOAD_ATTR                content

 L. 217       330  LOAD_CONST               16737380

 L. 214       332  LOAD_CONST               ('title', 'description', 'color')
              334  BUILD_CONST_KEY_MAP_3     3 

 L. 213       336  CALL_METHOD_1         1  ''

 L. 211       338  LOAD_CONST               ('content', 'embed')
              340  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              342  GET_AWAITABLE    
              344  LOAD_CONST               None
              346  YIELD_FROM       
              348  POP_TOP          

 L. 221       350  SETUP_FINALLY       374  'to 374'

 L. 222       352  LOAD_FAST                'message2'
              354  LOAD_ATTR                author
              356  LOAD_METHOD              send

 L. 223       358  LOAD_STR                 'Non-words like "bruh," "oof," "oop," "rip," "ew," "I-," and "f" don\'t contribute anything meaningful to discussions and are no different from spam. Please don\'t fill the chat with messages like these.'

 L. 222       360  CALL_METHOD_1         1  ''
              362  GET_AWAITABLE    
              364  LOAD_CONST               None
              366  YIELD_FROM       
              368  POP_TOP          
              370  POP_BLOCK        
              372  JUMP_FORWARD        428  'to 428'
            374_0  COME_FROM_FINALLY   350  '350'

 L. 226       374  DUP_TOP          
              376  LOAD_GLOBAL              Exception
              378  COMPARE_OP               exception-match
          380_382  POP_JUMP_IF_FALSE   426  'to 426'
              384  POP_TOP          
              386  POP_TOP          
              388  POP_TOP          

 L. 227       390  LOAD_FAST                'message2'
              392  LOAD_ATTR                channel
              394  LOAD_ATTR                send

 L. 228       396  LOAD_FAST                'message2'
              398  LOAD_ATTR                author
              400  LOAD_ATTR                mention
              402  FORMAT_VALUE          0  ''
              404  LOAD_STR                 ', non-words like "bruh," "oof," "oop," "rip," "ew," "I-," and "f" don\'t contribute anything meaningful to discussions and are no different from spam. Please don\'t fill the chat with messages like these.'
              406  BUILD_STRING_2        2  ''

 L. 230       408  LOAD_CONST               15

 L. 227       410  LOAD_CONST               ('delete_after',)
              412  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              414  GET_AWAITABLE    
              416  LOAD_CONST               None
              418  YIELD_FROM       
              420  POP_TOP          
              422  POP_EXCEPT       
              424  JUMP_FORWARD        428  'to 428'
            426_0  COME_FROM           380  '380'
              426  END_FINALLY      
            428_0  COME_FROM           424  '424'
            428_1  COME_FROM           372  '372'
              428  JUMP_FORWARD        434  'to 434'
            430_0  COME_FROM           158  '158'

 L. 232       430  LOAD_CONST               None
              432  RETURN_VALUE     
            434_0  COME_FROM           428  '428'

Parse error at or near `LOAD_CONST' instruction at offset 44

    @commands.Cog.listener(name='easteregg')
    async def on_message(self, easteregg):
        if easteregg.content.startswith('-'):
            return
            if 'background' in easteregg.content.lower():
                if easteregg.author.id == 135161245941628928:
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(3)
                    await easteregg.channel.send('YandereDev��? YandereDev��? <:MidoriInsane:618333166020591637>')
                    await asyncio.sleep(0.5)
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(3)
                    await easteregg.channel.send('Background decoration��? Background decoration��?')
                    await asyncio.sleep(0.5)
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(3)
                    await easteregg.channel.send('Kill��? Kill��? Kill��?')
            if 'hatch with ninja' in easteregg.content.lower():
                if easteregg.author.id == 187625954858893322:
                    await asyncio.sleep(3)
                    await easteregg.channel.trigger_typing()
                    await asyncio.sleep(6)
                    await easteregg.channel.send('Good night, Ninja and Penpen. <:hugsayori:586518199902666753><:HugKOSMOS:586518199114268692>')
            if ':SayoriSleep:' in easteregg.content:
                if easteregg.author.id == 419863495866056704:
                    await easteregg.add_reaction('<:hugsayori:586518199902666753>')
            if ':SnugKOSMOS:' in easteregg.content:
                if easteregg.author.id == 187625954858893322:
                    await easteregg.add_reaction('<:HugKOSMOS:586518199114268692>')
            if ':yandComfy:' in easteregg.content and easteregg.author.id == 135161245941628928:
                await easteregg.add_reaction('<:YanPet:619472223115280385>')
        else:
            return

    @commands.Cog.listener(name='pouty')
    async def on_message(self, pouty):
        if ':YanPout:' in pouty.content:
            if pouty.author.id == 287417691332149248:
                await pouty.add_reaction('<a:YanNomming:614465108168671241>')
        else:
            if ':catmanager:' in pouty.content:
                if pouty.author.id == 287417691332149248:
                    await pouty.add_reaction('<a:YanNomming:614465108168671241>')
            if ':dolfinpout:' in pouty.content and pouty.author.id == 287417691332149248:
                await pouty.add_reaction('<a:YanNomming:614465108168671241>')

    @commands.Cog.listener(name='ownerping')
    async def on_message(self, ownerping):
        ping = False
        if '<@396241937658675206>' in ownerping.content.lower():
            if ownerping.author.id == 396241937658675206:
                return
            ping = True
        elif ping:
            Warn = f":warning: Detected ping from **{ownerping.author.name}**#{ownerping.author.discriminator} ({ownerping.author.id}) in <#{ownerping.channel.id}>."
            channel = self.bot.get_channel(639275263716229120)
            await channel.send(content=(f"{Warn}"),
              embed=(discord.Embed().from_dict({'title':'Message Content:', 
             'description':ownerping.content, 
             'color':16737380})))
        else:
            return

    @commands.Cog.listener(name='mention')
    async def on_message(self, mention):
        if mention.content.startswith('<@614730255672016896>'):
            if 'help' in mention.content.lower():
                await asyncio.sleep(1)
                await mention.channel.trigger_typing()
                await asyncio.sleep(1)
                HelpDM = await mention.channel.send('Sending...')
                embed = discord.Embed(title='**Help menu!\nMy available commands!**',
                  description='approve - Approve a bug (only usable in bug approval channel, currently disabled)baka - B–Baka! <:OsaPout:585710064661299220>\nbug - YandereDev, YandereDev! I found a bug!\ndeny <Bug ID> - Deny a bug (only usable in bug approval channel, currently disabled)\nhelp <Bug ID> - Show this help message\nhug [@user] - Hug someone, or get a hug from me! <:HugMidori:586518197642067978>\nneko - Get a neko, nya~!\nkiss [@user] - Kiss anyone you want~ or do I have to kiss you? <:YanSmooch:585576522371432461>\nnormie [@user] - Find out how much of a filthy normie someone is\npat [@user] - Pet someone, or get petted by me (-pet is an alias)\nping - Ping me!\npoke [@user] - Poke someone, or get poked\nreport [Report] - Report a bug about the game\nsanity [@user] - Let me judge how sane you are\nslap [@user] - Slap someone��? or get slapped!\nsuggest [Suggestion] - Suggest a command or feature (for me, not for the game) [CURRENTLY DISABLED!]\nwaifu [Waifu name] - Get a waifu (requested by YandereDev, -w is an alias, 15-second cooldown)!\ncuddle [@user] -  Huggles and cuddles for that person or for you <:HugMidori:586518197642067978>\n8ball [Question] - Ask the magic 8ball a question!\ntickle [@user] - Tickle anyone, or I will tickle you!\nfeed [@user] - Feed a user, or I can feed you~\n**NOTE: Most commands take about 20 seconds to cool down!**')
                if mention.author.guild_permissions.manage_messages:
                    embed.add_field(name='Moderator commands:',
                      value="purge [NUMBER] - Purge the chat (Requires ability to delete messages)\n                              nickname [name] (Leave blank to remove) - Rename the bot the easier way (Alias is -nick)\n                              announcetwitch - Announce dev's twitch ONLY if mee6 isn't working.\n                              warn <@user> <reason> - Warn a user, the logs get located to a logs channel\n                              kick <@user> [reason] - Kick a user, Experimental.\n                              ban <@user> [reason] - Ban a user, Experimental.\n                              These commands are only visible to server moderators.")
                embed.add_field(name='Credits:',
                  value='<@396241937658675206> *(Bot owner/main coder)*\n                          onceler#2919 *(Assisting with getting statuses and a few other things to work)*\n                          iSoheabM#5757 *(Assisting with commands)*\n                          <@482943210637754378> *(Helping me get Samus images for the -waifu command)*\n                          HarutoHiroki#4000 *(Helping me get Miku, Megumin, and Zero Two images for the -waifu command)*\n                          <@523579776749928449> *(Hosting me on a fast, stable server)*\n                          <@104632038425903104> *(Proofreading and other writing)*\n                          <@135161245941628928> *(Being the best game developer ever and giving me his approval)*\n                          <@533473096028389406> *(Giving me a few Yuri (DDLC) waifu pics)*\n                          <@197926334180229121> *(Giving me some spank gifs)*\n                          [Click here](https://www.youtube.com/watch?v=dQw4w9WgXcQ) for more information!')
                embed.add_field(name='Donations!',
                  value='I am not asking for donations at all, but any coin is appreciated,                      Non of this will go towards my own needs, this will go to the person that hosts my bot.\n                     There is no link available right now, so hold all your coins for yourself! <:YanDerp:591048226719924294>')
                embed.set_footer(text='Midori Bot',
                  icon_url=self.bot.user.avatar_url_as(format='png'))
                try:
                    await mention.author.send(embed=embed)
                    await HelpDM.edit(content='Sent! Check your DMs!')
                except Exception:
                    await HelpDM.edit(content="Hmm. I can't send you a DM. \\Try checking your settings to make sure DMs are open, and make sure you didn't block me!")


def setup(bot):
    bot.add_cog(events(bot))