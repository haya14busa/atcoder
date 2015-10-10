#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, m, sts):
    assert 1 <= n <= 3 * (10 ** 5)
    assert 1 <= m <= 1 * (10 ** 5)
    assert len(sts) == m
    ists = list(enumerate(sts, 1))
    ists.sort(key=lambda kst: kst[1][1])
    ists.sort(key=lambda kst: kst[1][0])
    # print('---')
    # print(ists)
    ans = []
    pleft = -100 # left wall
    prev = (-100, -1)
    right = -100
    for i, (s, t) in ists:
        # print(i, (s, t))
        # if t <= prev[1]:
        if t <= right:
            ans.append(i)
        if s <= pleft and right <= t:
            ans.append(previ)
        # if pleft + 1 == s and right <= t:
        if pleft + 1 >= s and right <= t:
            ans.append(previ)
        if prev == (s, t):
            ans.append(previ)
        if prev[0] == s and prev[1] <= t:
            ans.append(previ)
        # pleft = max([s, right])
        pleft = max(pleft, right)
        prev = (s, t)
        right = max(right, t)
        previ = i
        # print('ans:', ans)
    ans = list(set(ans))
    return [len(ans)] + ans


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n, m = getints_line()
    return [n, m, getints_lines(m)]


def iosolve():
    # return str(solve(*getinput()))
    # return 'YES' if solve(*getinput()) else 'NO' # for boolean output
    return '\n'.join(map(str, solve(*getinput()))) # for multiple line output


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
10 5
1 4
5 5
6 8
9 10
5 6
            ''',
            # EXPECT
            '''\
2
2
5
            '''
        ),

        (
            # INPUT
            '''\
3 6
1 1
1 1
2 2
2 2
3 3
3 3
            ''',
            # EXPECT
            '''\
6
1
2
3
4
5
6
            '''
        ),

        (
            # INPUT
            '''\
10 3
1 4
2 6
6 10
            ''',
            # EXPECT
            '''\
0
            '''
        ),

        (
            # INPUT
            '''\
10 3
1 4
4 6
5 10
            ''',
            # EXPECT
            '''\
1
2
            '''
        ),

        (
            # INPUT
            '''\
10 3
1 10
4 6
5 10
            ''',
            # EXPECT
            '''\
2
2
3
            '''
        ),


        (
            # INPUT
            '''\
10 3
1 5
4 6
6 10
            ''',
            # EXPECT
            '''\
1
2
            '''
        ),

        (
            # INPUT
            '''\
10 3
1 6
1 8
7 10
            ''',
            # EXPECT
            '''\
2
1
2
            '''
        ),


        (
            # INPUT
            '''\
10 3
1 5
1 8
7 10
            ''',
            # EXPECT
            '''\
1
1
            '''
        ),

        (
            # INPUT
            '''\
10 3
1 6
4 8
7 10
            ''',
            # EXPECT
            '''\
1
2
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
