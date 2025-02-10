from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from datastructures.bag import Bag
from projects.project1.cards import Card, MultiDeck
from projects.project1.game_logic import Game
from copy import deepcopy
import random

def main():
    blackjack = Game()
    blackjack.play()


if __name__ == '__main__':
    main()
