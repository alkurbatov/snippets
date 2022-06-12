import sys
import traceback


def wrapper3():
    print("This is callstack:")
    traceback.print_stack()
    print()

    raise ValueError("Oops")


def wrapper2():
    wrapper3()


def wrapper1():
    try:
        wrapper2()

    except ValueError:
        print("This is exception traceback:")
        print(traceback.print_exception(*sys.exc_info()))


wrapper1()
