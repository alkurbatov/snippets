import sys
import traceback


def wrapper3():
    raise ValueError('Oops')


def wrapper2():
    wrapper3()


def wrapper1():
    try:
        wrapper2()

    except ValueError:
        print(traceback.print_exception(*sys.exc_info()))


wrapper1()
