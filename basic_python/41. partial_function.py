'''
A partial function allows us to call a second function wit fixed values
in certain arguments. for instance we have a function that computes an
exponentiation. then we may need to create a new function tat assigns a
fixed a value to either base or exponent. this can be done through partial.
'''

from functools import partial


def power(base, exponent):
    return base ** exponent


squared = partial(power, exponent = 2)
print(squared(7))
