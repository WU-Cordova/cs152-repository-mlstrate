"""The cell data structure."""

class Cell:

    def __init__(self) -> None:
        
        self.row: int = 0   # cell's row and column position (all start at 0, will be set in grid)
        self.col: int = 0

        self.is_alive: bool = False    # whether cell is alive or not (all start as false, will be set in grid)
        self.neighbors = 0


    def alive_next_gen(self) -> bool:
        """Decides whether the spot in the grid will contain a live cell in the next generation."""

        if self.neighbors <= 1: 
            return False
        if self.neighbors == 2:
            return self.is_alive
        if self.neighbors == 3:
            return True
        if self.neighbors >= 4:
            return False