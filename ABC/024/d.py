#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: d.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from pprint import pprint


def solve(a, b, c):
    return find_rc(a, b, c)


def makedp():
    cache = {}

    def dp(_r, _c):
        r, c = sorted([_r, _c])
        if r == 0 or c == 0:
            return 1
        else:
            if (r, c) not in cache:
                cache[(r, c)] = dp(r - 1, c) + dp(r, c - 1)
            return cache[(r, c)]
    return dp

dp = makedp()


def find_rc(x, y, z):
    def _find_rc(x, y, z):
        assert y >= z
        for i in range(99999999):
            for r in range(i):
                for c in range(0, r):
                    if (dp(r, c) == x and
                            dp(r, c + 1) == y and
                            dp(r + 1, c) == z):
                        return r, c
        return None
    flag = y < z
    args = [x] + sorted([y, z], reverse=True)
    r = _find_rc(*args)
    return tuple(sorted(r, reverse=True)) if flag else r


def getinput():
    def getints_line():
        return map(int, input().split(' '))
    return [int(input())for _ in range(3)]


def test():
    '''
    35
    15 21
    -> 4, 2

    126 252
        126 210
            84
    -> 5, 4

    '''
    r = find_rc(15, 35, 21)
    assert r == (4, 2)
    r = find_rc(15, 21, 35)
    assert r == (4, 2)
    r = find_rc(126, 252, 210)
    assert r == (5, 4)
    r = find_rc(144949225, 545897619, 393065978)
    assert r == (314159, 365358)


def main():
    test()
    # print(' '.join(map(str, solve(*getinput()))))
    # n = 7
    # pprint(list(reversed(
    #     [[str(dp(i, j)).rjust(3) for i in range(n)] for j in range(n)])))

    # 4, 10, 20, 35, 56, 84
    # 2x2, 2x5, 2x2x4, 5x7, 7x8, 2x2x3x7

if __name__ == '__main__':
    main()
