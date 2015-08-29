#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n):
    assert 1 <= n <= 10 ** 18

    def line(n):
        i = 0
        while True:
            if n < (2 ** i):
                return i - 1
            i += 1

    lnum = line(n)
    if lnum % 2:
        def accum(lnum):
            s = 0
            lnum -= 2
            while lnum > 0:
                s += 2 ** lnum
                lnum -= 2
            return s
        # if 2 ** lnum <= n <= 2 ** (lnum - 2) * 5 - 1:
        if 2 ** lnum <= n <= 2 ** lnum + accum(lnum) - 1:
            return 'Aoki'
        else:
            return 'Takahashi'
    else:
        def accum(lnum):
            s = 0
            lnum -= 2
            while lnum > 1:
                s += 2 ** lnum
                lnum -= 2
            return s + 2
        if lnum == 0:
            return 'Aoki'
        elif 2 ** (lnum + 1) - accum(lnum) <= n <= 2 ** (lnum + 1) + 1:
            return 'Aoki'
        else:
            return 'Takahashi'


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    return [getint()]


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
1
            ''',
            # EXPECT
            '''\
Aoki
            '''
        ),

        (
            # INPUT
            '''\
5
            ''',
            # EXPECT
            '''\
Takahashi
            '''
        ),

        (
            # INPUT
            '''\
7
            ''',
            # EXPECT
            '''\
Aoki
            '''
        ),

        (
            # INPUT
            '''\
10
            ''',
            # EXPECT
            '''\
Takahashi
            '''
        ),

        (
            # INPUT
            '''\
123456789123456789
            ''',
            # EXPECT
            '''\
Aoki
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
        print('expect: ', expect.strip())
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
