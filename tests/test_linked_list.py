import unittest
from linked_list import DoublyLinkedList
from node import Node


class TestNode(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n1.set_next(self.n2)
        self.n1.set_previous(None)
        self.n2.set_previous(self.n1)
        self.n2.set_next(None)

    def test_get_value(self):
        self.assertEqual(self.n1.get_value(), 1)

    def test_getters(self):
        self.assertEqual(self.n1.get_next(), self.n2)
        self.assertEqual(self.n2.get_next(), None)
        self.assertEqual(self.n2.get_previous(), self.n1)

    def test_setters(self):
        self.n2.set_next(self.n3)
        self.n3.set_previous(self.n2)
        self.n3.set_next(None)
        self.assertEqual(self.n2.get_next(), self.n3)
        self.assertEqual(self.n3.get_previous(), self.n2)
        self.assertEqual(self.n3.get_next(), None)

    def test_clear_connections(self):
        self.n2.set_next(self.n3)
        self.n2.clear_connections()
        self.assertEqual(self.n2.get_next(), None)
        self.assertEqual(self.n2.get_previous(), None)


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)

        self.empty_list = DoublyLinkedList()
        self.empty_head = self.empty_list.head()
        self.empty_tail = self.empty_list.get_end()

        self.single_list = DoublyLinkedList(self.n4)
        self.single_head = self.single_list.head()
        self.single_tail = self.single_list.get_end()

        self.linked_list = DoublyLinkedList(self.n1)
        self.linked_list.append(self.n2)
        self.head = self.linked_list.head()
        self.tail = self.linked_list.get_end()

    def test_empty_linked_list(self):
        self.assertRaises(ValueError, self.empty_list.remove_head)

    def test_connections(self):
        self.linked_list.position_insert(self.n3)
        self.assertEqual(self.linked_list.head().get_previous(), None)
        self.assertEqual(self.linked_list.head().get_next(), self.n3)
        self.assertEqual(self.linked_list.get_position(1).get_previous(), self.linked_list.head())
        self.assertEqual(self.linked_list.get_position(1).get_next(), self.linked_list.get_end())
        self.assertEqual(self.linked_list.get_end().get_previous(), self.n3)
        self.assertEqual(self.linked_list.get_end().get_next(), None)

    def test_make_node(self):
        data = 5
        already_node = Node(1)
        node = DoublyLinkedList.make_node(data)
        already_node = DoublyLinkedList.make_node(already_node)

        self.assertEqual(type(node), Node)
        self.assertEqual(type(already_node), Node)

    def test_head(self):
        self.assertEqual(self.empty_head, None)

        self.assertEqual(self.single_head.get_next(), None)
        self.assertEqual(self.single_head.get_previous(), None)

        self.assertEqual(self.head.get_previous(), None)
        self.assertEqual(self.head.get_next(), self.n2)

    def test_set_head(self):
        self.empty_list.set_head(self.n1)
        self.assertEqual(self.empty_list.head(), self.n1)

    def test_node_set(self):
        self.linked_list.append(self.n3)
        self.assertEqual(len(self.linked_list.get_node_set()), 3)

    def test_tail(self):
        self.assertEqual(self.empty_tail, None)

        self.assertEqual(self.single_tail.get_next(), None)
        self.assertEqual(self.single_tail.get_previous(), None)

        self.assertEqual(self.tail.get_previous(), self.n1)
        self.assertEqual(self.tail.get_next(), None)

    def test_get_tail(self):
        self.assertEqual(self.tail, self.n2)

    def test_append(self):
        self.linked_list.append(self.n3)
        self.assertEqual(self.linked_list.get_length(), 3)
        self.assertEqual(self.linked_list.get_end().get_next(), None)
        self.assertEqual(self.linked_list.get_end().get_previous(), self.n2)
        self.assertEqual(self.linked_list.head().get_next().get_next(), self.n3)
        self.assertEqual(len(self.linked_list.get_node_set()), 3)

    def test_extend(self):
        self.linked_list.extend(self.single_list)
        self.assertEqual(self.linked_list.get_end().get_next(), None)
        self.assertEqual(self.linked_list.get_end().get_previous(), self.n2)
        self.assertEqual(self.n2.get_next(), self.n4)
        self.assertEqual(self.linked_list.get_length(), 3)
        self.assertEqual(len(self.linked_list.get_node_set()), 3)

    def test_bulk_append(self):
        addition = [2, 4, -3, 3.4, Node(0)]
        self.linked_list.bulk_append(addition)
        self.assertEqual(type(self.linked_list.get_position(3)), Node)
        self.assertEqual(type(self.linked_list.get_position(5)), Node)
        self.assertEqual(self.linked_list.get_length(), 7)
        self.assertEqual(self.linked_list.get_position(1).get_next().get_value(), 2)
        self.assertEqual(self.linked_list.get_position(2).get_next().get_value(), 4)
        self.assertEqual(self.linked_list.get_position(2).get_previous(), self.n2)
        self.assertEqual(type(self.linked_list.get_end()), Node)
        self.assertEqual(len(self.linked_list.get_node_set()), 7)

    def test_search(self):
        self.linked_list.append(self.n3)
        self.linked_list.append(self.n5)

        self.assertRaises(ValueError, self.empty_list.search, 1)

        self.assertEqual(self.single_list.search(4), self.n4)

        self.assertEqual(self.linked_list.search(5), self.n5)
        self.assertRaises(ValueError, self.linked_list.search, 0)

    def test_get_position(self):
        self.linked_list.append(self.n3)
        self.linked_list.append(self.n5)

        self.assertRaises(IndexError, self.empty_list.get_position, 0)

        self.assertEqual(self.single_list.get_position(0), self.n4)

        self.assertEqual(self.linked_list.get_position(3), self.n5)
        self.assertRaises(IndexError, self.linked_list.get_position, 4)
        self.assertRaises(IndexError, self.linked_list.get_position, -1)

    def test_node_insert(self):
        self.linked_list.node_insert(self.n1, self.n3)
        self.assertEqual(self.linked_list.head().get_next(), self.n3)
        self.assertEqual(self.linked_list.get_end().get_previous(), self.n3)
        self.assertEqual(self.n3.get_next(), self.n2)
        self.assertEqual(len(self.linked_list.get_node_set()), 3)
        self.assertTrue(self.n3 in self.linked_list.get_node_set())

    def test_position_insert(self):
        self.empty_list.position_insert(3, -1)
        self.single_list.position_insert(0, 0)
        self.linked_list.append(self.n5)
        self.linked_list.position_insert(8, 1)

        self.assertEqual(self.empty_list.get_length(), 1)
        self.assertEqual(self.empty_list.head().get_next(), None)
        self.assertEqual(self.empty_list.head().get_previous(), None)
        self.assertEqual(len(self.empty_list.get_node_set()), 1)

        self.assertEqual(self.single_list.get_length(), 2)
        self.assertEqual(self.single_list.head().get_next().get_value(), 0)
        self.assertEqual(self.single_list.get_end().get_previous(), self.n4)
        self.assertEqual(self.single_list.get_end().get_next(), None)
        self.assertEqual(len(self.single_list.get_node_set()), 2)

        self.assertEqual(self.linked_list.get_length(), 4)
        self.assertEqual(self.linked_list.get_position(1).get_next().get_value(), 8)
        self.assertEqual(self.linked_list.get_end().get_previous().get_value(), 8)
        self.assertEqual(self.linked_list.get_position(2).get_next(), self.n5)
        self.assertEqual(self.linked_list.get_position(2).get_previous(), self.n2)
        self.assertEqual(len(self.linked_list.get_node_set()), 4)

        self.linked_list.position_insert(-6, -1)
        self.assertEqual(self.linked_list.head().get_next(), self.n1)
        self.assertEqual(self.linked_list.head().get_previous(), None)
        self.assertEqual(len(self.linked_list.get_node_set()), 5)

    def test_remove_head(self):
        self.single_list.remove_head()
        self.linked_list.remove_head()

        self.assertRaises(ValueError, self.empty_list.remove_head)

        self.assertEqual(self.single_list.head(), None)
        self.assertEqual(self.n4.get_next(), None)
        self.assertEqual(len(self.single_list.get_node_set()), 0)

        self.assertEqual(self.linked_list.head(), self.n2)
        self.assertEqual(self.n2.get_next(), None)
        self.assertEqual(self.n2.get_previous(), None)
        self.assertEqual(len(self.linked_list.get_node_set()), 1)

    def test_remove_tail(self):
        self.single_list.remove_tail()
        self.linked_list.remove_tail()

        self.assertRaises(ValueError, self.empty_list.remove_tail)

        self.assertEqual(self.single_list.head(), None)
        self.assertEqual(self.n4.get_next(), None)
        self.assertEqual(len(self.single_list.get_node_set()), 0)

        self.assertEqual(self.linked_list.head(), self.n1)
        self.assertEqual(self.n1.get_next(), None)
        self.assertEqual(self.n1.get_previous(), None)
        self.assertEqual(len(self.linked_list.get_node_set()), 1)

    def test_node_delete(self):
        self.linked_list.append(self.n3)
        node = self.linked_list.node_delete(self.n2)

        self.assertEqual(self.linked_list.get_length(), 2)
        self.assertEqual(node, self.n2)
        self.assertEqual(self.n1.get_next(), self.n3)
        self.assertEqual(self.n3.get_previous(), self.n1)
        self.assertEqual(len(self.linked_list.get_node_set()), 2)

    def test_delete(self):
        self.single_list.delete(4)
        self.linked_list.delete(1)

        self.assertRaises(ValueError, self.empty_list.delete, 3)

        self.assertRaises(IndexError, self.single_list.get_length)
        self.assertEqual(self.single_list.head(), None)
        self.assertEqual(len(self.single_list.get_node_set()), 0)

        self.assertEqual(self.linked_list.get_length(), 1)
        self.assertEqual(self.linked_list.get_position(0).get_next(), None)
        self.assertEqual(self.linked_list.get_end().get_previous(), None)
        self.assertRaises(ValueError, self.linked_list.delete, 7)
        self.assertEqual(len(self.linked_list.get_node_set()), 1)

    def test_is_empty(self):
        self.assertEqual(self.empty_list.is_empty(), True)
        self.assertEqual(self.single_list.is_empty(), False)
        self.assertEqual(self.linked_list.is_empty(), False)

    def test_reverse_recursive(self):
        self.linked_list.append(self.n3)
        self.linked_list.reverse_recursive()
        self.assertEqual(self.linked_list.head().get_next(), self.n2)
        self.assertEqual(self.linked_list.head().get_previous(), None)
        self.assertEqual(self.linked_list.get_position(1).get_next(), self.n1)
        self.assertEqual(self.linked_list.get_position(1).get_previous(), self.n3)
        self.assertEqual(self.linked_list.get_position(2).get_next(), None)
        self.assertEqual(self.linked_list.get_position(2).get_previous(), self.n2)

    def test_reverse(self):
        self.linked_list.append(self.n3)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.head().get_next(), self.n2)
        self.assertEqual(self.linked_list.head().get_previous(), None)
        self.assertEqual(self.linked_list.get_position(1).get_next(), self.n1)
        self.assertEqual(self.linked_list.get_position(1).get_previous(), self.n3)
        self.assertEqual(self.linked_list.get_position(2).get_next(), None)
        self.assertEqual(self.linked_list.get_position(2).get_previous(), self.n2)

    def test_get_length(self):
        self.linked_list.append(self.n3)
        self.linked_list.append(self.n5)

        self.assertRaises(IndexError, self.empty_list.get_length)
        self.assertEqual(self.single_list.get_length(), 1)
        self.assertEqual(self.linked_list.get_length(), 4)


if __name__ == "__main__":
    unittest.main()
