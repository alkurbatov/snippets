import asyncio
from typing import Generic, TypeVar

T = TypeVar("T")


class ChannelWriteError(Exception):
    def __init__(self) -> None:
        super().__init__("Cannot put item into the closed channel")


class Channel(Generic[T]):
    """Simplified implementation of Golang buffered channel in async Python.

    This implementation is not thread safe.
    """

    def __init__(self) -> None:
        self._queue: asyncio.Queue[T | None] = asyncio.Queue()
        self._closed = False

    async def put(self, item: T) -> None:
        """Put an item into the channel.

        Throws ChannelWriteError, if channel is closed.
        """
        if self._closed:
            raise ChannelWriteError

        await self._queue.put(item)

    async def get(self) -> T | None:
        """Get an item from the channel.

        None is returned in case of closed channel.
        It is safe to read from closed channel several times.
        """
        if self.drained():
            return None

        return await self._queue.get()

    def close(self) -> None:
        if self._closed:
            return

        self._closed = True

        if self._queue.qsize() == 0:
            # NB (a.kurbatov): Put None to unblock readers waiting on empty queue.
            self._queue.put_nowait(None)

    def drained(self) -> bool:
        """No more data could be read from this channel."""
        return self._closed and self._queue.qsize() == 0

    def __len__(self) -> int:
        return self._queue.qsize()

    def closed(self) -> bool:
        return self._closed
