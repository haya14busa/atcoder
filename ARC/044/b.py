#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io

from collections import defaultdict
from itertools import combinations


MOD = 10 ** 9 + 7

def solve(n, xs):
    assert 1 <= n <= 10 ** 5
    for x in xs:
        assert 0 <= x < n

    table = {}
    for i, x in enumerate(xs, 1):
        table[i] = x

    inv_table = defaultdict(int)
    for x in table.values():
        inv_table[x] += 1

    if inv_table[0] != 1:
        return 0

    
    answer = 1
    for dist, n in sorted(inv_table.items(), key=lambda x:x[0]):
        if dist == 0:
            continue
        same = ((2 ** inv_table[dist - 1]) - 1)
        answer *= (same ** n if same > 1 else same) % MOD
        answer *= ((2 ** ((n * (n - 1)) // 2)) or 1) % MOD

    return answer % MOD


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n = getint()
    return [n, getints_line()]


def iosolve():
    return str(solve(*getinput()))
    # return 'YES' if solve(*getinput()) else 'NO' # for boolean output
    # return '\n'.join(map(str, solve(*getinput()))) # for multiple line output


def main():
    if sys.stdin.isatty():
        test()
    stdin_lines = getstdin_lines()
    sys.stdin = io.StringIO('\n'.join(stdin_lines))
    if stdin_lines:
        print(iosolve())
    else:
        test()


def test():
    IO_TEST_CASES = [

        (
            # INPUT
            '''\
4
0 1 1 2
            ''',
            # EXPECT
            '''\
6
            '''
        ),

        (
            # INPUT
            '''\
4
0 1 2 0
            ''',
            # EXPECT
            '''\
0
            '''
        ),

        (
            # INPUT
            '''\
3
1 1 2
            ''',
            # EXPECT
            '''\
0
            '''
        ),

        (
            # INPUT
            '''\
17
0 1 1 2 2 4 3 2 4 5 3 3 2 1 5 4 2
            ''',
            # EXPECT
            '''\
855391686
            '''
        ),

    ]

    # List[(List[arg for solve()], expect)]
    TEST_CASES = [
        # ([], None),
    ]

    # You do need to see below
    import unittest  # to save memory, import only if test required
    import sys
    import io

    class Assert(unittest.TestCase):
        def equal(self, a, b):
            self.assertEqual(a, b)

        def float_equal(self, actual, expect, tolerance):
            self.assertTrue(expect - tolerance < actual < expect + tolerance)

    art = Assert()

    for inputs, expect in TEST_CASES:
        art.equal(solve(*inputs), expect)

    for stdin, expect in IO_TEST_CASES:
        sys.stdin = io.StringIO(stdin.strip())
        art.equal(iosolve(), expect.strip())
        # art.float_equal(float(iosolve()), float(expect.strip()), 10 ** -6)


def getstdin_lines():
    stdin = []
    while 1:
        try:
            stdin.append(input())
        except EOFError:
            break
    return stdin

if __name__ == '__main__':
    main()
