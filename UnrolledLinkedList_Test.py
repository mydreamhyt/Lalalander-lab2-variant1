import unittest
from hypothesis import given
import hypothesis.strategies as st
from UnrolledLinkedList import UnrolledLinkedList
# from UnrolledLinkedList import *
from UnrolledLinkedList import cons, length, remove
from UnrolledLinkedList import member, reverse, concat
from UnrolledLinkedList import to_list, from_list
from UnrolledLinkedList import filter, map, reduce, empty


class TestUnrolledLinkedList(unittest.TestCase):
    def test_api(self):
        empty = UnrolledLinkedList()
        l1 = cons(cons(empty, 1), None)
        l2 = cons(cons(empty, None), 1)
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(cons(empty, 1), None))
        self.assertEqual(length(empty), 0)
        self.assertEqual(length(l1), 2)
        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, None)), "[1]")
        self.assertEqual(str(remove(l1, 1)), "[None]")
        self.assertFalse(member(empty, None))
        self.assertTrue(member(l1, None))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))
        self.assertEqual(l1, reverse(l2))
        self.assertEqual(to_list(l1), [None, 1])
        self.assertEqual(l1, from_list([None, 1]))
        self.assertEqual(concat(l1, l2), from_list([None, 1, 1, None]))
        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [None, 1])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])
        # and also you need:
        # - filter(l, f)
        # - map(l, f)
        # - reduce(l, f)
        # - empty()

    def test_filter(self):
        ull = UnrolledLinkedList()
        for i in range(20):
            ull = cons(ull, i)
        res = filter(ull, lambda x: x % 3 == 0)
        dl = to_list(res)
        self.assertEqual(dl, [1, 3, 5])

    def test_map(self):
        ull = UnrolledLinkedList()
        for i in range(5):
            ull = cons(ull, i)
        ans = map(ull, lambda x: x - 2)
        dl = to_list(ans)
        self.assertEqual(dl, [-2, -1, 0, 1, 2])

    def test_reduce(self):
        ull = UnrolledLinkedList()
        for i in range(1, 6):
            ull = cons(ull, i)
        res = reduce(ull, lambda x, y: x + y, 0)
        self.assertEqual(res, 15)

    def test_empty(self):
        ull = UnrolledLinkedList()
        for i in range(1, 4):
            ull = cons(ull, i)
        res = empty(ull)
        res = to_list(res)
        self.assertEqual(res, [])

    def test_member(self):
        ull = UnrolledLinkedList()
        for i in range(5):
            ull = cons(ull, i)
        res1 = member(ull, 2)
        self.assertEqual(res1, True)
        res2 = member(ull, 5)
        self.assertEqual(res2, False)

    # all finished
    # def test_reversed(self):
    #     ull = UnrolledLinkedList()
    #     for i in range(5):
    #         ull.cons(i)
    #     iter_string = ''
    #     for e in ull.reverse():
    #         iter_string += str(e) + ' '
    #     self.assertEqual(iter_string, '4 3 2 1 0 ')
    #
    # def test_from_list(self):
    #     ull = UnrolledLinkedList()
    #     lst = [1, 3, 5, 7]
    #     res = ull.from_list(lst)
    #     self.assertEqual(str(res), "{[1, 3, 5, 7]}")
    #
    # def test_iterator(self):
    #     ull = UnrolledLinkedList()
    #     for i in range(1, 4):
    #         ull.cons(i)
    #     arr = []
    #     for i in ull.iterator():
    #         arr.append(i)
    #     self.assertEqual(str(arr), "[1, 2, 3]")



    # @given(strategies.integers(), strategies.integers())
    # def test_add_commutative(self, a, b):
    #     self.assertEqual(Foo().add(a, b), Foo().add(b, a))


# if __name__ == '__main__':
#     unittest.main()
