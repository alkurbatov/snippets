# Enable the following options to simplify
# debugging of asyncio applications:

import asyncio
import warnings


def handle_exception(_loop: asyncio.AbstractEventLoop, context: dict[str, str]) -> None:
    """Catch exceptions not handled by asyncio tasks."""
    msg = context.get("exception", context["message"])
    print(f"Caught unhandled exception from async task: {msg}")


async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.slow_callback_duration = 0.2  # in seconds
    loop.set_exception_handler(handle_exception)

    warnings.simplefilter("always", ResourceWarning)


if __name__ == "__main__":
    asyncio.run(main())
