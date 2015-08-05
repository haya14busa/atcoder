#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, ses):
    '''
    ses: List[(start_time_str, ent_time_str)]
    '''
    assert(1 <= n <= 100)

    def tomill(time):
        h, m, sm = time.split(':')
        h, m = map(int, [h, m])
        s, mil = map(int, sm.split('.'))
        assert 21 <= h <= 22
        return mil + 1000 * s + 1000 * 60 * m + 1000 * 60 * 60 * (h - 21)

    ses = list(map(lambda se: list(map(tomill, se)), ses))

    backed_se = [(start, end) for start, end in ses if start >= end]
    left = max([-1] + list(map(lambda se: se[0], backed_se))) - 1000
    right = min([float('inf')] + list(map(lambda se: se[1], backed_se))) + 1000

    if right == float('inf'):
        return [-1 for _ in range(n)]
    else:
        ds = []
        for start, end in ses:
            if end <= left or right <= start:
                ds += [end - start]
            elif ((start >= end) or (start <= left and right <= end)):
                ds += [end - start + 1000]
            else:
                ds += [-1]
        return ds


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n = getint()
    ses = [input().split(' ') for _ in range(n)]
    return [n, ses]


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
1
21:00:01.500 21:00:01.000
            ''',
            # EXPECT
            '''\
500
            '''
        ),

        (
            # INPUT
            '''\
1
22:00:00.000 22:00:03.000
            ''',
            # EXPECT
            '''\
-1
            '''
        ),
        (
            # INPUT
            '''\
3
21:00:00.000 21:00:03.000
21:00:01.500 21:00:01.000
21:00:02.000 21:00:02.500
            ''',
            # EXPECT
            '''\
4000
500
500
            '''
        ),

        (
            # INPUT
            '''\
3
21:00:00.000 21:00:03.000
21:00:01.500 21:00:01.000
21:00:00.500 21:00:01.000
            ''',
            # EXPECT
            '''\
4000
500
-1
            '''
        ),

        (
            # INPUT
            '''\
5
21:00:00.000 21:00:03.000
21:00:01.500 21:00:01.000
21:00:00.000 21:00:03.000
21:00:00.700 21:00:01.800
21:00:00.400 21:00:01.800
            ''',
            # EXPECT
            '''\
4000
500
4000
-1
-1
            '''
        ),

        (
            # INPUT
            '''\
2
21:00:00.000 21:00:03.000
21:00:00.000 21:00:03.000
            ''',
            # EXPECT
            '''\
-1
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

    case = 0
    for stdin, expect in IO_TEST_CASES:
        case += 1
        print('#case ' + str(case))
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
