#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n, ds):
    ds = sorted(ds)

    cache = {}

    def cnt(_min, rest):
        if (_min, rest) in cache:
            return cache[(_min, rest)]
        else:
            candidates = [d for d in ds if d >= _min]
            if rest == 1:
                cache[(_min, rest)] = len(candidates)
            elif (len(candidates) < rest or
                  candidates[-1] < _min * (2 ** (rest - 1))):
                cache[(_min, rest)] = 0
            else:
                c = 0
                for i in candidates:
                    # Use i
                    c += cnt(i * 2, rest - 1)
                cache[(_min, rest)] = c
            return cache[(_min, rest)]

    # print('ds:', ds)
    # def cnt(idx, rest):
    #     if (idx, rest) in cache:
    #         return cache[(idx, rest)]
    #     else:
    #         if n < idx + rest:
    #             cache[(idx, rest)] = 0
    #             return 0
    #         t = ds[idx]
    #         candidates = [d for d in ds[idx + 1:] if d >= t * 2]
    #         if len(candidates) < rest - 1:
    #             for i in range(rest, 5):
    #                 cache[(idx, i)] = 0
    #         elif rest == 2:
    #             print('ichi:', idx, t, candidates)
    #             cache[(idx, rest)] = len(candidates) + cnt(idx + 1, rest)
    #         else:
    #             cache[(idx, rest)] = cnt(idx + 1, rest) + cnt(idx + 1, rest - 1)
    #         return cache[(idx, rest)]

    r = cnt(0, 4)
    return r % (10 ** 9 + 7)


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
