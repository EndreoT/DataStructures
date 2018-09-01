from linked_list import DoublyLinkedList


class LinkedListStack(object):
    """Implements a stack using a double linked list internally. O(1) time complexity for push and pop"""

    def __init__(self, top=None):
        self._linked_list = DoublyLinkedList(top)

    def get_linked_list(self):
        return self._linked_list

    def is_empty(self):
        return self.get_linked_list().is_empty()

    def push(self, new_node):
        """"Pushes a new element onto the top of the stack"""
        self._linked_list.position_insert(new_node, -1)

    def pop(self):
        """Removes and returns the first item on the top of the stack"""
        return self.get_linked_list().remove_head()

    def peek(self):
        """Returns the first item on the top of the stack"""
        return self.get_linked_list().head()

    def get_size(self):
        try:
            return self.get_linked_list().get_length()
        except IndexError:
            return 0
