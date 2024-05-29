# -*- coding: utf-8 -*-
import functools


def my_decorator(func):
    # @functools.wraps(func)
    def wrapper1(*args, **kwargs):
        """decorator1"""
        print('Calling decorated function1...')
        return func(*args, **kwargs)

    return wrapper1

def my_decorator2(func):
    # @functools.wraps(func)
    def wrapper2(*args, **kwargs):
        """decorator2"""
        print('Calling decorated function2...')
        return func(*args, **kwargs)

    return wrapper2


@my_decorator
# @my_decorator2
def example():
    """Docstring1"""
    print('Called example function1')
    return 2


@my_decorator2
def example2():
    """Docstring2"""
    print('Called example function2')

print(example.__name__, example.__doc__)
print(example2.__name__, example2.__doc__)
result = example()
print(result)
# example2()
