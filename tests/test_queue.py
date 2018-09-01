import unittest
from queue import Queue, LinkedlistQueue
from node import Node


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_empty_queue(self):
        self.assertEqual(self.q.get_front(), None)
        self.assertEqual(self.q.get_rear(), None)
        self.assertEqual(self.q.get_front(), self.q.get_rear())
        self.assertEqual(self.q.get_size(), 0)
        self.assertEqual(self.q.dequeue(), None)

    def test_one_element_queue(self):
        q = Queue(1)

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

    def test_enqueue(self):
        for i in range(1, 4):
            self.q.enqueue(i)
        self.assertEqual(self.q.get_front().get_value(), 1)
        self.assertEqual(self.q.get_rear().get_next().get_value(), 2)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 2)
        self.assertEqual(self.q.get_size(), 3)

    def test_deueue(self):
        for i in range(1, 8):
            self.q.enqueue(i)
        removed = self.q.dequeue()
        self.assertEqual(self.q.get_size(), 6)
        self.assertEqual(self.q.get_front().get_value(), 2)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 3)
        self.assertEqual(removed.get_value(), 1)
        self.assertEqual(removed.get_previous(), None)


class TestLinkedListQueue(unittest.TestCase):

    def setUp(self):
        self.q = LinkedlistQueue()

    def test_empty_queue(self):
        self.assertEqual(self.q.get_front(), None)
        self.assertEqual(self.q.get_rear(), None)
        self.assertEqual(self.q.get_front(), self.q.get_rear())
        self.assertEqual(self.q.get_size(), 0)

    def test_one_element_queue(self):
        q = LinkedlistQueue(1)

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

    def test_enqueue(self):
        for i in range(1, 4):
            self.q.enqueue(i)
        self.assertEqual(self.q.get_front().get_value(), 1)
        self.assertEqual(self.q.get_rear().get_next().get_value(), 2)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 2)
        self.assertEqual(self.q.get_size(), 3)

    def test_deueue(self):
        for i in range(1, 8):
            self.q.enqueue(i)
        removed = self.q.dequeue()
        self.assertEqual(self.q.get_size(), 6)
        self.assertEqual(self.q.get_front().get_value(), 2)
        self.assertEqual(self.q.get_front().get_next(), None)
        self.assertEqual(self.q.get_front().get_previous().get_value(), 3)
        self.assertEqual(removed.get_value(), 1)
        self.assertEqual(removed.get_previous(), None)


if __name__ == "__main__":
    unittest.main()
