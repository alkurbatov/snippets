"""Implementation of domain object with validation during it's creation."""

from typing import Self


class StrictInteger(int):
    min_value = 1
    max_value = 256

    def __new__(cls, value) -> Self:
        cls._validate(value)
        return super().__new__(cls, value)

    @classmethod
    def _validate(cls, v) -> None:
        if not isinstance(v, int):
            raise TypeError("int required", v._class_)

        if not (cls.min_value < v < cls.max_value):
            raise ValueError("invalid value range", v, cls.min_value, cls.max_value)
