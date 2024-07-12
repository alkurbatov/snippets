"""The module provides lazily evaluated wrappers around objects to be used with loggers.

Example usage:
logger.debug("Result of some heavy func: %s", LazyCallable(my_func, 1, 2, kwarg1=3))
"""

from typing import Any, Callable, ParamSpec

P = ParamSpec("P")


class LazyRepr:
    """LazyRepr designed to provide lazy creation of time consuming repr strings.

    It should be used in logger calls to avoid time waste when the resulting string
    is not logged due to log level settings (e.g. logger.debug when log level is ERROR).
    """

    def __init__(self, entity: Any) -> None:
        self._entity = entity

    def __str__(self) -> str:
        return repr(self._entity).replace("\n", " ")


class LazyCallable:
    """LazyCallable designed to provide lazy evaluation of time consuming Ofunctions.

    It should be used in logger calls to avoid time waste when the resulting string
    is not logged due to log level settings (e.g. logger.debug when log level is ERROR).
    """

    def __init__(
        self,
        entity: Callable[P, str],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        self._entity = entity
        self._args = args
        self._kwargs = kwargs

    def __str__(self) -> str:
        return self._entity(*self._args, **self._kwargs)
