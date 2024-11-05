from typing import Optional
from dataclasses import dataclass

# data structure for parsing

@dataclass
class Block:
    pass

@dataclass
class Clue:
    sumRow: Optional[int] = None
    sumCol: Optional[int] = None

@dataclass
class Input:
    pass

@dataclass
class Map:
    dimensions: dict
    cells: list[Block | Clue | Input]

# data structure for playing a game
@dataclass
class Node:

    def __init__(self):
        self.value = 0
        row = None
        column = None
        right_node = None
        left_node = None
        upper_node = None
        bottom_node = None

    value: int = 0

    row: Optional['NodeList'] = None
    column: Optional['NodeList'] = None

    right_node: Optional['Node'] = None
    left_node: Optional['Node'] = None
    upper_node: Optional['Node'] = None
    bottom_node: Optional['Node'] = None

    def change_value(self, value):
        pass

@dataclass
class NodeList:
    sum_value: int
    
    list_od_nodes: list[Node]

    remained_value: int

    def get_available_values(self):
        pass

    def calculate_sum(self):
        pass

@dataclass
class RowList(NodeList):
    pos_y: int
    start_pos_x: int
    length: int

@dataclass
class ColList(NodeList):
    pos_x: int
    start_pos_y: int
    length: int
