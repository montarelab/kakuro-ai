from typing import Optional
from dataclasses import dataclass


# data structure for parsing

@dataclass
class Cell:
    type: str
    sumRow: Optional[int] = None
    sumCol: Optional[int] = None


@dataclass
class Map:
    dimensions: dict
    cells: list[Cell]


# data structure for playing a game

class Node:
    value: int
    row: 'NodeList'
    column: 'NodeList'
    right_node: 'Node'
    left_node: 'Node'
    upper_node: 'Node'
    bottom_node: 'Node'

    def change_value(self, value):
        pass


class NodeList:
    sum_value: int
    list_od_nodes: list[Node]
    remained_value: int

    def get_available_values(self):
        pass

    def calculate_sum(self):
        pass
