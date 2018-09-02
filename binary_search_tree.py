from binary_tree import BinaryTree
from tree_node import TreeNode


class BinarySearchTree(BinaryTree):
    """Non-self balancing binary search tree."""

    def __init__(self):
        super().__init__()

    def put(self, key, value) -> None:
        if not self.get_root():
            self.set_root(TreeNode(key, value))
        else:
            self._put_helper(key, value, self.get_root())
        self._size += 1

    def _put_helper(self, key, value, node: TreeNode) -> None:
        if key < node.get_key():
            if node.get_left_child():
                self._put_helper(key, value, node.get_left_child())
            else:
                node.set_left_child(TreeNode(key, value, parent=node))
        elif key > node.get_key():
            if node.get_right_child():
                self._put_helper(key, value, node.get_right_child())
            else:
                node.set_right_child(TreeNode(key, value, parent=node))
        else:
            node.set_value(value)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key) -> TreeNode:
        if not self.get_root():
            raise KeyError
        else:
            return self._get_helper(key, self.get_root())

    def _get_helper(self, key, node: TreeNode) -> TreeNode:
        output = None
        if node.get_key() == key:
            output = node
        elif node.get_key() > key and node.get_left_child():
            output = self._get_helper(key, node.get_left_child())
        elif node.get_key() < key and node.get_right_child():
            output = self._get_helper(key, node.get_right_child())
        elif not node:
            raise KeyError
        return output

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        try:
            self.get(key)
        except KeyError:
            return False
        return True

    def find_min(self) -> TreeNode:
        return self.get_root().get_min()

    def delete(self, key) -> None:
        if self.get_size() == 1 and self.get_root().get_key() == key:
            # Only root exists and has the key
            removed = self.get_root()
            self.set_root(None)
            self._size -= 1
            removed.clear_connections()
        elif self.get_size() > 1:
            node_to_remove = self.get(key)
            self._remove(node_to_remove)
            self._size -= 1
        else:
            raise KeyError

    def _remove(self, node_to_remove: TreeNode):
        if node_to_remove.is_leaf():
            if node_to_remove.is_left_child():
                node_to_remove.get_parent().set_left_child(None)
            else:
                node_to_remove.get_parent().set_right_child(None)
            node_to_remove.clear_connections()
        elif node_to_remove.has_only_one_child():
            if node_to_remove.get_left_child():
                self._remove_if_only_one_child(node_to_remove, node_to_remove.get_left_child)
            else:
                self._remove_if_only_one_child(node_to_remove, node_to_remove.get_right_child)
        else:
            successor = node_to_remove.get_successor()
            node_to_remove.set_key(successor.get_key())
            node_to_remove.set_value(successor.get_value())
            successor.remove_self()

    def _remove_if_only_one_child(self, node_to_remove, child_of_node_to_remove):
        parent = node_to_remove.get_parent()
        if node_to_remove.is_left_child():
            parent.set_left_child(child_of_node_to_remove())
            child_of_node_to_remove().set_parent(parent)
        elif node_to_remove.is_right_child():
            parent.set_right_child(child_of_node_to_remove())
            child_of_node_to_remove().set_parent(parent)
        else:
            # Node to remove is root and has only one child
            prev_root = self.get_root()
            self.set_root(child_of_node_to_remove())
            child_of_node_to_remove().set_parent(None)
            prev_root.clear_connections()

    @staticmethod
    def has_bst_property(node) -> None:
        if node:
            if node.get_left_child() and node.get_left_child().get_key() > node.get_key():
                raise ValueError
            if node.get_right_child() and node.get_right_child().get_key() < node.get_key():
                raise ValueError
            BinarySearchTree.has_bst_property(node.get_left_child())
            BinarySearchTree.has_bst_property(node.get_right_child())
