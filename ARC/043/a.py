#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, a, b, ss):
    assert 2 <= n <= 10 ** 5
    assert 1 <= a <= 10 ** 9
    assert 1 <= b <= 10 ** 9

    mins = min(ss)
    maxs = max(ss)

    if maxs - mins == 0:
        return (-1, '')
    else:
        p = b / (maxs - mins)
        q = a - ((p * sum(ss)) / n)
        return (p, q)


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n, a, b = getints_line()
    return [n, a, b, [getint() for _ in range(n)]]


def iosolve():
    return str(' '.join(map(str, solve(*getinput()))))
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
5 2 4
2
4
6
8
10
            ''',
            # EXPECT
            '''\
0.5 -1
            '''
        ),

        (
            # INPUT
            '''\
13 29 31
3
1
4
1
5
9
2
6
5
3
5
8
9
            ''',
            # EXPECT
            '''\
3.875 10.8173076
            '''
        ),
        (
            # INPUT
            '''\
5 1 2
34
34
34
34
34
            ''',
            # EXPECT
            '''\
-1
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
        # art.equal(iosolve(), expect.strip())
        e = expect.strip()
        if e == '-1':
            art.equal('-1', iosolve().strip())
        else:
            p, q = map(float, expect.strip().split(' '))
            ap, aq = map(float, iosolve().split(' '))
            # art.float_equal(float(), float(expect.strip()), 10 ** -6)
            art.float_equal(ap, p, 10 ** -6)
            art.float_equal(aq, q, 10 ** -6)


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
