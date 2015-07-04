#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n: int, m: int, bss):
    ass = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if bss[i - 1][j] > 0 and bss[i][j - 1] > 0 and bss[i][j + 1] > 0 and bss[i + 1][j] > 0:
                r = min(bss[i - 1][j], bss[i][j - 1], bss[i][j + 1], bss[i + 1][j])
                ass[i][j] = r
                bss[i - 1][j] -= r
                bss[i][j - 1] -= r
                bss[i][j + 1] -= r
                bss[i + 1][j] -= r
    return ass


def getinput():
    def getints_line():
        return map(int, input().split(' '))
    n, m = getints_line()
    bss = []
    for _ in range(n):
        bss.append(list(map(int, list(input()))))
    return n, m, bss


def test():
    r = solve(3, 3,
              [
                  [0, 1, 0],
                  [1, 0, 1],
                  [0, 1, 0]
              ]
              )
    assert r == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    r = solve(3, 4,
              [
                [0, 2, 3, 0],
                [2, 3, 2, 3],
                [0, 2, 3, 0]
              ]
              )
    assert r == [[0, 0, 0, 0], [0, 2, 3, 0], [0, 0, 0, 0]]



def main():
    # test()
    ass = solve(*getinput())
    for _as in ass:
        print(''.join(map(str, _as)))
    # print()
    # print('\n'.join(map(str, solve(*getinput()))))

if __name__ == '__main__':
    main()
