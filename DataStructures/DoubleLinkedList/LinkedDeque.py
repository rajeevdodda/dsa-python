from DataStructures.DoubleLinkedList.DoubleLinkedList import _DoubleLinkedList


class LinkedDeque(_DoubleLinkedList):
    def first(self):
        if self.is_empty():
            raise Empty
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty
        return self._trailer._prev._element

    def insert_first(self, element):
        self._insert_between(element, self._header, self._header._next)

    def insert_last(self, element):
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_fist(self):
        if self.is_empty():
            raise Empty
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty
        return self._delete_node(self._trailer._next)


class Empty(Exception):
    pass


d = LinkedDeque()
d.insert_last(3)
d.insert_last(1)
d.insert_first(2)
print(d.first(), d.last())
