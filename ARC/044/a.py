#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n):
    if n == 1:
        return False
    elif n == 2 or n == 3 or n == 5:
        return True

    digit1 = n % 10

    if digit1 % 2 == 0 or digit1 == 5:
        return False

    sum_of_each_digit = sum(map(int, list(str(n))))

    if sum_of_each_digit % 3:
        return True

    return False


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    return [getint()]


def iosolve():
    # return str(solve(*getinput()))
    return 'Prime' if solve(*getinput()) else 'Not Prime' # for boolean output
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
42
            ''',
            # EXPECT
            '''\
Not Prime
            '''
        ),

        (
            # INPUT
            '''\
49
            ''',
            # EXPECT
            '''\
Prime
            '''
        ),

        (
            # INPUT
            '''\
3
            ''',
            # EXPECT
            '''\
Prime
            '''
        ),

        (
            # INPUT
            '''\
1
            ''',
            # EXPECT
            '''\
Not Prime
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
