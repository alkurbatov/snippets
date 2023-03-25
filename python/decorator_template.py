"""
Kudos to https://realpython.com/primer-on-python-decorators/

Type hints taken from:
https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators
"""

import functools
from typing import Any, Awaitable, Callable, cast, TypeVar

DecoratedFunction = TypeVar("DecoratedFunction", bound=Callable[..., Any])
DecoratorFactory = Callable[[DecoratedFunction], DecoratedFunction]

AsyncDecoratedFunction = TypeVar(
    "AsyncDecoratedFunction", bound=Callable[..., Awaitable[Any]]
)
AsyncDecoratorFactory = Callable[[AsyncDecoratedFunction], AsyncDecoratedFunction]


def decorator(func: DecoratedFunction) -> DecoratedFunction:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return cast(DecoratedFunction, wrapper)


def decorator_with_args(_some_arg: Any) -> DecoratorFactory:
    # Do something with _some_arg.

    def actual_decorator(func: DecoratedFunction) -> DecoratedFunction:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value

        return cast(DecoratedFunction, wrapper)

    return actual_decorator


def async_decorator(func: AsyncDecoratedFunction) -> AsyncDecoratedFunction:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        # Do something before
        value = await func(*args, **kwargs)
        # Do something after
        return value

    return cast(AsyncDecoratedFunction, wrapper)


def async_decorator_with_args(_some_arg: Any) -> AsyncDecoratorFactory:
    # Do something with _some_arg.

    def actual_decorator(func: AsyncDecoratedFunction) -> AsyncDecoratedFunction:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            # Do something before
            value = await func(*args, **kwargs)
            # Do something after
            return value

        return cast(AsyncDecoratedFunction, wrapper)

    return actual_decorator
