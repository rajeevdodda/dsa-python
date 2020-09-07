import ctypes

class DynamicArray:
    """ A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """ Create an empty array."""
        self._n = 0                                                 # count actual elements
        self._capacity = 1                                          # defult array capacity
        self._A = self._make_array(self._capacity)                  # low-level array
    
    def _make_array(self, c):
        """ Return new array with capacity c."""
        return (c * ctypes.py_object)()
    
    def __len__(self):
        """ Return the number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """ Return an element at index k."""
        if not 0 <= k <= self._n :
            raise IndexError('invalid index')
        return self._A[k]                                           # retrieve from array

    
    def append(self, obj):
        """ Add object to end of the array."""
        if self._n == self._capacity:                               # not enough space
            self._resize(self._capacity)
        
        self._A[self._n] = obj
        self._n += 1

    
    def _resize(self, c):                                           # non public utility
        new_array = self._make_array(2 * c)                         # double the capacity
        for i in self._A:
            new_array.append(i)
        
        self._capacity = 2 * c
        self._A = new_array


        



    
