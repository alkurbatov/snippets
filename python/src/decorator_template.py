"""Decorators examples.

Kudos to https://realpython.com/primer-on-python-decorators/

Type hints taken from:
https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators
"""

import functools
from typing import Any, Awaitable, Callable, ParamSpec, TypeAlias, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def decorator(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper


def decorator_with_args(_some_arg: Any) -> Callable[[Callable[P, T]], Callable[P, T]]:
    # Do something with _some_arg.

    def actual_decorator(func: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value

        return wrapper

    return actual_decorator


def async_decorator(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        # Do something before
        value = await func(*args, **kwargs)
        # Do something after
        return value

    return wrapper


AsyncFunc: TypeAlias = Callable[P, Awaitable[T]]


def async_decorator_with_args(_some_arg: Any) -> Callable[[AsyncFunc], AsyncFunc]:
    # Do something with _some_arg.

    # NB (a.kurbatov): We don't use the AsyncFunc alias below to avoid weird
    # errors from mypy.
    def actual_decorator(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            # Do something before
            value = await func(*args, **kwargs)
            # Do something after
            return value

        return wrapper

    return actual_decorator
