import sys
import traceback


def wrapper3() -> None:
    print("This is callstack:")
    traceback.print_stack()
    print()

    raise ValueError("Oops")


def wrapper2() -> None:
    wrapper3()


def wrapper1() -> None:
    try:
        wrapper2()

    except ValueError:
        print("This is exception traceback:")
        traceback.print_exception(*sys.exc_info())


wrapper1()
