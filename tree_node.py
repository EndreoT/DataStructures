from typing import Union, Any, List


class TreeNode:

    def __init__(self, key: int, value: Any, left: "TreeNode"=None, right: "TreeNode"=None, parent: "TreeNode"=None):
        self._key = key
        self._value = value
        self._left_child = left
        self._right_child = right
        self._parent = parent

    def get_key(self) -> int:
        return self._key

    def set_key(self, key) -> None:
        self._key = key

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value) -> None:
        self._value = value

    def get_left_child(self) -> "TreeNode":
        return self._left_child

    def get_right_child(self) -> "TreeNode":
        return self._right_child

    def get_parent(self) -> "TreeNode":
        return self._parent

    def set_right_child(self, data: Union["TreeNode", None]) -> None:
        self._right_child = data

    def set_left_child(self, data: Union["TreeNode", None]) -> None:
        self._left_child = data

    def set_parent(self, data: Union["TreeNode", None]) -> None:
        self._parent = data

    def is_left_child(self) -> bool:
        return self.get_parent() and self.get_parent().get_left_child() == self

    def is_right_child(self) -> bool:
        return self.get_parent() and self.get_parent().get_right_child() == self

    def is_root(self) -> bool:
        return not self.get_parent()

    def is_leaf(self) -> bool:
        return not (self.get_left_child() or self.get_right_child())

    def has_any_children(self) -> bool:
        if self.get_left_child() or self.get_right_child():
            return True
        return False

    def has_both_children(self) -> bool:
        if self.get_left_child() and self.get_right_child():
            return True
        return False

    def has_only_one_child(self) -> bool:
        return len([i for i in (self.get_left_child(), self.get_right_child()) if i]) == 1

    def clear_connections(self) -> None:
        self.set_left_child(None)
        self.set_right_child(None)
        self.set_parent(None)

    @staticmethod
    def get_height(node) -> int:
        if not node:
            return 0
        else:
            left_depth = TreeNode.get_height(node.get_left_child())
            right_depth = TreeNode.get_height(node.get_right_child())
            max_height = max(left_depth, right_depth) + 1
            return max_height

    @staticmethod
    def breadth_first_search(node) -> List["TreeNode"]:
        """Uses queue"""
        array = list()
        queue = list()
        queue.append(node)
        while len(queue) > 0:
            temp_node = queue.pop(0)
            array.append(temp_node)
            if temp_node.get_left_child():
                queue.append(temp_node.get_left_child())
            if temp_node.get_right_child():
                queue.append(temp_node.get_right_child())
        return array

    @staticmethod
    def preorder_traversal(node: "TreeNode", array) -> List["TreeNode"]:
        if node:
            array.append(node)
            TreeNode.preorder_traversal(node.get_left_child(), array)
            TreeNode.preorder_traversal(node.get_right_child(), array)
        return array

    @staticmethod
    def inorder_traversal(node: "TreeNode", array) -> List["TreeNode"]:
        if node:
            TreeNode.inorder_traversal(node.get_left_child(), array)
            array.append(node)
            TreeNode.inorder_traversal(node.get_right_child(), array)
        return array

    @staticmethod
    def postorder_traversal(node: "TreeNode", array) -> List["TreeNode"]:
        if node:
            TreeNode.postorder_traversal(node.get_left_child(), array)
            TreeNode.postorder_traversal(node.get_right_child(), array)
            array.append(node)
        return array

    def get_successor(self) -> "TreeNode":
        successor = self.get_right_child().get_min()
        return successor

    def get_min(self) -> "TreeNode":
        current = self
        while current.get_left_child():
            current = current.get_left_child()
        return current

    def remove_self(self) -> None:
        if self.is_leaf():
            self.get_parent().set_right_child(None)
        else:
            # node to be removed has right child only
            child = self.get_right_child()
            child.set_parent(self.get_parent())
            self.get_parent().set_left_child(child)
        self.clear_connections()
