#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io


class Member():
    def __init__(self, member_id, subordinates):
        self.member_id = member_id
        self.subordinates = subordinates

    def pay(self):
        ps = list(map(lambda m: m.pay(), self.subordinates))
        if ps:
            return min(ps) + max(ps) + 1
        else:
            return 1

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Member(id: {}, subs: {})'.format(
            self.member_id, str(self.subordinates))

    @classmethod
    def create_member_tree(cls, id_with_superiors):
        ms = []
        for member_id, superior in id_with_superiors:
            m = cls.create_member(member_id, id_with_superiors)
            ms.append(m)
        return ms

    @classmethod
    def create_member(cls, member_id, id_with_superiors):
        return Member(member_id,
                      [cls.create_member(m_id, id_with_superiors)
                       for (m_id, sup_id) in id_with_superiors
                       if sup_id and sup_id == member_id])


def solve(n, bs):
    '''
    bs: List[int(上司の社員番号)]
    '''
    assert 1 <= n <= 20
    assert len(bs) == n - 1

    id_with_superiors = list(enumerate(bs, start=2)) + [(1, None)]
    ms = Member.create_member_tree(id_with_superiors)
    assert(len(Member.create_member_tree(id_with_superiors)) == n)

    president = ms[-1]
    return president.pay()


def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getint_lines(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n = getint()
    return [n, getint_lines(n - 1)]


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
1
1
1
            ''',
            # EXPECT
            '''\
3
            '''
        ),

        (
            # INPUT
            '''\
7
1
1
2
2
3
3
            ''',
            # EXPECT
            '''\
7
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

