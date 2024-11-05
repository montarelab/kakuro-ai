from typing import Optional
from dataclasses import dataclass

# data structure for parsing

@dataclass
class Block:
    '''
    Map class: Indicates a block on a map
    '''
    pass

@dataclass
class Clue:
    '''
    Map class: Indicates a clue on a map
    '''
    sumRow: Optional[int] = None
    sumCol: Optional[int] = None

@dataclass
class Input:
    '''
    Map class: Indicates an input on a map
    '''
    pass

@dataclass
class Map:
    dimensions: dict
    cells: list[Block | Clue | Input]

# data structure for playing a game
@dataclass
class Node:
    '''
    Node for graph traversal via DFS 
    '''
    def __init__(self, id: int, pos_x: int, pos_y: int):
        self.value = 0
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y

    id: int = -1

    pos_x: int = 0
    pos_y: int = 0

    value: int = 0

    row: int = -1
    column: int = -1

    right_node: Optional[int] = None
    left_node: Optional[int] = None
    upper_node: Optional[int] = None
    bottom_node: Optional[int] = None

    def change_value(self, value, nodelist_arr) -> bool:
        '''
        Tries to change value of a node
        returns: status as bool
        '''
        
        row_available_values = []
        col_available_values = []

        if self.row != -1:
            row_available_values = nodelist_arr[self.row].get_available_values()
        else:
            row_available_values = set(range(1, 10))
            
        if self.column != -1:
            col_available_values = nodelist_arr[self.column].get_available_values()
        else:
            col_available_values = set(range(1, 10))

        available_values = row_available_values & col_available_values

        if value in available_values:
            self.value = value
            return True
        
        return False
        

@dataclass
class NodeList:
    '''
    Class for graph traversal 
    '''
    id: int

    sum_value: int
    
    list_of_nodes: list[Node]

    remained_value: int

    def get_available_values(self) -> set[int]:
        '''
        Returns a list of available to chose unique values 
        '''
        used_values = set([ node.value for node in self.list_of_nodes ])
        available_valuables = set(range(1, 10)) - used_values
        return available_valuables

    def calculate_sum(self):        
        '''
        1. Calculates a sum of row | column

        2. Update 'remained_value'
        '''
        used_values = [ node.value for node in self.list_of_nodes]
        received_sum = used_values.sum()
        
        self.remained_value = self.sum_value - received_sum
        
        return received_sum

@dataclass
class RowList(NodeList):
    '''
    Class for graph traversal . Represents row
    '''
    pos_y: int
    start_pos_x: int
    length: int

@dataclass
class ColList(NodeList):
    '''
    Class for graph traversal. Represents Column 
    '''
    pos_x: int
    start_pos_y: int
    length: int
