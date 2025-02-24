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

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 

        ## ERRORS
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting sequence is not a valid sequence type.")
        if not isinstance(data_type, type):
            raise ValueError("Data type is not a valid type.")
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


    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):          # if index
            return self.__elements[index]
        elif isinstance(index, slice):      # if slice
            return [elem for elem in self.__elements[index]]
        else:
            raise TypeError("Argument must be an index or a slice.")
      
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is not an instance of the specified data type.")
        self.__elements[index] = item

    ##
    def append(self, data: T) -> None:
        if not isinstance(data, self.__data_type):
            raise TypeError("Item is not an instance of the array's specified data type.")

        ## CREATE EMPTY ARRAY OF DOUBLED SIZE
        new_size = np.empty(2 * self.__capacity, dtype = self.__data_type)

        ## ADD ELEMENTS
        for i in range(len(self)):              # add previous elements
            new_size[i] = deepcopy(self[i])
        new_size[len(self)] = deepcopy(data)    # append new element
        self.__elements = deepcopy(new_size)    # update self.__elements
        
        ## UPDATE COUNTS
        self.__element_count += 1
        self.__capacity = len(self)

        print("test")
        print(repr(self))
        # raise NotImplementedError('Append not implemented.')


    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')
    ##

    def __len__(self) -> int: 
        return(self.__element_count)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        else:
            return self.__elements.all() == other.__elements.all()
    
    def __iter__(self) -> Iterator[T]:
        return(self.__elements.__iter__())

    def __reversed__(self) -> Iterator[T]:
        rev = self.__elements[::-1]
        return(rev.__iter__())

    ##
    def __delitem__(self, index: int) -> None:
        raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        raise NotImplementedError('Clear not implemented.')
    ##

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__element_count}, Physical: {self.__capacity}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')