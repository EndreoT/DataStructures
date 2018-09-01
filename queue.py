from typing import Union

from linked_list import DoublyLinkedList
from node import Node


class Queue:
    """
    Implements a queue which uses a doubly linked list implicitly. This queue keeps both front and rear
    references so than enqueueing and dequeueing occur in O(1). The queue rear is the head of the linked
    list, while the queue front is the tail of the linked list.
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

    def enqueue(self, data) -> None:
        """Adds an item to the rear of the queue."""
        data = Node.make_node(data)
        if self.get_rear():
            self.get_rear().set_previous(data)
        data.set_next(self.get_rear())
        self.set_rear(data)
        self._size += 1
        if self.get_size() == 1:
            self.set_front(data)

    def dequeue(self) -> Union[Node, None]:
        """Removes and returns the first item at the front of the queue"""
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


class LinkedlistQueue:
    """
    Implements a queue which uses a doubly linked list explicitly internally. This queue keeps both front and rear
    references so than enqueueing and dequeueing occur in O(1). The queue rear is the head of the linked
    list, while the queue front is the tail of the linked list.
    """

    def __init__(self, head=None):
        self._linked_list = DoublyLinkedList(head)
        self._front = self._linked_list.head()
        self._rear = self._linked_list.get_end()
        if not head:
            self._size = 0
        else:
            self._size = self.get_linked_list().get_length()

    def get_linked_list(self) -> DoublyLinkedList:
        return self._linked_list

    def get_front(self) -> Union[Node, None]:
        return self._front

    def set_front(self, node) -> None:
        self._front = node

    def get_rear(self) -> Union[Node, None]:
        return self._rear

    def set_rear(self, node) -> None:
        self._rear = node

    def enqueue(self, data) -> None:
        """Adds an item to the rear of the queue."""
        data = DoublyLinkedList.make_node(data)
        self._linked_list.position_insert(data, -1)
        self.set_rear(self._linked_list.head())
        self._size += 1
        if self.get_size() == 1:
            self.set_front(data)

    def dequeue(self) -> Node:
        """Removes and returns the first item at the front of the queue"""
        removed = self.get_front()
        new_front = removed.get_previous()
        self.set_front(new_front)
        new_front.set_next(None)
        removed.clear_connections()
        self._size -= 1
        return removed

    def is_empty(self) -> bool:
        return self.get_linked_list().is_empty()

    def get_size(self) -> int:
        return self._size

    def __str__(self):
        return str(self.get_linked_list())
