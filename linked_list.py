# TODO make single LL

from typing import Union, Any, List


class Node(object):
    """A node object to be used in a linked list."""

    def __init__(self, value: Any, next_node: "Node"=None, previous_node: "Node"=None):
        """
        :param value: Any data type which the node will hold.
        :param next_node: The node's next neighbor.
        :param previous_node: The node's previous neighbor.
        >>> node_2 = Node(2)
        >>> node_1 = Node(1, node_2)
        >>> node_1.get_next()
        node_2
        """
        self._value = value
        self._next = next_node
        self._previous = previous_node

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value: Any) -> None:
        self._value = value

    def get_next(self) -> Union["Node", None]:
        return self._next

    def set_next(self, node: Union["Node", None]) -> None:
        self._next = node

    def get_previous(self) -> Union["Node", None]:
        return self._previous

    def set_previous(self, node: Union["Node", None]) -> None:
        self._previous = node

    def clear_connections(self) -> None:
        self.set_next(None)
        self.set_previous(None)

    def __repr__(self):
        return str(self.get_value())

    def __str__(self):
        return "(" + str(self.get_value()) + ")"


class DoublyLinkedList(object):
    """Linked list implementation in which each node has a next and previous reference."""

    def __init__(self, head: Node=None):
        """
        :param head: The head of the linked list. The type is either a node or none.
        >>> node = Node(0)
        >>> ll = DoublyLinkedList(node)
        >>> ll.head()
        node
        """
        self._head = head
        self._node_set = set()
        if head:
            self._node_set.add(self._head)

    @staticmethod
    def make_node(data) -> Node:
        """Turns the data into a node if it is not already."""
        if type(data) is not Node:
            data = Node(data)
        return data

    def head(self) -> Union[Node, None]:
        return self._head

    def set_head(self, head: Any, make_node=True) -> None:
        """Sets the linked list's head reference."""
        if make_node:
            head = self.make_node(head)
        self._head = head

    def get_node_set(self):
        return self._node_set

    def get_end(self) -> Union[Node, None]:
        """Traverses the linked list and returns the final node unless there is no head"""
        if self.head():
            current = self.head()
            while current.get_next():
                current = current.get_next()
            return current
        return None

    def append(self, data: Any) -> None:
        """Adds a node to the end of the linked list"""
        data = self.make_node(data)
        self._addition_helper(data)
        self.get_node_set().add(data)

    def extend(self, linked_list: "DoublyLinkedList") -> None:
        """Adds a new linked list to the end of self"""
        linked_list_head = linked_list.head()
        current = linked_list_head
        self.get_node_set().add(current)
        while current.get_next():
            current = current.get_next()
            self.get_node_set().add(current)
        self._addition_helper(linked_list_head)

    def bulk_append(self, array: List[Any]) -> None:
        """Appends multiple nodes in a list to the linked list"""
        for data in array:
            data = self.make_node(data)
            self.get_node_set().add(data)
            self.append(data)

    def _addition_helper(self, addition: Node) -> None:
        tail = self.get_end()
        if tail:
            tail.set_next(addition)
            addition.set_previous(tail)
        else:
            self.set_head(addition)
            addition.set_previous(None)

    def search(self, value: Any) -> Node:
        """Searches for the first node with the given value"""
        if self.head():
            current = self.head()
            found = False
            while current and not found:
                if current.get_value() == value:
                    return current
                current = current.get_next()
        raise ValueError(value, "value not in linked list")

    def get_position(self, position: int) -> Node:
        """Returns the node at the given position. The Linked list head is assigned to position 0"""
        if position < 0:
            raise IndexError("Index must be >= 0")
        counter = 0
        current = self.head()
        found = False
        while current and not found:
            if counter == position:
                return current
            else:
                current = current.get_next()
                counter += 1
        raise IndexError("Index out of bounds")

    def node_insert(self, prev_node: Node, new_node: Node) -> None:
        """
        Inserts a node into the linked list in front of a known node.
        Time complexity is O(1) because no searching for the node is needed.
        """
        if prev_node in self.get_node_set():
            next_obj = prev_node.get_next()
            new_node.set_next(next_obj)
            if next_obj:
                next_obj.set_previous(new_node)
            prev_node.set_next(new_node)
            new_node.set_previous(prev_node)
            self.get_node_set().add(new_node)
        else:
            raise KeyError("Node is not in Linked List")

    def position_insert(self, data: Any, position: int=0) -> None:
        """
        Inserts a node at the given position. Inserting at position -1 means the data is the new head.
        Position 0 means inserting between head and head's next node
        """
        data = self.make_node(data)
        self.get_node_set().add(data)
        if position < -1:
            raise IndexError("position must be >= -1")
        elif position == -1:
            if self.head():
                data.set_next(self.head())
                self.head().set_previous(data)
                self.set_head(data)
            else:
                self.set_head(data)
        else:
            current = self.get_position(position)
            next_node = current.get_next()
            data.set_next(next_node)
            if next_node:
                next_node.set_previous(data)
            current.set_next(data)
            data.set_previous(current)

    def remove_head(self) -> Node:
        if self.head():
            head = self.head()
            if not head.get_next():
                self.set_head(None, make_node=False)
            else:
                self.set_head(head.get_next())
                head.get_next().set_previous(None)
            head.set_next(None)
            self.get_node_set().remove(head)
            return head
        raise ValueError("No head exists")

    def remove_tail(self) -> Node:
        if self.head():
            end = self.get_end()
            if end is self.head():
                self.set_head(None, make_node=False)
            else:
                end.get_previous().set_next(None)
            end.set_previous(None)
            self.get_node_set().remove(end)
            return end
        raise ValueError("No tail exists")

    def node_delete(self, node: Node) -> Node:
        """
        Deletes the given node in the linked list.
        Time complexity is O(1) because the linked list does not need to be traversed to find the node.
        """
        if node in self.get_node_set():
            previous = node.get_previous()
            next = node.get_next()
            previous.set_next(next)
            next.set_previous(previous)
            node.clear_connections()
            self.get_node_set().remove(node)
            return node
        raise KeyError("Node not in Linked List")

    def delete(self, value: Any) -> Node:
        """Deletes the first found node with the given value."""
        node = self.search(value)
        if not self.head().get_next():
            # Value is in the head and the linked list size is 1
            self.set_head(None, make_node=False)
            node.set_next(None)
        elif not node.get_previous():
            # Value is in the head and linked list size is > 1
            next_node = node.get_next()
            self.set_head(next_node)
            next_node.set_previous(None)
            node.set_next(None)
        elif not node.get_next():
            # Value is in the tail
            node.get_previous().set_next(None)
            node.set_previous(None)
        else:
            # Value is somewhere else in the linked list
            previous = node.get_previous()
            previous.set_next(node.get_next())
            node.get_next().set_previous(previous)
            node.clear_connections()
        self.get_node_set().remove(node)
        return node

    def reverse_recursive(self):
        if self.head() is not None:
            self.reverse_helper(self.head(), None)

    def reverse_helper(self, current, previous):
        if current.get_next() is None:
            self.set_head(current)
            current.set_next(previous)
            current.set_previous(None)
        else:
            next = current.get_next()
            current.set_next(previous)
            current.set_previous(next)
            self.reverse_helper(next, current)

    def reverse(self) -> None:
        """Reverses the next and previous values for each node. The new head becomes the old tail."""
        current = self.head()
        previous = None
        while current:
            next = current.get_next()
            current.set_previous(next)
            current.set_next(previous)
            previous = current
            current = next
        self.set_head(previous)

    def is_empty(self):
        return self.head() is None

    def get_length(self) -> int:
        """Returns the number of nodes"""
        if self.head():
            current = self.head()
            count = 0
            while current:
                count += 1
                current = current.get_next()
            return count
        raise IndexError("Headless linked list has no length")

    def __getitem__(self, value):
        return self.search(value)

    def __str__(self):
        if not self.head():
            return str(None)
        current = self.head()
        output = []
        while current:
            output.append(str(current))
            current = current.get_next()
        return ", ".join(output)


def main():
    # Test cases
    # Set up some Elements
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)
    e5 = Node(5)
    e6 = Node(6)
    # l2 = DoublyLinkedList(e4)
    z = DoublyLinkedList(e5)
    z.append(e1)
    z.append(e2)
    # print(z)
    # z.delete(5)
    # print(z)
    z.append(e6)
    # print(z.get_node(0))
    print(z)
    # print(z.head().get_next())
    z.reverse()

    print(z)
    # print(z.head().get_next().get_next().get_next().get_next())
    print(z.search(5))
    x = z[5]
    print(x.get_value())
    # print(l2)
    # Start setting up a LinkedList
    # ll = DoublyLinkedList(e1)
    # ll.append(e2)
    # ll.append(e3)
    # print(ll)
    # print(ll.get_node(2))
    # print(ll.search(-1))
    # ll.insert(e4, 43, force=True)

    # ll.extend(l2)


    # print(ll)
    # print(z.is_empty())
    # print(ll.is_empty())
    # ll.reverse()
    # print(ll)
    # print(ll.head())
    # print(ll.get_node(3).get_previous())

    # print(ll.get_node(3))
    # print(ll)
    # print(e3.get_previous())
    # Test get_position
    # Should print 3
    # print(ll.head().get_next().get_next().get_value())
    # Should also print 3
    # print(ll.get_node(1))

    # # Test insert
    # ll.insert(e4, 3)

    # # Should print 4 now
    # print(ll)
    # print(ll.get_node(0))
    # print(ll.get_node(3))
    # # Test delete
    # ll.remove_tail()
    # # Should print 2 now
    # print(ll)
    # # Should print 4 now
    # print(ll.get_length())
    # print(ll.get_node(2))
    # print(ll)
    # print(ll.get_node(1).get_next())
    # print(ll.get_node(1).get_previous())
    # print(ll.get_node(0).get_next())
    # print("size", ll.get_length())
    # print(ll.get_node(2))
    # head = ll.remove_head()
    # print(head)
    # print(head.get_next())
    # print(ll.get_end())
    # print(ll.head().get_previous())
if __name__ == "__main__":
    main()

