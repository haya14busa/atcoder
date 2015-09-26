#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, t, xys):
    assert 1 <= n <= 10 ** 5
    assert 0 <= t <= 10 ** 9
    assert len(xys) > 0
    ds = sorted(map(lambda xy: xy[0] - xy[1], xys), reverse = True)
    time = sum(map(lambda xy: xy[0], xys))
    if time <= t:
        return 0
    for i, d in enumerate(ds):
        time -= d
        if time <= t:
            return i + 1
    return -1


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n, t = getints_line()
    return [n, t, list(map(tuple, getints_lines(n)))]


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
5 7
1 0
3 0
5 0
2 0
4 0
            ''',
            # EXPECT
            '''\
2
            '''
        ),

        (
            # INPUT
            '''\

1 1000000000
5 0
            ''',
            # EXPECT
            '''\
0
            '''
        ),

        (
            # INPUT
            '''\
1 0
100 99
            ''',
            # EXPECT
            '''\
-1
            '''
        ),

        (
            # INPUT
            '''\
3 11
5 2
6 4
7 3
            ''',
            # EXPECT
            '''\
2
            '''
        ),

        (
            # INPUT
            '''\
6 92
31 4
15 9
26 5
35 8
97 9
32 3
            ''',
            # EXPECT
            '''\
3
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
