#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: a.py
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


def solve(a: int, b: int, c: int, k: int, s: int, t: int) -> int:
    '''
    a: price per one child
    b: price per one adult
    k, c: cont down by `c` per person if the number of all members is greater
        than `k`.
    s: the number of children
    t: the number of adult
    '''
    for_child = a * s
    for_adult = b * t
    discount = c * (s + t) if (s + t) >= k else 0
    return for_child + for_adult - discount


def readline_as_ints():
    return map(int, input().split(' '))


def test():
    assert solve(100, 200, 50, 20, 40, 10) == 3500
    assert solve(400, 1000, 400, 20, 10, 10) == 6000


def main():
    test()
    a, b, c, k = readline_as_ints()
    s, t = readline_as_ints()
    print(solve(a, b, c, k, s, t))

if __name__ == '__main__':
    main()
