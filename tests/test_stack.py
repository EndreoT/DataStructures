import unittest
from stack import LinkedListStack
from node import Node


class TestStack(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)

        self.stack = LinkedListStack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(self.n1)

    def test_peek(self):
        item = self.stack.peek()
        self.assertEqual(item, self.n1)

    def test_push(self):
        self.assertEqual(self.stack.get_size(), 3)
        self.stack.push(self.n2)
        self.assertEqual(self.stack.get_size(), 4)

    def test_pop(self):
        item = self.stack.pop()
        self.assertEqual(item, self.n1)

    def test_is_empty(self):
        empty_stack = LinkedListStack()
        self.assertEqual(empty_stack.is_empty(), True)
        self.assertEqual(self.stack.is_empty(), False)

    def test_get_size(self):
        empty_stack = LinkedListStack()
        self.assertEqual(empty_stack.get_size(), 0)
        self.assertEqual(self.stack.get_size(), 3)


if __name__ == "__main__":
    unittest.main()
