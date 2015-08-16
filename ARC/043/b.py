#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io

MOD = 10 ** 9 + 7

def solve(n, ds):
    assert 4 <= n <= 10 ** 5
    ds = sorted(ds)
    MD = 10 ** 5 + 1  # max d

    # dp[i][d]
    # i: i 番目の問題として (0 <= i <= 4)
    # d: d (D_x) を採用した
    # 場合の数
    dp = [[0] * MD for _ in range(5)]

    for d in ds:
        dp[0][d] += 1

    s = 0
    for i in range(MD):
        s += dp[0][i]
        dp[1][i] = s

    for i in range(2, 4 + 1):
        for j in range(1, MD):
            dp[i][j] = dp[i][j - 1]
            if dp[0][j]:
                dp[i][j] += (dp[i - 1][j // 2] * dp[0][j])
                # dp[i][j] *= dp[0][j]


    # print('=' * 10)
    # print('ds: ', ds)
    # print('i', list(range(ds[-1] + 1)))
    # print('--')
    # for ii in range(4, -1, -1):
    #     print(ii, dp[ii][:ds[-1] + 1])

    return dp[4][-1] % MOD


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n = getint()
    return [n, [getint() for _ in range(n)]]


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
        # print(solve(8, [1,3,4,6,7,8,10,12]))
        # print(solve(4, [2, 4, 8, 16]))
        # print(solve(5, [2, 4, 8, 16, 16]))
        # print(solve(7, [1, 2, 2, 4, 4, 8, 8]))
        # print(solve(7, [1, 2, 3, 3, 4, 6, 16]))
        # 1, 2, 4, 16
        # 1, 2, 6, 16
        # 1, 3, 6, 16
        # 1, 3, 6, 16


def test():
    IO_TEST_CASES = [

        (
            # INPUT
            '''\
5
1
2
4
5
10
            ''',
            # EXPECT
            '''\
2
            '''
        ),

        (
            # INPUT
            '''\
10
11
12
13
14
15
16
17
18
19
20
            ''',
            # EXPECT
            '''\
0
            '''
        ),

        (
            # INPUT
            '''\
20
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
            ''',
            # EXPECT
            '''\
94
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
