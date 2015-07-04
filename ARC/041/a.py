#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(x: int, y: int, k: int) -> int:
    '''
    x: the num of 表 True
    y: the num of 裏 False
    k: the num of coint to be reversed
    '''
    if k <= y:
        return x + k
    else:
        return x - (k - y) + y


def getinput():
    def getints_line():
        return map(int, input().split(' '))
    x, y = getints_line()
    k = int(input())
    return x, y, k


def test():
    assert solve(3, 2, 1) == 4
    assert solve(3, 2, 4) == 3
    assert solve(3, 2, 5) == 2


def main():
    # test()
    print(solve(*getinput()))

if __name__ == '__main__':
    main()
