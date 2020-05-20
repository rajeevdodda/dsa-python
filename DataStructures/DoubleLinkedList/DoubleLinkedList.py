class _DoubleLinkedList:
    class _Node:
        def __init__(self, element, prev, nex):
            self._element = element
            self._prev = prev
            self._next = nex

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        new_element = self._Node(element, predecessor, successor)
        predecessor._next = new_element
        successor._prev = new_element
        self._size += 1
        return new_element

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node
        node._prev = node._next = node._element = None
        return element



