from DataStructures.DoubleLinkedList import DoubleLinkedList


class PositionalList(DoubleLinkedList):
    """A sequential container of elements allowing positional access"""

    # -------------------------- nested Position class --------------------------
    class Position:
        """”””An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node

        def __ne__(self, other):
            return not (self == other)

    # #------------------------------- utility method -------------------------------
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('"p" must be proper position type')

        if p._container is not self:
            raise ValueError("p does not belong to this container")

        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def make_position(self, node):

        """Return Position instance for given node( or None if sentinel)."""

        if node is self.header or node is self.trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)
