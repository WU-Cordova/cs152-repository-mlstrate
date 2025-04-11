# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
from copy import deepcopy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T], data_type: type=object) -> None: 

        ## ERRORS
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting sequence is not a valid sequence type.")
        if starting_sequence == None:
            raise ValueError("Must have a starting sequence. Try Array.empty() to initialize an empty array.")
        if not isinstance(data_type, type):
            raise ValueError(" Data type is not a valid type.")
        for i in range(len(starting_sequence)):
            if not isinstance(starting_sequence[i], data_type):
                raise TypeError("An element of the starting sequence is not an instance of the specified data type.")
        
        ## INITIALIZE ATTRIBUTES
        self.__element_count = len(starting_sequence)   # logical size
        self.__capacity = len(starting_sequence)        # physical size (storage)
        self.__data_type = data_type

        ## CREATE EMPTY ARRAY
        self.__elements = np.empty(self.__element_count, dtype = data_type)

        ## PLACE ELEMENTS IN ARRAY
        for i in range(len(starting_sequence)):
            self.__elements[i] = deepcopy(starting_sequence[i])


    def empty(elements: int=1, data_type: type=object) -> Array:
        if elements < 1:
            raise ValueError("Element amount must be 1 or above. This will not affect the length of the array.")
        starting_sequence: List[T] = []
        for elem in range(elements):
            starting_sequence.append(data_type())
        return Array(starting_sequence, data_type)

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):          # if index
            return self.__elements[index].item() if isinstance(self.__elements[index], np.generic) else self.__elements[index]
        elif isinstance(index, slice):      # if slice
            return Array([elem.item() if isinstance(elem, np.generic) else elem for elem in self.__elements[index]], data_type = self.__data_type)
        else:
            raise TypeError("Argument must be an index or a slice.")
      

    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is not an instance of the specified data type.")
        self.__elements[index] = item

    def grow_array(self) -> None:
        if self.__element_count == self.__capacity:     # if array has reached capacity, double capacity
            if self.__capacity == 0:
                self.__capacity == 1
            else:
                self.__capacity *= 2
            new_array = np.empty(self.__capacity, dtype = self.__data_type)  # create new empty array

            for i in range(len(self)):              # copy over elements
                new_array[i] = deepcopy(self[i])
            self.__elements = deepcopy(new_array)  


    def append(self, data: T) -> None:
        if not isinstance(data, self.__data_type):
            raise TypeError("Item is not an instance of the array's specified data type.")

        self.grow_array()   # will grow array if needed

        ## APPEND ELEMENT
        self.__element_count += 1
        self[len(self) - 1] = deepcopy(data)    # append new element
        self.__elements = deepcopy(self)    # update self.__elements

    
    def append_front(self, data: T) -> None:
        if not isinstance(data, self.__data_type):
            raise TypeError("Item is not an instance of the array's specified data type.")

        self.grow_array()   # will grow array if needed
        
        ## APPEND ELEMENT
        for i in range(len(self)):   # shift everything forward 1 space, thereby leaving space for the element to be appended
            self[i + 1] = deepcopy(self[i])
        self[0] = deepcopy(data)    # append new element to first position
        self.__element_count += 1
        self.__elements = deepcopy(self)


    def shrink_array(self) -> None:
        if self.__element_count <= 0.25 * self.__capacity:  # check if capacity has outgrown elements
            self.__capacity = self.__capacity // 2
            new_array = np.empty(self.__capacity, dtype = self.__data_type)     # create empty array of new size

            for i in range(len(self)):              # copy over elements
                new_array[i] = deepcopy(self[i])
            self.__elements = deepcopy(new_array)


    def pop(self) -> None:
        popped = deepcopy(self[len(self) - 1])  # store the last element somewhere else before it's deleted

        ## DELETE ELEMENT
        self[len(self) - 1] = self.__data_type()   # replace element w/ generic version of the data type
        self.__element_count -= 1
        self.__elements = deepcopy(self)

        self.shrink_array()     # shrink array if needed

        return popped

    
    def pop_front(self) -> None:
        popped = deepcopy(self[0])  # store the first element somewhere else before it's deleted

        ## DELETE ELEMENT
        for i in range(len(self)):   # shift everything back 1, thereby overwriting the first element
            self[i - 1] = deepcopy(self[i])
            # last element is now written twice - in its previous position and back 1 since nothing shifted back to overwrite it
        self.__element_count -= 1
        self[len(self) - 1] = self.__data_type()    # replace 2nd instance of last element w/ generic instance of data type
        self.__elements = deepcopy(self)

        self.shrink_array()     # shrink array if needed

        return popped


    def __len__(self) -> int: 
        return(self.__element_count)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        return self.__elements.all() == other.__elements.all()
        
    def __iter__(self) -> Iterator[T]:
        return(self.__elements.__iter__())

    def __reversed__(self) -> Iterator[T]:
        rev = self.__elements[::-1]
        return(rev.__iter__())


    def __delitem__(self, index: int) -> None:
        for i in range(index, len(self) - 1):   # shift everything after the deleted item back 1, thereby overwriting the deleted item
            self[i - 1] = self[i]
        self.__element_count -= 1

        if self.__element_count <= 0.25 * self.__capacity:  # check if capacity has outgrown elements
            self.__capacity *= 0.5
            new_array = np.empty(self.__capacity, dtype = self.__data_type)     # create empty array of new size
            
            for i in range(len(self)):              # copy over elements
                new_array[i] = deepcopy(self[i])
            self.__elements = deepcopy(new_array)


    def __contains__(self, item: Any) -> bool:
        return item in self.__elements


    def clear(self) -> None:
        self.__element_count = 0
        self.__capacity = 0
        self.__elements = np.empty(self.__element_count, dtype = self.__data_type)
        # raise NotImplementedError('Clear not implemented.')

    def get_capacity(self) -> int:
        return self.__capacity

    def set_element_count(self, num: int) -> None:
        self.__element_count = num

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__element_count}, Physical: {self.__capacity}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')