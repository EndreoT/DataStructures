from typing import Union
from tree_node import TreeNode


class BinaryTree:

    def __init__(self):
        self._root = None
        self._size = 0

    def get_root(self) -> Union[TreeNode, None]:
        return self._root

    def set_root(self, node) -> None:
        self._root = node

    def get_size(self) -> int:
        return self._size

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self.get_size() > 0

    def __iter__(self):
        return self._root.__iter__()

    def get_tree_height(self) -> int:
        return TreeNode.get_height(self._root)

    @staticmethod
    def get_node_height(node: TreeNode):
        return TreeNode.get_height(node)

    def breadth_first_search(self):
        return TreeNode.breadth_first_search(self._root)

    def preoder_traversal(self):
        return TreeNode.preorder_traversal(self._root, [])

    def inorder_traversal(self):
        return TreeNode.inorder_traversal(self._root, [])

    def postorder_traversal(self):
        return TreeNode.postorder_traversal(self._root, [])
