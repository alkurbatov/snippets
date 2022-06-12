"""
Kudos to https://realpython.com/primer-on-python-decorators/
"""

import functools
from typing import Any, Awaitable, Callable, TypeVar

T = TypeVar("T")


def decorator(func: Callable[..., Callable[T]]) -> Callable[..., Callable[T]]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> T:
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper


def decorator_with_args(_some_arg: Any) -> Callable:
    # Do something with _some_arg.

    def actual_decorator(
        func: Callable[..., Callable[T]]
    ) -> Callable[..., Callable[T]]:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value

        return wrapper

    return actual_decorator


def async_decorator(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> T:
        # Do something before
        value = await func(*args, **kwargs)
        # Do something after
        return value

    return wrapper


def async_decorator_with_args(_some_arg: Any) -> Callable:
    # Do something with _some_arg.

    def actual_decorator(
        func: Callable[..., Awaitable[T]]
    ) -> Callable[..., Awaitable[T]]:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            # Do something before
            value = await func(*args, **kwargs)
            # Do something after
            return value

        return wrapper

    return actual_decorator
