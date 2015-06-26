#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: c.py
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
# 問題文 高橋王国には N 個の街があり、それぞれ 1 ～ N
# の整数によって番号付けされています。
#
# 高橋王国には K 種類の民族が住んでおり、i 番目の民族は街 Si に住んでいます。
#
# 高橋王国の民族たちには、百年に一回住む街を変える「民族大移動」という文化が有ります。
# 基本的には全民族が同時期に「民族大移動」を行うのですが、全く同じ日に全民族が移動すると混雑が予想されるため、
# 以下の様な移動制限を毎日設けて、 D 日かけて行います。
#
# i 日目は 街の番号が Li 以上 Ri
# 以下であるよう街の間を自由に行き来できる。それ以外の行き来は禁止される。
# 各民族はこの移動制限を守り、いくつかの街を経由しながら目的地の街まで移動します。
#
# i 番目の民族の目的地は街 Ti
# です。どの民族もできるだけ早く目的地に到着したいと思っています。
#
# 各民族について、目的地に到着できる最も早い日を求めてください。
#
# なお、どの民族も D 日以内に目的地に到着できることが保証されています。
#
#


def solve(n: int, d: int, k: int, lrs, sts):
    '''
    n: 1 <= n <= 10^9
    d: 1 <= d <= 10^4
    k: 1 <= k <= 100
    lrs: (L_d, R_d) restriction. L <= x <= R, x can move this town
    sts: (S_k, T_k) (start_town, target_town)
    return: list of minimum date for each ethnic group
    time complexity: O(KD)
    '''
    r = []
    for ethnic in sts:
        start, target = ethnic
        movable = {'left': start, 'right': start}

        def is_movable(left, right):
            return (left <= movable['left'] <= right or
                    left <= movable['right'] <= right)

        for d, date in enumerate(lrs):
            left, right = date
            if is_movable(left, right):
                movable['left'] = min(left, movable['left'])
                movable['right'] = max(right, movable['right'])
            if movable['left'] <= target <= movable['right']:
                r.append(d + 1)
                break
    return r


def getinput():
    def getints_line():
        return map(int, input().split(' '))
    n, d, k = getints_line()
    lrs = [tuple(getints_line()) for _ in range(d)]
    sts = [tuple(getints_line()) for _ in range(k)]
    return n, d, k, lrs, sts


def test():
    r = solve(10, 10, 3,
              [(1, 5),
               (3, 6),
               (7, 10),
               (5, 8),
               (4, 4),
               (1, 4),
               (2, 9),
               (1, 3),
               (1, 1),
               (4, 5)],
              [(1, 6), (2, 7), (10, 1)])
    assert r == [2, 4, 8]
    r = solve(10, 10, 4,
              [(1, 2),
               (2, 4),
               (3, 6),
               (4, 8),
               (5, 10),
               (9, 10),
               (7, 8),
               (5, 6),
               (3, 5),
               (1, 3)],
              [(10, 1), (3, 8), (2, 4), (1, 3)])
    assert r == [10, 4, 2, 2]
    r = solve(314159265, 10, 1,
              [(1, 10000),
               (500, 12031),
               (1414, 113232),
               (111111, 777777),
               (666661, 23423423),
               (12345678, 123456789),
               (111111111, 314159265),
               (112334, 235235235),
               (1, 223445),
               (314, 1592)],
              [(1, 314159265)])
    assert r == [7]


def main():
    # test()
    print('\n'.join(map(str, solve(*getinput()))))

if __name__ == '__main__':
    main()
