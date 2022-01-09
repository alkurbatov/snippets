import contextlib
import os


with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
