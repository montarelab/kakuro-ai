from typing import Optional
from dataclasses import dataclass


# data structure for parsing
@dataclass
class Block:
    """
    Map class: Indicates a block on a map
    """
    pass


@dataclass
class Clue:
    """
    Map class: Indicates a clue on a map
    """
    sumRow: Optional[int] = None
    sumCol: Optional[int] = None


@dataclass
class Input:
    """
    Map class: Indicates an input on a map
    """
    pass


@dataclass
class Map:
    dimensions: dict
    cells: list[Block | Clue | Input]


# data structure for playing a game
@dataclass
class Node:
    """
    Node for graph traversal via DFS
    """

    def __init__(self, id: int, pos_x: int, pos_y: int):
        self.value = 0
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y

    id: int

    pos_x: int
    pos_y: int

    value: int = 0

    row: Optional[int] = None
    column: Optional[int] = None

    right_node: Optional[int] = None
    left_node: Optional[int] = None
    upper_node: Optional[int] = None
    bottom_node: Optional[int] = None

    def change_value(self, value, nodelist_arr) -> bool:
        """
        Tries to change value of a node
        returns: status as bool
        """

        if self.row is not None:
            row_available_values = nodelist_arr[self.row].get_available_values()
        else:
            row_available_values = set(range(1, 10))

        if self.column is not None:
            col_available_values = nodelist_arr[self.column].get_available_values()
        else:
            col_available_values = set(range(1, 10))

        available_values = row_available_values & col_available_values

        if value not in available_values:
            return False

        self.value = value

        if self.row is not None:
            nodelist_arr[self.row].update_sum()
        if self.column is not None:
            nodelist_arr[self.column].update_sum()

        return True


@dataclass
class NodeList:
    """
    Class for graph traversal
    """
    id: int
    list_of_nodes: list[Node]
    sum_value: int
    current_sum: int = 0

    def get_available_values(self) -> set[int]:
        """
        Returns a list of available to chose unique values
        """
        used_values = set([node.value for node in self.list_of_nodes])
        available_valuables = set(range(1, 10)) - used_values
        return available_valuables

    def update_sum(self):
        """
        Updates 'current_sum'
        """
        used_values = [node.value for node in self.list_of_nodes]
        self.current_sum = sum(used_values)

    def is_valid(self) -> bool:
        """
        returns: True if col | row is valid and its sum is completed. False otherwise
        """

        self.update_sum()
        return self.sum_value == self.current_sum


@dataclass
class RowList(NodeList):
    """
    Class for graph traversal . Represents row
    """
    pos_y: int = -1
    start_pos_x: int = -1
    length: int = -1


@dataclass
class ColList(NodeList):
    """
    Class for graph traversal. Represents Column
    """
    pos_x: int = -1
    start_pos_y: int = -1
    length: int = -1
