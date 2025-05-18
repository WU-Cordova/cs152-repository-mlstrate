from __future__ import annotations

from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
from copy import deepcopy

from datastructures.iarray import IArray, T
from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 1, data_type=object) -> None:
        ''' Constructor to initialize the stack 

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.empty
                True
                >>> s.full
                False
                >>> s.maxsize
                5
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.array = Array.empty(elements = max_size, data_type = data_type)
        self.max_size = max_size
        self.data_type = data_type
        self.top_item_index = -1    # starting at -1 so when you add the first item its index is 0
        self.array.set_element_count(0)     # because otherwise Array thinks the length is max_size

    def push(self, item: T) -> None:
        ''' Pushes an item onto the stack.
        
            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> s.push(4)
                >>> s.push(5)
                >>> s.full
                True
                >>> print(repr(s))
                ArrayStack(5): items: [1, 2, 3, 4, 5]
                >>> s.push(6)
                IndexError('Stack is full')

            Arguments:
                item: T -- The item to push onto the stack.
        '''
        if not isinstance(item, self.data_type):
            raise TypeError('Item is not an instance of the specified data type')
        if self.top_item_index >= self.max_size - 1:
            raise IndexError('Stack is full')
        else:
            self.array.append(item)
            self.top_item_index += 1

    def pop(self) -> T:
        ''' Pops an item from the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> s.pop()
                3
                >>> s.pop()
                2
                >>> s.pop()
                1
                >>> s.empty
                True
                >>> print(repr(s))
                ArrayStack(5): items: []
                >>> s.pop()
                IndexError('Stack is empty')
        
            Returns:
                T -- The item popped from the stack.
        '''
        if self.top_item_index == -1:
            raise IndexError('Stack is empty')
        else: 
            popped = self.array.pop()
            self.top_item_index -= 1
            return popped

    def clear(self) -> None:
       ''' Clears the stack. 
       
           Examples:
               >>> s = ArrayStack(max_size=5, data_type=int)
               >>> s.push(1)
               >>> s.push(2)
               >>> s.push(3)
               >>> s.clear()
               >>> s.empty
               True
               >>> print(repr(s))
               ArrayStack(5): items: []
        '''
       self.array.clear()
       self.top_item_index = -1
    
    @property
    def peek(self) -> T:
        ''' Returns the top item on the stack without removing it.
        
            Returns:
                T -- The top item on the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> s.peek
                3
                >>> s.pop()
                3
                >>> s.peek
                2
                >>> s.pop()
                2
                >>> s.peek
                1
                >>> s.pop()
                1
                >>> s.empty
                True
                >>> s.peek
                IndexError('Stack is empty')
        '''
        if self.top_item_index == -1:
            raise IndexError('Stack is empty')
        else:
            return self.array[self.top_item_index]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.maxsize
                5
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.max_size
      
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 

            Examples:

        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self.top_item_index == self.max_size - 1

    @property
    def empty(self) -> bool:
        ''' Returns True if the stack is empty, False otherwise. 

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.empty
                True
                >>> s.push(1)
                >>> s.empty
                False
                >>> s.pop()
                1
                >>> s.empty
                True
        
            Returns:
                bool: True if the stack is empty, False otherwise.
        '''
        return self.top_item_index == -1
    
    def __eq__(self, other: object) -> bool:
        ''' Compares two stacks for equality.

            Examples:
                >>> s1 = ArrayStack(max_size=5, data_type=int)
                >>> s2 = ArrayStack(max_size=5, data_type=int)
                >>> s1 == s2
                True
                >>> s1.push(1)
                >>> s1 == s2
                False
                >>> s2.push(1)
                >>> s1 == s2
                True
                >>> s1.push(2)
                >>> s2.push(3)
                >>> s1 == s2
                False
        
            Arguments:
                other: object -- The other stack to compare.
                
            Returns:
                bool -- True if the stacks are equal, False otherwise.
        '''
        if not isinstance(other, ArrayStack):
            raise TypeError('Cannot compare ArrayStack to another data type')
        else:
            return self.array == other.array

    def __len__(self) -> int:
        ''' Returns the number of items in the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> len(s)
                0
                >>> s.push(1)
                >>> len(s)
                1
                >>> s.push(2)
                >>> len(s)
                2
                >>> s.pop()
                2
                >>> len(s)
                1
                >>> s.pop()
                1
                >>> len(s)
                0
        
            Returns:
                int -- The number of items in the stack.
        '''
        return self.top_item_index + 1
    
    def __contains__(self, item: T) -> bool:
        ''' Returns True if the item is in the stack, False otherwise.
        
            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> 1 in s
                True
                >>> 2 in s
                True
                >>> 3 in s
                True
                >>> 4 in s
                False
                >>> 5 in s
                False
            
            Arguments:
                item: T -- The item to search for.
                
            Returns:
                bool -- True if the item is in the stack, False otherwise.
        '''
        for i in range(self.top_item_index + 1):
            if self.array[i] == item:
                return True
        return False

    def __str__(self) -> str:
        ''' Returns a string representation of the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> print(s)
                [1, 2, 3]
        
            Returns:
                str -- A string representation of the stack.
        '''
        return str([self.array[i] for i in range(self.top_item_index + 1)])
    
    def __repr__(self) -> str:
        ''' Returns a string representation of the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> repr(s)
                'ArrayStack(5): items: [1, 2, 3]'
        
            Returns:
                str -- A string representation of the stack.
        '''
        return f"ArrayStack({self.max_size}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

