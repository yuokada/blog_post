#!/usr/bin/env python2.7
# -*-coding:utf-8 -*-


def collatz(n):
    ls = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = n * 3 + 1
        ls.append(n)
    return ls

if __name__ == '__main__':
    for i in range(1, 13):
        print collatz(i)

