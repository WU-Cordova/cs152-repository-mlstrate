from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence, Iterator
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.data_type = data_type
        self.head = None
        self.tail = None
        self.count = 0

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        for data in sequence:
            if not isinstance(data, data_type):
                raise TypeError(f"Element '{data}' in sequence is not an instance of data type '{data_type}.")
        
        LList = LinkedList(data_type = data_type)
        for data in sequence:
            LList.append(data)
        return LList


    def append(self, item: T) -> None:
        
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item '{item}' is not an instance of data type '{self.data_type}'.")

        new_node = self.Node(data = item, next = None, previous = self.tail)
        if self.count == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1


    def prepend(self, item: T) -> None:

        if not isinstance(item, self.data_type):
            raise TypeError(f"Item '{item}' is not an instance of data type '{self.data_type}'.") 

        new_node = self.Node(item, next = self.head, previous = None)
        if self.count == 0:
            self.tail = new_node
        else:
            self.head.previous = new_node
        self.head = new_node
        self.count += 1
        

    ####### MIGHT WANT TO CHANGE THIS FOR NONE CASE     
    def insert_before(self, target: T, item: T) -> None:
        ## ERRORS
        if not isinstance(target, self.data_type):
            raise TypeError(f"Target node '{target}' is not an instance of data type '{self.data_type}'.")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item '{item}' is not an instance of data type '{self.data_type}'.") 

        current = self.head

        while current:   # while current is not None
            if current.data == target:   # break once we've found target node
                break
            current = current.next
        
        if current is None:
            raise ValueError(f"The target value '{target}' was not found in the linked list.")

        if current is self.head:     # use "is" instead of "==" because we're talking about the object, not its value
            self.prepend(item)
            return

        ## Not the head
        new_node = self.Node(item, next = current, previous = current.previous)
        current.previous.next = new_node
        current.previous = new_node
        self.count += 1

    
    ####### MIGHT WANT TO CHANGE THIS FOR NONE CASE
    def insert_after(self, target: T, item: T) -> None: 
        ## ERRORS
        if not isinstance(target, self.data_type):
            raise TypeError(f"Target node '{target}' is not an instance of data type {self.data_type}.")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item '{item}' is not an instance of data type {self.data_type}.") 

        current = self.head

        while current:   # while current is not None
            if current.data == target:   # break once we've found target node
                break
            current = current.next
        
        if current is None:
            raise ValueError(f"The target value '{target}' was not found in the linked list.")

        if current is self.tail:     # use "is" instead of "==" because we're talking about the object, not its value
            self.append(item)
            return

        ## Not the tail
        new_node = self.Node(item, next = current.next, previous = current)
        current.next.previous = new_node
        current.next = new_node
        self.count += 1


    def remove(self, item: T) -> None:
        ## ERRORS
        if self.count == 0:
            raise IndexError("Linked list is empty.")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item '{item}' is not an instance of data type {self.data_type}.")

        current = self.head

        while current:
            if current.data == item:    # if you've found the node
                if current != self.head:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current != self.tail:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.count -= 1
                break
            elif current == self.tail: # if you've reached the end of the list and haven't found the node
                raise ValueError(f"Item '{item}' was not found in the linked list.")
            else:   # if you're not at the end of the list and haven't found the node
                current = current.next


    def remove_all(self, item: T) -> None:
        ## ERRORS
        if self.count == 0:
            raise IndexError("Linked list is empty.")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item '{item}' is not an instance of data type {self.data_type}.")
        
        starting_count = self.count
        current = self.head

        while current:
            if current.data == item:    # if you've found an instance of the item
                if current != self.head:    # to avoid NoneType error
                    current.previous.next = current.next
                else:   # if current is self.head
                    self.head = current.next
                if current != self.tail:    # to avoid NoneType error
                    current.next.previous = current.previous
                else:   # if current is self.tail
                    self.tail = current.previous
                self.count -= 1
            elif current == self.tail and self.count == starting_count: # if you've reached the end of the list and haven't found an instance of the item yet
                raise ValueError(f"Item '{item}' was not found in the linked list.")
            elif current == self.tail:  # if you've reached the end of the list but HAVE found an instance of the item in the past
                break
            current = current.next


    def pop(self) -> T:
        if self.count == 0:
            raise IndexError("Linked list is empty.")

        popped = self.tail.data

        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail.previous.next = None
            self.tail.previous = self.tail
        
        self.count -= 1
        return popped
        

    def pop_front(self) -> T:
        if self.count == 0:
            raise IndexError("Linked list is empty.")
        
        popped = self.head.data

        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            self.head.next.previous = None
            self.head.next = self.head

        self.count -= 1
        return popped


    @property
    def front(self) -> T:
        if self.count == 0:
            raise IndexError("Linked list is empty.")
        else:
            return self.head.data

    @property
    def back(self) -> T:
        if self.count == 0:
            raise IndexError("Linked list is empty.")
        else:
            return self.tail.data

    @property
    def empty(self) -> bool:
        if self.count == 0 and self.head is None and self.tail is None:
            return True
        else:
            return False

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0


    def __contains__(self, item: T) -> bool:
        current = self.head

        while current:   # while current is not None
            if current.data == item:   # found target node
                return True
            elif current == self.tail:  # reached end of linked list
                return False
            else:
                current = current.next


    def __iter__(self) -> Iterator[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        
        if self.travel_node is None:
            raise StopIteration

        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    

    def __reversed__(self) -> ILinkedList[T]:
        rev_items = []
        current = self.tail
        while current:
            rev_items.append(current.data)
            current = current.previous
        return rev_items


    def __eq__(self, other: object) -> bool:
        current_other = other.head

        if self.count != other.count:
            return False

        for data in self:
            if data == current_other.data:
                current_other = current_other.next
                # at the end, should both be None, so don't need an ending case
            else:
                return False
        return True


    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
