import functools
from colorama import init, Fore

init()


def color(color):
    def wrapper(func):
        @functools.wraps(func)
        def runner(*args, **kwargs):
            print(color + "changing to blue")
            func(*args, **kwargs)

        return runner

    return wrapper


@color(color=Fore.BLUE)
def greeter():
    print("Hello, world!!")
    print("Just saying hi again")


greeter()


def logger(func):
    def wrapper():
        print("Logging execution")
        func()
        print("Done execution")

    return wrapper


@logger
def sample():
    print("... inside sample function")


sample()



def demo():
    print("printing this")
    return "something"

