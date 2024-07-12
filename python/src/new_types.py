"""Custom types creation.

Should be used e.g. as arguments and return values in functions and methods.
"""

import typing

ArtID = typing.NewType("ArtID", int)
UserID = typing.NewType("UserID", int)
