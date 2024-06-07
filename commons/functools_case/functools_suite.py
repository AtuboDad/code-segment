# -*- coding: utf-8 -*-
import functools



def note(func):
    def wrapper(*args, **kwargs):
        print('note something')
        return func(*args, **kwargs)

    return wrapper

@note
def test():
    print('I am test')


test()
print(test.__doc__)
print(test.__name__)


def note2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('note something')
        return func(*args, **kwargs)

    return wrapper

@note2
def test2():
    print('I am test')


test2()
print(test2.__doc__)
print(test2.__name__)