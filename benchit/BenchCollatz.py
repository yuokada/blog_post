#!/usr/bin/env python2.7
# -*-coding:utf-8 -*-

from timeit import Timer


def collatz(n):
    ls = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = n * 3 + 1
        ls.append(n)
    return ls


s = '''
def collatz(n):
    ls = [n]
    while not n == 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = n * 3 + 1
        ls.append(n)
    return ls

for i in xrange(1, 1000):
    collatz(i)
'''


if __name__ == '__main__':
    t = Timer(stmt=s)
    # ミリ秒で表示するために1000で乗算
    print map(lambda x: x * 1000.0, t.repeat(repeat=10, number=100))
