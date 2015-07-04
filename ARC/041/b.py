#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n: int, m: int, bss):
    ass = [[0 for _ in range(m)] for _ in range(n)]

    def put(x, i, j):
        '''up, left, right, down'''
        # # up
        # if (1 < i and
        #     0 < j < m - 1 and
        #     bss[i - 2][j] >= x and
        #     bss[i - 1][j - 1] >= x and
        #     bss[i - 1][j + 1] >= x
        #    ):
        #     bss[i - 2][j] -= x
        #     bss[i - 1][j - 1] -= x
        #     bss[i - 1][j + 1] -= x
        #     bss[i][j] -= x
        #     ass[i - 1][j] += x

        # left
        if (1 < i < n - 1 and
            2 < j and
            bss[i - 1][j - 1] >= x and
            bss[i][j - 2] >= x and
            bss[i + 1][j - 1] >= x
           ):
            bss[i - 1][j - 1] -= x
            bss[i][j - 2] -= x
            bss[i + 1][j - 1] -= x
            bss[i][j] -= x
            ass[i][j - 1] += x

        # right
        # if (1 < i < n - 1 and
        #     j < m - 2 and
        #     bss[i - 1][j + 1] >= x and
        #     bss[i][j + 2]     >= x and
        #     bss[i + 1][j + 1] >= x
        #    ):
        #     bss[i - 1][j + 1] -= x
        #     bss[i][j + 2]     -= x
        #     bss[i + 1][j + 1] -= x
        #     bss[i][j] -= x
        #     ass[i][j + 1] += x

        # down
        if (i < n - 2 and
            0 < j < m - 1 and
            bss[i + 1][j - 1] >= x and
            bss[i + 1][j + 1] >= x and
            bss[i + 2][j]     >= x
           ):
            bss[i + 1][j - 1] -= x
            bss[i + 1][j + 1] -= x
            bss[i + 2][j]     -= x
            bss[i][j] -= x
            ass[i + 1][j] += x

    for x in range(1, 10):
        for i in range(n):
            for j in range(m):
                # if bss[i][j] == x:
                if bss[i][j] == x:
                    put(x, i, j)
                    # print(x)
                    # print('ass: ', ass)
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
