#!/usr/bin/env python2.7
# -*-coding:utf-8 -*-

from timeit import Timer


def _fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 5 == 0:
        return "Buzz"
    elif x % 3 == 0 return "Fizz"
    else:
        return str(x)


def FizzBuzz(n):
    """ get fizzbuzz list

    Arguments:
    - `n`: integer, n > 0
    """
    return [_fizzbuzz(x) for x in range(1, n + 1)]


s = '''
def _fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 5 == 0:
        return "Buzz"
    elif x % 3 == 0:
        return "Fizz"
    else:
        return str(x)

def FizzBuzz(n):
    """ get fizzbuzz list

    Arguments:
    - `n`: integer, n > 0
    """
    return [_fizzbuzz(x) for x in range(1, n +1)]

FizzBuzz(10000)
'''


if __name__ == '__main__':
    t = Timer(stmt=s)
    print t.repeat(repeat=10, number=100)
