#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, m, xs):
    # xs: sorted
    assert len(xs) == m
    assert 1 <= n <= 10 ** 9
    assert 1 <= m <= 10 ** 5
    assert m <= n
    # left = float('inf')
    before_dist = float('inf')
    before_i = 0
    for i, x in enumerate(xs):
        next_i =  xs[i + 1] if i + 1 < m else float('inf')
        from_dist = x - before_i - 1
        to_dist = next_i - x

        if to_dist > before_dist * 2 + from_dist:
            before_i = x
            before_dist = 
        else:
            before_dist = from_dist
            before_i = x
    return 0


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
    return [n, m, getints(m)]


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
17 5
1
5
10
15
16
            ''',
            # EXPECT
            '''\
3
            '''
        ),

        (
            # INPUT
            '''\
66 10
8
9
16
23
37
47
51
52
53
64
            ''',
            # EXPECT
            '''\
8
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
