#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io
import math


class Node():
    def __init__(self, xy):
        x, y = xy
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __repr__(self):
        return '<Node({}, {})>'.format(self.x, self.y)

    def connect(self, node):
        # if self.left:
        assert node.right is None
        assert node is not None
        assert self is not None
        self.left = node
        node.right = self
        assert self.left != self.right

    def fx(self, node):
        dx = (node.x - self.x)
        if dx != 0:
            a = (node.y - self.y) / (node.x - self.x)
            b = self.y - a * self.x
            return lambda x: x * a + b
        else:
            return lambda x: None

    def dist(self, node):
        dx = (node.x - self.x)
        dy = (node.y - self.y)
        return math.sqrt(dx ** 2 + dy ** 2)


def solve(txy, n, xys):
    assert 3 <= n <= 10
    nodes = list(map(lambda x: Node(x), xys))
    # O(n * (n-1)! * (n - 2))
    for i, node in enumerate(nodes):
        rest_nodes = [rn for rn in nodes[:i] + nodes[i + 1:] if not rn.right and rn.left != node]
        for connect_to_node in rest_nodes:
            f = node.fx(connect_to_node)
            sign = None
            flag = True
            for rest_xy in [frest_node
                            for frest_node in nodes
                            if frest_node != node and frest_node != connect_to_node]:
                fresult = f(rest_xy.x)
                if fresult:
                    if sign is None:
                        sign = fresult > rest_xy.y
                    elif sign != (fresult > rest_xy.y):
                        flag = False
                        break
                else:
                    if sign is None:
                        sign = connect_to_node.x > rest_xy.x
                    elif sign != (connect_to_node.x > rest_xy.x):
                        flag = False
                        break
            if flag:
                node.connect(connect_to_node)
                break
        assert node.left is not None
    dist = float('inf')
    tnode = Node(txy)
    for node in nodes:
        tx, ty = tnode.x - node.x, tnode.y - node.y
        x, y = node.left.x - node.x, node.left.y - node.y
        d = abs(x * ty - y * tx) / node.dist(node.left)
        if d < dist:
            dist = d
    return dist


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    x, y = getints_line()
    n = getint()
    xys = getints_lines(n)
    return [(x, y), n, xys]


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
0 0
4
100 100
-100 100
-100 -100
100 -100
            ''',
            # EXPECT
            '''\
100
            '''
        ),

        (
            # INPUT
            '''\
10 10
3
0 100
-100 -100
100 -100
            ''',
            # EXPECT
            '''\
31.3049516850
            '''
        ),
        (
            # INPUT
            '''\
34 6
7
-43 -65
-23 -99
54 -68
65 92
16 83
-18 43
-39 2
            ''',
            # EXPECT
            '''\
25.0284205314
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
        art.float_equal(float(iosolve()), float(expect.strip()), 10 ** -6)


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
