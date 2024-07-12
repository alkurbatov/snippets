import asyncio
import contextvars
import functools
from typing import Any, Callable


async def to_thread(func: Callable, /, *args, **kwargs) -> Any:
    """Run blocking code in a separate thread to asynchroniously wait for result.

    See: https://github.com/python/cpython/blob/main/Lib/asyncio/threads.py

    (!) Should be used on Python < 3.9, in other case please prefer asyncio.to_thread.
    """
    loop = asyncio.get_running_loop()
    ctx = contextvars.copy_context()
    func_call: Callable = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)
