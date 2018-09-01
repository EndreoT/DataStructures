from typing import Any, Union


class Node(object):
    """A doubly lined node to be used in a linked list."""

    def __init__(self, value: Any, next_node: "Node"=None, previous_node: "Node"=None):
        """
        :param value: Any data type which the node will hold.
        :param next_node: The node's next neighbor.
        :param previous_node: The node's previous neighbor.
        >>> node_2 = Node(2)
        >>> node_1 = Node(1, node_2)
        >>> node_2 == node_1.get_next()
        True
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

    @staticmethod
    def make_node(data) -> "Node":
        """Turns the data into a node if it is not already."""
        if type(data) is not Node:
            data = Node(data)
        return data

    def __repr__(self):
        return str(self.get_value())

    def __str__(self):
        return "(" + str(self.get_value()) + ")"
