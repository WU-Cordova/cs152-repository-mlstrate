"""The grid data structure; a child structure of Array2D."""

## IMPORTS
from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from datastructures.array2d import Array2D
from copy import deepcopy
import random
import time


class Grid(Array2D):

    def __init__(self, width: int, height: int) -> None:
        cells: List[List[Cell]] = []

        for row in range(height):
            cells.append([])
            for col in range(width):
                is_alive = random.choice([True, False])
                cells[row].append(Cell(is_alive = is_alive))

        self.grid: Array2D = Array2D(starting_sequence = cells, data_type = Cell)


    def display(self):
        print(self.grid) # I don't think this is going to work

    
    def count_neighbors(self, row: int, col: int) -> None:
        """
        1. iterate through each cell
        2. set each cell's num to grid.num_neighbors()
        3. populate new grid
        4. check for alternate or constant repeats
            - if grid == last_grid or grid == last_grid - 1, stop
        5. archive old grid in grid storage
        6. set grid = new_grid
        """


    def produce_next_gen():
        pass
        



    kb = KBHit()

    print('Hit any key, or ESC to exit.')

    iteration = 0

    while True:

        print(f"In loop: {iteration}")
        iteration += 1
        time.sleep(1)

        if kb.kbhit():
            c = kb.getch()
            c_ord = ord(c)
            print(c)
            print(c_ord)
            time.sleep(2)
            if c_ord == 27: # ESC
                break
            print(c)

    



