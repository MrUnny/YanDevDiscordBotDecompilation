# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Embedded file name: /home/joelthomson08/midori-bot/utils/cache.py
# Compiled at: 2019-12-07 00:39:50
# Size of source mod 2**32: 1451 bytes
from functools import wraps

def cache(maxsize=128):
    cache = {}

    def decorator(func):

        @wraps(func)
        def inner(*args, no_cache=False, **kwargs):
            if no_cache:
                return func(*args, **kwargs)
            key_base = '_'.join((str(x) for x in args))
            key_end = '_'.join((f"{k}:{v}" for k, v in kwargs.items()))
            key = f"{key_base}-{key_end}"
            if key in cache:
                return cache[key]
            res = func(*args, **kwargs)
            if len(cache) > maxsize:
                del cache[list(cache.keys())[0]]
                cache[key] = res
            return res

        return inner

    return decorator


def async_cache(maxsize=128):
    cache = {}

    def decorator(func):

        @wraps(func)
        async def inner(*args, no_cache=False, **kwargs):
            if no_cache:
                return await func(*args, **kwargs)
            key_base = '_'.join((str(x) for x in args))
            key_end = '_'.join((f"{k}:{v}" for k, v in kwargs.items()))
            key = f"{key_base}-{key_end}"
            if key in cache:
                return cache[key]
            res = await func(*args, **kwargs)
            if len(cache) > maxsize:
                del cache[list(cache.keys())[0]]
                cache[key] = res
            return res

        return inner

    return decorator