import contextlib
from pathlib import Path

with contextlib.suppress(FileNotFoundError):
    Path("somefile.tmp").unlink()
