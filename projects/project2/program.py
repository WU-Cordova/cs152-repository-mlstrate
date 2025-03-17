## IMPORTS
from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from projects.project2.grid import Grid
from projects.project2.gamecontroller import GameController


def main():

    game_controller = GameController()
    game_controller.run(10, 5, 5)




if __name__ == '__main__':
    main()
