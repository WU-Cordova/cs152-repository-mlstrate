## IMPORTS
from __future__ import annotations
import os
from typing import Iterator, Sequence
from copy import deepcopy
import random
import time

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from datastructures.array2d import Array2D
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit


class GameController:

    def __init__(self):
        pass

    
    def run(self, gens: int, grid_w, grid_h) -> None:
        self.done = False

        '''
        kb = KBHit()
        print("Press M for Manual mode. Default mode is Automatic.")
        print("")
        '''

        self.gen_storage = []
        self.curr_gen = Grid(grid_w, grid_h)
        self.gen_count = 1

        print(f"Generation {self.gen_count}:")
        self.curr_gen.display()
        print("")


        def advance_gens():
            ## STORE CURRENT GEN
            self.gen_storage.append(deepcopy(self.curr_gen))
            if len(self.gen_storage) > 3:
                self.gen_storage = self.gen_storage[1:]   # will overwrite the list and remove the first (oldest) element
            
            ## MAKE NEXT GEN
            self.curr_gen.count_neighbors()
            self.curr_gen.produce_next_gen()
            self.gen_count += 1

            print(f"Generation {self.gen_count}:")
            self.curr_gen.display()
            print("")
            
            ## CHECK FOR AN EMPTY COLONY
            num_alive = 0
            for row_idx in range(self.curr_gen.rows):
                for cell in self.curr_gen.grid[row_idx]:
                    if cell.is_alive:
                        num_alive += 1
            if num_alive == 0:
                self.done = True
                print(f"No cells left alive in the colony. Program terminated at generation {self.gen_count}.")


            ## CHECK FOR REPEATS
            for stored_gen in self.gen_storage:
                if self.curr_gen == stored_gen:
                    self.done = True
                    print(f"Colony has reached a stable orientation or repeating pattern of orientations. Program terminated at generation {self.gen_count}.")
            
            
            ## END AT SPECIFIED NUMBER OF GENERATIONS
            if self.gen_count >= gens:
                self.done = True
                print(f"Program terminated at generation {self.gen_count}.")


        ## ATTEMPTED KBHIT
        '''
        while True:
            if kb.kbhit():
                c = kb.getch()
                c_ord = ord(c)
                if c_ord == 27: # ESC
                    break
                if self.done:
                    break
                elif c_ord == 101: # A
                    while not self.done:
                        advance_gens()
                        print("Generation advanced. Sleeping now.")
                        time.sleep(1.0)
                        print("Awoken.")
                        if kb.kbhit():
                            c = kb.getch()
                            c_ord = ord(c)
                            if c_ord == 101: # M
                                break
                elif c_ord == 115: # M
                    while not self.done:
                        if kb.kbhit():
                            c = kb.getch()
                            c_ord = ord(c)
                            if c_ord == 123: # S
                                advance_gens()
                            if c_ord == 101: # A
                                break
        '''


        while not self.done:
                advance_gens()