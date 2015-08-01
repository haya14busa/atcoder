#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(m, n, a, b):
    cnt = 0
    for l in range(m):
        for c in range(n):
            if a[l][c] != b[l][c]:
                cnt += 1
                if (c + 1 < n and a[l][c + 1] != b[l][c + 1] and
                        a[l][c] == b[l][c + 1] and a[l][c + 1] == b[l][c]):
                    a[l][c], a[l][c + 1] = a[l][c + 1], a[l][c]
                elif (l + 1 < m and a[l + 1][c] != b[l + 1][c] and
                        a[l][c] == b[l + 1][c] and a[l + 1][c] == b[l][c]):
                    a[l][c], a[l + 1][c] = a[l + 1][c], a[l][c]
                else:
                    a[l][c] = b[l][c]
    return cnt


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    m, n = getints_line()
    a = getints_lines(m)
    b = getints_lines(m)
    return [m, n, a, b]


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
2 2
0 0
1 0
0 0
0 1
            ''',
            # EXPECT
            '''\
1
            '''
        ),

        (
            # INPUT
            '''\
3 3
0 0 0
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
            ''',
            # EXPECT
            '''\
4
            '''
        ),

        (
            # INPUT
            '''\
3 4
0 0 0 0
1 1 0 0
0 0 0 0
1 1 1 0
0 1 0 0
0 0 0 0
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
