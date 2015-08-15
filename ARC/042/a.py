#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


def solve(n_of_slead, n_of_w, ws):
    assert 1 <= n_of_slead <= 10 ** 5
    assert 1 <= n_of_w <= 10 ** 5
    sleads = range(1, n_of_slead + 1)
    wsleads = []
    wslead_set = set()
    for w in reversed(ws):
        if w not in wslead_set:
            wsleads.append(w)
            wslead_set.add(w)
    rest = sorted(set(sleads) - wslead_set)
    return wsleads + rest


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n, m = getints_line()
    return [n, m, [getint() for _ in range(m)]]


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

        # (
        #     # INPUT
        #     '''\
        #     ''',
        #     # EXPECT
        #     '''\
        #     '''
        # ),

        (
            # INPUT
            '''\
3 3
2
3
1
            ''',
            # EXPECT
            '''\
1
3
2
            '''
        ),

        (
            # INPUT
            '''\
3 3
1
1
1
            ''',
            # EXPECT
            '''\
1
2
3
            '''
        ),

        (
            # INPUT
            '''\
10 10
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
            ''',
            # EXPECT
            '''\
3
5
6
2
9
1
4
7
8
10
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
