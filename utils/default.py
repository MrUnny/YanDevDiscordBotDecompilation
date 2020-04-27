import asyncio
import json
import traceback
from collections import namedtuple

import aiohttp
import discord

from utils import cache


def can_send(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).send_messages


def traceback_maker(err, advance: bool = True):
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = '```py\n{1}{0}: {2}\n```'.format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"


def jsonget(file):
    try:
        with open(file, encoding='utf8') as data:
            return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")


# Removes the aiohttp ClientSession instance warning.
class HTTPSession(aiohttp.ClientSession):
    """ Abstract class for aiohttp. """

    def __init__(self, loop=None):
        super().__init__(loop=loop or asyncio.get_event_loop())

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
async def query(url, method="get", res_method="text", *args, **kwargs):
    async with getattr(session, method.lower())(url, *args, **kwargs) as res:
        return await getattr(res, res_method)()


async def get(url, *args, **kwargs):
    return await query(url, "get", *args, **kwargs)


async def post(url, *args, **kwargs):
    return await query(url, "post", *args, **kwargs)
