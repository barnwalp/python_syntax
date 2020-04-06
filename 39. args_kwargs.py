"""
*args allows you to take in more arguments than the number of formal
arguments that you previously defined. with *args, any number of
extra arguments can be tracked on to your current formal parameters

Using the *, the variable that we associate with the * becomes an
iterable meaning you can do things like iterate over it, run some
high order functions

it is used as a non-keyworded variable length argument list
"""


def multiply(*args):
    value = 1
    for arg in args:
        value *= arg
    return value


print(multiply(3, 5, 6))

"""
**kwargs is used to pass a keyworded, variable length argument list
**, allows us to pass through keyword arguments.
kwargs is like a dictionary that maps each keyword to the value that
we pass alongside it.
"""


def test(**kwargs):
    for key, value in kwargs.items():
        print(key + ", " + str(value))


test(a='b', b='c', c='d')
