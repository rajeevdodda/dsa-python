class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._next = next
            self._element = element

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._head._element

    def enqueue(self, element):
        new_node = self._Node(element, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty
        else:
            result = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
            return result


class Empty(Exception):
    pass


q = LinkedQueue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(len(q))
