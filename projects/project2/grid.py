"""The grid data structure; a child structure of Array2D."""

## IMPORTS
from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from copy import deepcopy
import random
import time


class Grid(Array2D):

    def __init__(self, width: int, height: int) -> None:
        cells: List[List[Cell]] = []

        for row in range(height):
            cells.append([])
            for col in range(width):
                cells[row].append(Cell())
                cells[row][col].is_alive = random.choice([True, False])
                
                # Give the cell an idea of its position
                cells[row][col].row = row
                cells[row][col].col = col

                '''
                if row == 0:
                    cells[row][col].touching_top = True
                elif row == height - 1:
                    cells[row][col].touching_bottom = True
                if col == 0:
                    cells[row][col].touching_left = True
                elif col == width - 1:
                    cells[row][col].touching_right = True
                '''

        self.grid: Array2D = Array2D(starting_sequence = cells, data_type = Cell)
        self.rows = height
        self.cols = width


    def __str__(self) -> str:
        """ Creates a string representation of a grid that can be printed. """
        string = ""
        for row_idx in range(self.rows):
            for cell in self.grid[row_idx]:
                if cell.is_alive:
                    string += "X"
                else:
                    string += "-"
            string += "\n"
        return string


    def display(self) -> None:
        print(str(self))


    def __eq__(self, other: Grid) -> bool:
        return str(self) == str(other)


    def count_neighbors(self) -> None:
        '''
        Where ** is the cell, the neighbors orientation is: 

        UL | UC | UR
        ---+----+---
        L  | ** | R
        ---+----+---
        DL | DC | DR

        '''

        for row_idx in range(self.rows):        
            for cell in self.grid[row_idx]:     # for each cell:

                ## CHECK TOP NEIGHBORS
                if cell.row != 0:   # not touching top
                    if self.grid[cell.row - 1][cell.col].is_alive:    # UC
                        cell.neighbors += 1
                    if cell.col != 0:   # not touching L side
                        if self.grid[cell.row - 1][cell.col - 1].is_alive:  # UL
                            cell.neighbors += 1
                    if cell.col != self.cols - 1:   # not touching R side
                        if self.grid[cell.row - 1][cell.col + 1].is_alive:  # UR
                            cell.neighbors += 1
                
                ## CHECK SIDE NEIGHBORS
                if cell.col != 0:   # not touching L side
                    if self.grid[cell.row][cell.col - 1].is_alive:  # L
                        cell.neighbors += 1
                if cell.col != self.cols - 1:   # not touching R side
                    if self.grid[cell.row][cell.col + 1].is_alive:  # R
                        cell.neighbors += 1

                ## CHECK BOTTOM NEIGHBORS
                if cell.row != self.rows - 1:   # not touching bottom
                    if self.grid[cell.row + 1][cell.col].is_alive:    # DC
                        cell.neighbors += 1
                    if cell.col != 0:   # not touching L side
                        if self.grid[cell.row + 1][cell.col - 1].is_alive:  # DL
                            cell.neighbors += 1
                    if cell.col != self.cols - 1:   # not touching R side
                        if self.grid[cell.row + 1][cell.col + 1].is_alive:  # DR
                            cell.neighbors += 1


    def produce_next_gen(self) -> None:
        next_gen = Grid(self.cols, self.rows)
        for row_idx in range(self.rows):
                for col_idx in range(self.cols):     # for each cell:
                    if self.grid[row_idx][col_idx].alive_next_gen():
                        next_gen.grid[row_idx][col_idx].is_alive = True
                    else:
                        next_gen.grid[row_idx][col_idx].is_alive = False
        self.grid = deepcopy(next_gen.grid)
    



