"""Implementation of object containing either function result of error.

Similar to std::expected.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

V = TypeVar("V")
E = TypeVar("E")


@dataclass(frozen=True, slots=True, match_args=True)
class Result(Generic[V, E]):
    value: V | None
    error: E | None

    def __post_init__(self):
        if self.value is self.error is None:
            raise ValueError("value or error is required")

        if self.value is not None and self.error is not None:
            raise ValueError("init value or error only")

    @classmethod
    def ok(cls, value: V) -> Result[V, Any]:
        return cls(value=value, error=None)

    @classmethod
    def fail(cls, error: E) -> Result[Any, E]:
        return cls(value=None, error=error)
