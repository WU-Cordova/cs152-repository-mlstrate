import pytest

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T
from datastructures.linkedlist import LinkedList

class TestLinkedList:

    @pytest.fixture
    def empty(self) -> ILinkedList[int]:
        return LinkedList[int](data_type=int)
    
    @pytest.fixture
    def linked_list(self) -> ILinkedList[int]:
        return LinkedList[int].from_sequence([0, 1, 2, 3, 4], data_type=int)

    @pytest.fixture
    def single_list(self) -> ILinkedList[int]:
        return LinkedList[int].from_sequence([0], data_type = int)

    def test_from_sequence_error(self) -> None:
        with pytest.raises(TypeError):
            test_list = LinkedList[int].from_sequence([0, 1, 2, "three", 4], data_type = int)

    def test_append(self, empty: ILinkedList[int], single_list: ILinkedList[int]) -> None:
        empty.append(1)
        assert len(empty) == 1
        assert empty.back == 1

        with pytest.raises(TypeError):
            empty.append("one")
        
        single_list.append(1)
        assert len(single_list) == 2
        assert single_list.back == 1

    def test_prepend(self, empty: ILinkedList[int], single_list) -> None:
        empty.prepend(1)
        assert len(empty) == 1
        assert empty.front == 1

        with pytest.raises(TypeError):
            empty.prepend("one")

        single_list.prepend(1)
        assert len(single_list) == 2
        assert single_list.front == 1

    def test_insert_before(self, linked_list: ILinkedList[int], single_list) -> None:
        linked_list.insert_before(2, 99)
        assert 99 in linked_list
        assert list(linked_list) == [0, 1, 99, 2, 3, 4]

        single_list.insert_before(0, 1)
        assert 1 in single_list
        assert list(single_list) == [1, 0]

    def test_insert_before_errors(self, linked_list: ILinkedList[int]) -> None:
        with pytest.raises(ValueError):
            linked_list.insert_before(10, 99)
        with pytest.raises(TypeError):
            linked_list.insert_before(2, "ninety-nine")
        with pytest.raises(TypeError):
            linked_list.insert_before("two", 99)

    def test_insert_after(self, linked_list: ILinkedList[int], single_list) -> None:
        linked_list.insert_after(2, 99)
        assert 99 in linked_list
        assert list(linked_list) == [0, 1, 2, 99, 3, 4]

        single_list.insert_after(0, 1)
        assert 1 in single_list
        assert list(single_list) == [0, 1]

    def test_insert_after_errors(self, linked_list: ILinkedList[int]) -> None:
        with pytest.raises(ValueError):
            linked_list.insert_after(10, 99)
        with pytest.raises(TypeError):
            linked_list.insert_after(2, "ninety-nine")
        with pytest.raises(TypeError):
            linked_list.insert_after("two", 99)
        

    def test_remove(self, linked_list: ILinkedList[int], single_list) -> None:
        linked_list.remove(2)
        assert 2 not in linked_list
        assert list(linked_list) == [0, 1, 3, 4]

        single_list.remove(0)
        assert 0 not in single_list
        assert list(single_list) == []

    def test_remove_not_found(self, linked_list: ILinkedList[int]) -> None:
        with pytest.raises(ValueError):
            linked_list.remove(10)

    def test_remove_all(self, linked_list: ILinkedList[int], single_list) -> None:
        linked_list.append(2)
        linked_list.remove_all(2)
        assert 2 not in linked_list
        assert list(linked_list) == [0, 1, 3, 4]

        single_list.remove_all(0)
        assert 0 not in single_list
        assert list(single_list) == []

    def test_pop(self, linked_list: ILinkedList[int], single_list) -> None:
        assert linked_list.pop() == 4
        assert len(linked_list) == 4

        assert single_list.pop() == 0
        assert len(single_list) == 0

    def test_pop_empty(self, empty: ILinkedList[int]) -> None:
        with pytest.raises(IndexError):
            empty.pop()

    def test_pop_front(self, linked_list: ILinkedList[int]) -> None:
        assert linked_list.pop_front() == 0
        assert len(linked_list) == 4
    
    def test_pop_front_len_1(self) -> None:
        test_list = LinkedList[int].from_sequence([0], data_type = int)
        assert test_list.pop_front() == 0
        assert len(test_list) == 0

    def test_pop_front_empty(self, empty: ILinkedList[int]) -> None:
        with pytest.raises(IndexError):
            empty.pop_front()

    def test_front(self, linked_list: ILinkedList[int]) -> None:
        assert linked_list.front == 0

    def test_front_empty(self, empty: ILinkedList[int]) -> None:
        with pytest.raises(IndexError):
            _ = empty.front

    def test_back(self, linked_list: ILinkedList[int]) -> None:
        assert linked_list.back == 4

    def test_back_empty(self, empty: ILinkedList[int]) -> None:
        with pytest.raises(IndexError):
            _ = empty.back

    def test_empty(self, empty: ILinkedList[int], linked_list: ILinkedList[int]) -> None:
        assert empty.empty is True
        assert linked_list.empty is False

    def test_len(self, empty: ILinkedList[int], linked_list: ILinkedList[int]) -> None:
        assert len(empty) == 0
        assert len(linked_list) == 5

    def test_clear(self, linked_list: ILinkedList[int], single_list) -> None:
        linked_list.clear()
        assert len(linked_list) == 0
        assert linked_list.empty is True

        single_list.clear()
        assert len(single_list) == 0
        assert single_list.empty is True

    def test_contains(self, linked_list: ILinkedList[int]) -> None:
        assert 2 in linked_list
        assert 10 not in linked_list

    def test_iter(self, linked_list: ILinkedList[int]) -> None:
        assert list(iter(linked_list)) == [0, 1, 2, 3, 4]

    def test_eq(self, linked_list: ILinkedList[int]) -> None:
        other = LinkedList[int].from_sequence([0, 1, 2, 3, 4], data_type=int)
        assert linked_list == other
        other.append(5)
        assert linked_list != other
        linked_list.append(6)
        assert linked_list != other

    def test_reversed(self, linked_list: ILinkedList[int]) -> None:
        reversed_list = list(reversed(linked_list))
        assert reversed_list == [4, 3, 2, 1, 0]

    def test_check_type_asserts(self, linked_list: ILinkedList[int]) -> None:
        with pytest.raises(TypeError):
            linked_list.append("string")
        with pytest.raises(TypeError):
            linked_list.prepend("string")
        with pytest.raises(TypeError):
            linked_list.insert_after(1, "string")
        with pytest.raises(TypeError):
            linked_list.insert_before(1, "string")
        with pytest.raises(TypeError):
            linked_list.insert_after("string", 2)
        with pytest.raises(TypeError):
            linked_list.insert_before("string", 2)
        with pytest.raises(TypeError):
            linked_list.remove("string")
        with pytest.raises(TypeError):
            linked_list.remove_all("string")
        with pytest.raises(TypeError):
            LinkedList.from_sequence([1, 2, 3], data_type=str)

    def test_value_error_raised(self, linked_list: ILinkedList[int]) -> None:
        with pytest.raises(ValueError):
            linked_list.insert_before(10, 99)  # Target not in list
        with pytest.raises(ValueError):
            linked_list.insert_after(10, 99)  # Target not in list
        with pytest.raises(ValueError):
            linked_list.remove(10)  # Item not in list