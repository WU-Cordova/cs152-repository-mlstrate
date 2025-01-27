from typing import Iterable, Optional
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        ''' Creates the bag and adds any initial items. '''
        self.contents = {}
        for item in items:
            if item == None:
                raise TypeError("Cannot add NoneType item")
            elif item not in self.contents:
                self.contents[item] = 1   # start item count at 1
            else:
                self.contents[item] += 1  # add 1 to item count for duplicates

    def add(self, item: T) -> None:
        ''' Adds an item to the bag. '''
        if item == None:
            raise TypeError("Cannot add NoneType item")
        elif item not in self.contents:
            self.contents[item] = 1   # start item count at 1
        else:
            self.contents[item] += 1  # add 1 to item count for duplicates

    def remove(self, item: T) -> None:
        ''' Removes an item from the bag. '''
        if item == None:
            raise TypeError("Cannot remove NoneType item")
        elif item not in self.contents:
            raise ValueError("Item not in bag")
        else:
            self.contents[item] -= 1

    def count(self, item: T) -> int:
        ''' Returns the count of a given item. '''
        ## THIS NEEDS TO BE IMPLEMENTED BEFORE ADD AND IT SHOULD NOT
        try: self.contents[item]
        except: 
            if item == None:
                raise TypeError("Cannot count NoneType item")
            return 0    # if the item doesn't exist in the bag
        return self.contents[item]

    def __len__(self) -> int:
        ''' Returns the total number of items in the bag. '''
        length = 0
        for item in self.contents:
            length += self.contents[item]
        return length

    def distinct_items(self) -> Iterable[T]:
        ''' Returns a list of the unique items in the bag. '''
        return list(self.contents.keys())

    def __contains__(self, item) -> bool:
        ''' Checks whether or not a given item is in the bag. '''
        if item == None:
            raise TypeError("Cannot check if bag contains a NoneType item")
        else:
            if item in self.contents and self.contents[item] != 0:
                return True
            else:
                return False

    def clear(self) -> None:
        ''' Removes all items from the bag. '''
        ## Shouldn't there be a test for an item count of more than 1?
        for item in self.contents:
            while self.contents[item] > 0:
                self.remove(item)