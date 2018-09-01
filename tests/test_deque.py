import unittest
from deque import Deque
from node import Node


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Deque()

    def test_empty_deque(self):
        self.assertEqual(self.q.get_front(), None)
        self.assertEqual(self.q.get_rear(), None)
        self.assertEqual(self.q.get_front(), self.q.get_rear())
        self.assertEqual(self.q.get_size(), 0)
        self.assertEqual(self.q.remove_front(), None)

    def test_one_element_deque(self):
        q = Deque(1)

        self.assertEqual(q.get_front().get_value(), 1)
        self.assertEqual(q.get_rear().get_value(), 1)
        self.assertEqual(type(q.get_front()), Node)
        self.assertEqual(type(q.get_rear()), Node)
        self.assertEqual(q.get_rear(), q.get_front())

        self.assertEqual(q.get_rear().get_previous(), None)
        self.assertEqual(q.get_rear().get_next(), None)
        self.assertEqual(q.get_front().get_next(), None)
        self.assertEqual(q.get_front().get_previous(), None)
        self.assertEqual(q.get_size(), 1)

    def test_add_front(self):
        for i in range(1, 4):
            self.q.add_front(i)
        self.assertEqual(self.q.get_front().get_value(), 3)
        self.assertEqual(self.q.get_rear().get_next().get_value(), 2)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 2)
        self.assertEqual(self.q.get_size(), 3)

    def test_add_rear(self):
        for i in range(1, 4):
            self.q.add_rear(i)
        self.assertEqual(self.q.get_front().get_value(), 1)
        self.assertEqual(self.q.get_rear().get_next().get_value(), 2)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 2)
        self.assertEqual(self.q.get_size(), 3)

    def test_remove_front(self):
        for i in range(1, 8):
            self.q.add_front(i)
        removed = self.q.remove_front()
        self.assertEqual(self.q.get_size(), 6)
        self.assertEqual(self.q.get_front().get_value(), 6)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 5)
        self.assertEqual(removed.get_value(), 7)
        self.assertEqual(removed.get_previous(), None)

    def test_remove_rear(self):
        for i in range(1, 8):
            self.q.add_rear(i)
        removed = self.q.remove_rear()
        self.assertEqual(self.q.get_size(), 6)
        self.assertEqual(self.q.get_rear().get_value(), 6)
        self.assertEqual(self.q.get_rear().get_previous(), None)
        self.assertEqual(self.q.get_rear().get_next().get_value(), 5)
        self.assertEqual(removed.get_value(), 7)
        self.assertEqual(removed.get_previous(), None)

    def test_add_both(self):
        self.q.add_front(2)
        self.q.add_rear(1)

        self.assertEqual(self.q.get_rear().get_value(), 1)
        self.assertEqual(self.q.get_front().get_value(), 2)
        self.assertEqual(self.q.get_rear().get_next().get_value(), 2)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 1)


if __name__ == "__main__":
    unittest.main()
