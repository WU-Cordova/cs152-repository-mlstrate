from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from datastructures.bag import Bag
import random
from copy import deepcopy

suits = [
    '\u2660',    # spades
    '\u2661',    # hearts
    '\u2662',    # diamonds
    '\u2663'     # clubs
]

values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

poss_deck_num = [2, 4, 6, 8]    # the possible numbers of decks


class Card:

    def __init__(self, suit: str, value: str) -> None:
        ''' 
        Creates a card.
        
        Arguments:
            suit: one of the elements in <suits>
            value: one of the elements in <values>
        '''
        self.suit = suit        
        self.value = value
        self.symbol = f"{value}{suit}"    
            # the symbol players will see (e.g. "J\u2660")

    def __hash__(self):
        return hash((self.symbol, self.suit, self.value))

    def __eq__(self, other_card) -> bool:
        # other card is Card type
        if other_card is None:
            return False
        return self.symbol == other_card.symbol


class MultiDeck(Bag):    # need to make this a child of Bag eventually
    
    def __init__(self) -> None:
        num_decks = random.choice(poss_deck_num)    
            # choose number of decks to play with
        self.contents = {}     # initialize bag of cards

        # create each possible card in the deck once for every deck being played with
        for i in range(num_decks):
            for s in suits:
                for v in values:    
                    card = Card(s, v)
                    if card not in self.contents:
                        self.contents[card] = 1   # start card count at 1
                    else:
                        self.contents[card] += 1  # add 1 to card count for duplicates

    def distinct_items(self) -> Iterable[T]:
        ''' Returns a list of the unique items in the bag. '''
        items = []
        for key in self.contents.keys():
            items.append(key.symbol)
        return items

    def draw_random_card(self) -> Card:
        drawn_card = random.choice(list(self.contents.keys()))
        card_copy = deepcopy(drawn_card)
        self.remove(drawn_card)
        return card_copy
