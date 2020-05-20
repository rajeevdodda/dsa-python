class Empty(Exception):
    pass


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        head = self._tail._next
        return head._element

    def enqueue(self, element):
        new_node = self._Node(element, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


c = CircularQueue()
c.enqueue(1)
c.enqueue(2)
print(c.first())
print(c.dequeue())
print(c.first())