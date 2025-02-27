from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from copy import deepcopy


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type=object) -> None:
            self.__index = row_index
            self.__array = array
            self.__num_columns = num_columns
            self.__data_type = data_type

        def __getitem__(self, column_index: int) -> T:
            if column_index >= len(self) or column_index < -len(self):
                raise IndexError("Column index out of range.")

            index = self.map_index(column_index)
            return self.__array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(column_index)
            self.__array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.__num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(-1, (-self.__num_columns) - 1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.__num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.__num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__index}: [{", ".join([str(self[column_index]) for column_index in range(self.__num_columns - 1)])}, {str(self[self.__num_columns - 1])}]'

        def map_index(self, column_index: int) -> int:
            """Takes the index of an item within the row and returns the index of that item in the overarching 1D array."""
            index1d = self.__index * self.__num_columns + column_index
            return index1d

    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        ## CHECK FOR ERRORS
        if not isinstance(starting_sequence, Sequence) or isinstance(starting_sequence, str):
            raise ValueError("Starting sequence is not a valid sequence.")

        for i in range(len(starting_sequence)):
            if not isinstance(starting_sequence[i], Sequence):
                raise ValueError("Starting sequence must be a sequence of sequences.")

        for i in range(1, len(starting_sequence)):
            if len(starting_sequence[i]) != len(starting_sequence[0]):
                raise ValueError("All inner sequences must be the same size.")

        for i in range(len(starting_sequence)):
            for j in range(len(starting_sequence[0])):
                if not isinstance(starting_sequence[i][j], data_type):
                    raise TypeError("All items must be instances of the specified data type.")

        ## INITIALIZE ATTRIBUTES
        self.__data_type = data_type
        self.__row_len = len(starting_sequence[0])
        self.__col_len = len(starting_sequence)

        ## INITIALIZE EMPTY ARRAY2D
        self.__array1d = Array([data_type() for i in range(self.__row_len * self.__col_len)], data_type = data_type)

        ## ADD ITEMS TO ARRAY2D
        index = 0                   # initialize 1d index
        for row_index in range(self.__row_len):
            for col_index in range(self.__col_len):
                self.__array1d[index] = starting_sequence[row_index][col_index]
                index += 1          # count up 1d index


    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence: List[List[T]] = []
        for row in range(rows):
            starting_sequence.append([])
            for col in range(cols):
                starting_sequence[row].append(data_type()) 
        return Array2D(starting_sequence, data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index >= len(self) or row_index < -len(self):
            raise IndexError("Row index out of range.")
        return Array2D.Row(row_index, self.__array1d, self.__col_len, self.__data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(len(self)):
            yield self[row_index]
    
    def __reversed__(self):
        for row_index in range(len(self) - 1, -1, -1):
            yield self[row_index]
    
    def __len__(self): 
        return len(self.__array1d) // self.__row_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {len(self)} Rows x {self.__row_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')