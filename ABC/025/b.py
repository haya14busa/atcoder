#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, a, b, sds):
    ds = map(lambda sd: (sd[0], a) if sd[1] < a else (sd[0], b) if sd[1] > b else sd, sds)
    ds = map(lambda sd: sd[1] if sd[0] == 'East' else -sd[1], ds)
    d = sum(ds)
    return ('' if d == 0 else 'East ' if d > 0 else 'West ') + str(abs(d))

def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n, a, b = getints_line()
    # return [ (t[0], int(t[1])) for t in input().split(' ') for _ in range(n)]
    # print( [ input().split(' ') for _ in range(n)])
    lines = [input().split(' ') for _ in range(n)]
    return [n, a, b, [(s, int(d)) for s, d in lines]]


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
3 5 10
East 7
West 3
West 11
            ''',
            # EXPECT
            '''\
West 8
            '''
        ),

        (
            # INPUT
            '''\
3 3 8
West 6
East 3
East 1
            ''',
            # EXPECT
            '''\
0
            '''
        ),

        (
            # INPUT
            '''\
5 25 25
East 1
East 1
West 1
East 100
West 1
            ''',
            # EXPECT
            '''\
East 25
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
