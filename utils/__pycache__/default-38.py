# uncompyle6 version 3.6.6
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Users\Sohea\OneDrive\Documents\bots\midori-bot\utils\default.py
# Compiled at: 2019-12-06 13:47:56
# Size of source mod 2**32: 1930 bytes
import asyncio, json, traceback
from collections import namedtuple
import aiohttp, discord
from utils import cache

def can_send(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or 


def traceback_maker(err, advance: bool=True):
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = '```py\n{1}{0}: {2}\n```'.format(type(err).__name__, _traceback, err)
    if advance:
        return error
    return f"{type(err).__name__}: {err}"


def jsonget--- This code section failed: ---

 L.  23         0  SETUP_FINALLY        58  'to 58'

 L.  24         2  LOAD_GLOBAL              open
                4  LOAD_FAST                'file'
                6  LOAD_STR                 'utf8'
                8  LOAD_CONST               ('encoding',)
               10  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               12  SETUP_WITH           48  'to 48'
               14  STORE_FAST               'data'

 L.  25        16  LOAD_GLOBAL              json
               18  LOAD_ATTR                load
               20  LOAD_FAST                'data'
               22  LOAD_LAMBDA              '<code_object <lambda>>'
               24  LOAD_STR                 'jsonget.<locals>.<lambda>'
               26  MAKE_FUNCTION_0          ''
               28  LOAD_CONST               ('object_hook',)
               30  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               32  POP_BLOCK        
               34  ROT_TWO          
               36  BEGIN_FINALLY    
               38  WITH_CLEANUP_START
               40  WITH_CLEANUP_FINISH
               42  POP_FINALLY           0  ''
               44  POP_BLOCK        
               46  RETURN_VALUE     
             48_0  COME_FROM_WITH       12  '12'
               48  WITH_CLEANUP_START
               50  WITH_CLEANUP_FINISH
               52  END_FINALLY      
               54  POP_BLOCK        
               56  JUMP_FORWARD        112  'to 112'
             58_0  COME_FROM_FINALLY     0  '0'

 L.  26        58  DUP_TOP          
               60  LOAD_GLOBAL              AttributeError
               62  COMPARE_OP               exception-match
               64  POP_JUMP_IF_FALSE    84  'to 84'
               66  POP_TOP          
               68  POP_TOP          
               70  POP_TOP          

 L.  27        72  LOAD_GLOBAL              AttributeError
               74  LOAD_STR                 'Unknown argument'
               76  CALL_FUNCTION_1       1  ''
               78  RAISE_VARARGS_1       1  ''
               80  POP_EXCEPT       
               82  JUMP_FORWARD        112  'to 112'
             84_0  COME_FROM            64  '64'

 L.  28        84  DUP_TOP          
               86  LOAD_GLOBAL              FileNotFoundError
               88  COMPARE_OP               exception-match
               90  POP_JUMP_IF_FALSE   110  'to 110'
               92  POP_TOP          
               94  POP_TOP          
               96  POP_TOP          

 L.  29        98  LOAD_GLOBAL              FileNotFoundError
              100  LOAD_STR                 "JSON file wasn't found"
              102  CALL_FUNCTION_1       1  ''
              104  RAISE_VARARGS_1       1  ''
              106  POP_EXCEPT       
              108  JUMP_FORWARD        112  'to 112'
            110_0  COME_FROM            90  '90'
              110  END_FINALLY      
            112_0  COME_FROM           108  '108'
            112_1  COME_FROM            82  '82'
            112_2  COME_FROM            56  '56'

Parse error at or near `POP_BLOCK' instruction at offset 32


class HTTPSession(aiohttp.ClientSession):
    """HTTPSession"""

    def __init__(self, loop=None):
        super().__init__(loop=(loop or ))

    def __del__(self):
        """
        Closes the ClientSession instance
        cleanly when the instance is deleted.

        Useful for things like when the interpreter closes.

        This would be perfect if discord.py had this as well. :thinking:
        """
        if not self.closed:
            self.close()


session = HTTPSession()

@cache.async_cache()
async def query--- This code section failed: ---

 L.  57         0  LOAD_GLOBAL              getattr
                2  LOAD_GLOBAL              session
                4  LOAD_FAST                'method'
                6  LOAD_METHOD              lower
                8  CALL_METHOD_0         0  ''
               10  CALL_FUNCTION_2       2  ''
               12  LOAD_FAST                'url'
               14  BUILD_TUPLE_1         1 
               16  LOAD_FAST                'args'
               18  BUILD_TUPLE_UNPACK_WITH_CALL_2     2 
               20  LOAD_FAST                'kwargs'
               22  CALL_FUNCTION_EX_KW     1  'keyword args'
               24  BEFORE_ASYNC_WITH
               26  GET_AWAITABLE    
               28  LOAD_CONST               None
               30  YIELD_FROM       
               32  SETUP_ASYNC_WITH     72  'to 72'
               34  STORE_FAST               'res'

 L.  58        36  LOAD_GLOBAL              getattr
               38  LOAD_FAST                'res'
               40  LOAD_FAST                'res_method'
               42  CALL_FUNCTION_2       2  ''
               44  CALL_FUNCTION_0       0  ''
               46  GET_AWAITABLE    
               48  LOAD_CONST               None
               50  YIELD_FROM       
               52  POP_BLOCK        
               54  ROT_TWO          
               56  BEGIN_FINALLY    
               58  WITH_CLEANUP_START
               60  GET_AWAITABLE    
               62  LOAD_CONST               None
               64  YIELD_FROM       
               66  WITH_CLEANUP_FINISH
               68  POP_FINALLY           0  ''
               70  RETURN_VALUE     
             72_0  COME_FROM_ASYNC_WITH    32  '32'
               72  WITH_CLEANUP_START
               74  GET_AWAITABLE    
               76  LOAD_CONST               None
               78  YIELD_FROM       
               80  WITH_CLEANUP_FINISH
               82  END_FINALLY      

Parse error at or near `POP_BLOCK' instruction at offset 52


async def get(url, *args, **kwargs):
    return await query(url, 'get', *args, **kwargs)


async def post(url, *args, **kwargs):
    return await query(url, 'post', *args, **kwargs)