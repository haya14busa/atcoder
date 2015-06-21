#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: b.py
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

# B - 自動ドア
# 時間制限 : 2sec / スタック制限 : 256MB / メモリ制限 : 256MB
#
# 問題文
# ABCマーケットは高橋王国で最も人気なスーパーマーケットです。 入り口は自動ドアになっています。
#
# この自動ドアは人が前を通りかかると自動で開き、そこから T
# 秒後まで開き続け、その後自動的に閉じます。
# ドアが開いている状態で新たに人が前を通りかかると、通りかかった時刻のさらに T
# 秒後まで開き続ける時間が延長されます。
#
# 今日はのべ N 人の客が自動ドアの前を通りかかりました。 i 番目の人が通りかかった時刻はABCマーケットが開店してから Ai 秒経った時刻です。
#
# 今日、この自動ドアが開いていた合計秒数を求めてください。
#


def tailrec(func):
    from functools import wraps
    self_func = [func]
    self_firstcall = [True]
    self_CONTINUE = [object()]
    self_argskwd = [None]

    @wraps(func)
    def _tail_recursive(*args, **kwd):
        if self_firstcall[0] is True:
            func = self_func[0]
            CONTINUE = self_CONTINUE
            self_firstcall[0] = False
            try:
                while True:
                    result = func(*args, **kwd)
                    if result is CONTINUE:  # update arguments
                        args, kwd = self_argskwd[0]
                    else:  # last call
                        return result
            finally:
                self_firstcall[0] = True
        else:  # return the arguments of the tail call
            self_argskwd[0] = args, kwd
            return self_CONTINUE
    return _tail_recursive


def solve(n: int, t: int, cs) -> int:
    '''
    :n the number of people to pass by automatic door
    :t the duration to open door and extends it's time per person
    :cs the clock times of customers to pass by automatic door today
    :return the sum of duration to open the automatic door
    '''
    @tailrec
    def go(duration: int, tstart: int, rest):
        if not rest:
            return duration
        x, *xs = rest
        if tstart + t > x:
            return go(duration=duration + (x - tstart),
                      tstart=x,
                      rest=xs)
        else:
            return go(duration=duration + t, tstart=x, rest=xs)
    return go(duration=0, tstart=-float('inf'), rest=cs)


def getinput():
    def getints():
        return map(int, input().split(' '))

    def getallinputs():
        while True:
            try:
                yield ''.join(input())
            except EOFError:
                break
    n, t = getints()
    _as = map(int, getallinputs())
    return n, t, _as


def test():
    assert solve(5, 10, [20, 100, 105, 217, 314]) == 45
    assert solve(10, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
    assert solve(10, 100000, [3, 31, 314, 3141, 31415, 314159, 400000, 410000,
                              500000, 777777]) == 517253


def main():
    test()
    print(solve(*getinput()))

if __name__ == '__main__':
    main()
