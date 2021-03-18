#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib(n):
    """return the nth number in Fibonacci sequence.

    Args:
        n: a non-negative integer

    Return:
        the nth number in Fibonacci sequence, starting with 1, 1, ...

    """
    if n <= 0:
        return -1
    i = j = 1
    for _ in range(n - 1):
        i, j = j, i + j
    return i


def main():
    fib(10)


if __name__ == "__main__":
    main()
