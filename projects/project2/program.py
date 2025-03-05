
from projects.project2.grid import Grid
from projects.project2.gamecontroller import GameController


def main():
    
    """
    1. initialize first grid
    2. set speed
    3. initialize next generations at that speed
    4. store 5 past grids in grid storage list
    5. check for repeats
    6. stop if there are repeats
    """

    grid = Grid(10, 10)
    game_controller = GameController(grid)
    game_controller.run(100)




if __name__ == '__main__':
    main()
