#from bag.py import Bag
import random

suits = [
    ['spades', '\u2660'],
    ['hearts', '\u2661'],
    ['diamonds', '\u2662'],
    ['clubs', '\u2663']
]

values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

poss_deck_num = [2, 4, 6, 8]    # the possible numbers of decks

class Card:

    def __init__(self, lbl, val, suit):
        self.label = lbl
        self.value = val
        self.suit = suit


class Deck:    # need to make this a child of Bag eventually
    
    def __init__(self) -> None:
        num_decks = random.choice(poss_deck_num)
        self.cards = {}
        for i in range(num_decks):
            for suit in suits:
                for value in values:
                    next_card = Card(f"{value}{suit[1]}", value, suit)
                    if next_card not in self.cards:
                        self.cards[item] = 1   # start item count at 1
                    else:
                        self.contents[item] += 1  # add 1 to item count for duplicates



print(str(suits[1]))