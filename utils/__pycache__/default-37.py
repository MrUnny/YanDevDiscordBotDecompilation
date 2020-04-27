# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: /home/joelthomson08/midori-bot/utils/default.py
# Compiled at: 2019-12-07 00:47:56
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


def jsonget(file):
    try:
        with open(file, encoding='utf8') as (data):
            return json.load(data, object_hook=(lambda d: (namedtuple('X', d.keys()))(*d.values())))
    except AttributeError:
        raise AttributeError('Unknown argument')
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")


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
async def query(url, method='get', res_method='text', *args, **kwargs):
    async with (getattr(session, method.lower()))(url, *args, **kwargs) as res:
        return await getattr(res, res_method)()


async def get(url, *args, **kwargs):
    return await query(url, 'get', *args, **kwargs)


async def post(url, *args, **kwargs):
    return await query(url, 'post', *args, **kwargs)