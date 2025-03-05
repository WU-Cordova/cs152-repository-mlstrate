"""The cell data structure."""

class Cell:

    def __init__(row, col) -> None:
        self.__row = row
        self.__col = col
        
        '''
        self.__touching_top: bool
            tell from row and col whether cell is touching top or not
            do same for left, right, bottom
        '''

        self.is_alive: bool = False    # whether cell is alive or not (all start as false)
        self.neighbors = 0


    def alive_next_gen(neighbors) -> bool:
        """Decides whether the spot in the grid will contain a live cell in the next generation."""