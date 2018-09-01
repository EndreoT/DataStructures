import unittest
from binary_search_tree import BinarySearchTree
from tree_node import TreeNode
#            6
#         /     \
#        2       9
#       / \     / \
#      1   4   8  15
#                /  \
#               13  18
#              /
#             11
#              \
#               12


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()
        node_list = [6, 2, 1, 4, 9, 8, 15, 13, 11, 18, 12]
        for i in node_list:
            self.tree.put(i, i)
        self.root = self.tree.get_root()

    def test_bst_property(self):
        BinarySearchTree.has_bst_property(self.root)
        node = self.tree.get(1)
        node.set_left_child(TreeNode(5, 5))
        self.assertRaises(ValueError, BinarySearchTree.has_bst_property, self.root)

    def test_tree_structure(self):
        self.assertEqual(self.tree.get_size(), 11)
        self.assertEqual(self.root.get_value(), 6)
        self.assertEqual(self.root.get_right_child().get_key(), 9)
        self.assertTrue(self.root.has_both_children())
        self.assertEqual(self.root.get_left_child().get_key(), 2)
        self.assertTrue(self.root.get_right_child().has_both_children())
        self.assertTrue(self.root.get_right_child().get_right_child().has_both_children())
        self.assertEqual(self.root.get_right_child().get_right_child().get_min().get_value(), 11)
        self.assertEqual(self.tree.get(11).get_right_child().get_value(), 12)

    def test_put(self):
        self.tree.put(7, 7)
        self.assertEqual(self.tree.get_size(), 12)
        self.assertEqual(self.root.get_right_child().get_left_child().get_left_child().get_key(), 7)
        self.tree.put(3, 3)
        self.assertEqual(self.tree.get_size(), 13)
        self.assertEqual(self.root.get_left_child().get_right_child().get_left_child().get_key(), 3)
        BinarySearchTree.has_bst_property(self.root)

    def test_get(self):
        val_1 = self.tree.get(11)
        self.assertEqual(val_1.get_parent().get_value(), 13)
        self.assertEqual(val_1.get_right_child().get_key(), 12)
        val_2 = self.tree.get(15)
        self.assertEqual(val_2.get_parent().get_value(), 9)
        self.assertTrue(val_2.has_both_children())

    def test_find_min(self):
        self.assertEqual(self.root.get_min().get_key(), 1)
        self.assertEqual(self.root.get_min().get_parent().get_key(), 2)
        self.assertEqual(self.root.get_right_child().get_right_child().get_min().get_key(), 11)

    def test_delete_leaf(self):
        self.tree.delete(12)
        self.assertEqual(self.tree.get_size(), 10)
        self.assertFalse(self.tree.get(11).has_any_children())
        self.tree.delete(18)
        self.assertEqual(self.tree.get_size(), 9)
        self.assertEqual(self.root.get_right_child().get_right_child().get_right_child(), None)
        self.assertEqual(self.root.get_right_child().get_right_child().get_left_child().get_key(), 13)
        BinarySearchTree.has_bst_property(self.root)

    def test_delete_node_with_one_child(self):
        self.tree.delete(13)
        self.assertEqual(self.tree.get_size(), 10)
        self.assertEqual(self.tree.get(15).get_left_child().get_key(), 11)
        self.assertEqual(self.tree.get(11).get_parent().get_key(), 15)
        BinarySearchTree.has_bst_property(self.root)

    def test_delete_root_with_only_one_child(self):
        tree = BinarySearchTree()
        tree.put(1, 1)
        tree.put(2, 2)
        tree.put(3, 3)
        tree.delete(1)
        self.assertEqual(tree.get_size(), 2)
        self.assertEqual(tree.get_root().get_value(), 2)
        self.assertEqual(tree.get_root().get_right_child().get_key(), 3)
        BinarySearchTree.has_bst_property(self.root)

    def test_delete_node_with_both_children(self):
        self.tree.delete(2)
        self.assertEqual(self.tree.get_size(), 10)
        self.assertEqual(self.tree.get(4).get_left_child().get_key(), 1)
        self.assertEqual(self.tree.get(4).get_parent().get_key(), 6)
        self.assertEqual(self.tree.get(1).get_parent().get_key(), 4)
        BinarySearchTree.has_bst_property(self.root)

        self.tree.delete(9)
        self.assertEqual(self.tree.get_size(), 9)
        self.assertEqual(self.tree.get(11).get_right_child().get_key(), 15)
        self.assertTrue(self.tree.get(11).has_both_children())
        self.assertEqual(self.tree.get(11).get_parent().get_key(), 6)
        self.assertEqual(self.tree.get(12).get_parent().get_key(), 13)
        self.assertEqual(self.tree.get(13).get_left_child().get_key(), 12)
        BinarySearchTree.has_bst_property(self.root)

    def test_delete_root_with_both_children(self):
        self.tree.delete(6)
        self.assertEqual(self.tree.get_size(), 10)
        self.assertEqual(self.root.get_key(), 8)
        self.assertEqual(self.root.get_right_child().get_key(), 9)
        self.assertTrue(self.tree.get(9).get_left_child(), None)
        BinarySearchTree.has_bst_property(self.root)

    def test_tree_height(self):
        tree_height = self.tree.get_tree_height()
        self.assertEqual(tree_height, 6)
        self.assertEqual(self.tree.get_node_height(self.tree.get(15)), 4)


if __name__ == "__main__":
    unittest.main()
