from typing import Union
from node import Node


class Deque:
    """
    Implements a deque which uses a doubly linked list implicitly. This queue keeps both front and rear
    references so than adding and removing from both ends occurs in O(1).
    """
    def __init__(self, head=None):
        if head:
            head = Node.make_node(head)
        self._front = head
        self._rear = head
        if not head:
            self._size = 0
        else:
            self._size = 1

    def get_front(self) -> Union[Node, None]:
        return self._front

    def set_front(self, node) -> None:
        self._front = node

    def get_rear(self) -> Union[Node, None]:
        return self._rear

    def set_rear(self, node) -> None:
        self._rear = node

    def add_rear(self, data) -> None:
        """Adds an item to the rear of the deque."""
        data = Node.make_node(data)
        if self.get_rear():
            self.get_rear().set_previous(data)
        data.set_next(self.get_rear())
        self.set_rear(data)
        self._size += 1
        if self.get_size() == 1:
            self.set_front(data)

    def remove_rear(self) -> Union[Node, None]:
        """Removes and returns the first item at the rear of the deque"""
        if self.get_size() == 0:
            return None
        removed = self.get_rear()
        self.set_rear(removed.get_next())
        self.get_rear().set_previous(None)
        removed.clear_connections()
        self._size -= 1
        return removed

    def add_front(self, data) -> None:
        """Adds an item to the front of the deque."""
        data = Node.make_node(data)
        if self.get_front():
            self.get_front().set_next(data)
        data.set_previous(self.get_front())
        self.set_front(data)
        self._size += 1
        if self.get_size() == 1:
            self.set_rear(data)

    def remove_front(self) -> Union[Node, None]:
        """Removes and returns the first item at the front of the deque"""
        if self.get_size() == 0:
            return None
        removed = self.get_front()
        self.set_front(removed.get_previous())
        self.get_front().set_next(None)
        removed.clear_connections()
        self._size -= 1
        return removed

    def is_empty(self) -> bool:
        if self.get_front():
            return False
        return True

    def get_size(self) -> int:
        return self._size

    def __str__(self):
        return "Rear: " + str(self.get_rear()) + ", Front: " + str(self.get_front())
