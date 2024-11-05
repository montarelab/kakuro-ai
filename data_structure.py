from entities import Map, Node, NodeList, Clue, Input, Block, RowList, ColList
from itertools import takewhile
from dataclasses import dataclass
import copy


def display_matrix(matrix, width=30):
    '''
    Represents the matrix in console
    '''
    for row in matrix:
        # Use list comprehension to format each element
        formatted_row = ''.join([f"{str(element):>{width}}" for element in row])
        print(formatted_row)



@dataclass
class Empty:
    '''
    The class is needed for building a linkage matrix to link all of the nodes
    '''
    pass


def link_nodes(matrix, cols, rows) -> list[list[Node | Empty]] :
    '''
    1. Converts the matrix of elements (Block | Clue | Input) in the matrix of (Node | Empty)
    2. Creates links between neighbor Nodes
    returns: the the matrix of (Node | Empty)
    '''

    # get 2d arrray of nodes without links
    node_matrix = copy.deepcopy(matrix)
    for (row_index, row) in enumerate(matrix):
        for (col_index, cell) in enumerate(row):
            if isinstance(cell, Input):
               node_matrix[row_index][col_index] = Node()
            else:
                node_matrix[row_index][col_index] = Empty()

    # add links to nodes
    for (row_index, row) in enumerate(node_matrix):
        for (col_index, node) in enumerate(row):
            
            # add upper neighbour
            if row_index != 0:
                selected_node = node_matrix[row_index - 1][col_index]
                if isinstance(selected_node, Input):
                    node.upper_node = selected_node
            
            # add bottom neighbour
            if row_index != rows - 1:    
                selected_node = node_matrix[row_index + 1][col_index]
                if isinstance(selected_node, Input):
                    node.bottom_node = selected_node

            # add left neighbour
            if col_index != 0:
                selected_node = node_matrix[row_index][col_index -1]
                if isinstance(selected_node, Input):
                    node.left_node = selected_node

            # add right neighbour
            if col_index != cols - 1:
                selected_node = node_matrix[row_index][col_index + 1]
                if isinstance(selected_node, Input):
                    node.right_node = selected_node

    # return 2D array of linked Nodes and Empties
    return node_matrix




def get_data_structure(map: Map) -> tuple [list[Node], list[NodeList]]:
    '''
    Converts the map of (Block | Clue | Input) parsef from JSON into ready sets of data structures ready for DFS algorithms
    returns: 
        a) List of all the nodes of type Node
        b) List of all Rows in Columns represented by type NodeList
    '''

    cols = map.dimensions['columns']
    rows = map.dimensions['rows']
    cells_matrix = list()

    # Convert 1D array of cells in 2D array to simplify further processing 
    for i in range(rows):
        row = map.cells[i * cols : (i + 1) * cols]
        cells_matrix.append(row)


    # display_matrix(cells_matrix)

    # Get the matrix of linked Nodes
    node_matrix = link_nodes(cells_matrix, cols, rows)

    # Get array of clues: rows and columns
    all_clues = list()
    for (row_index, row) in enumerate(cells_matrix): # traverse the cell_matrix
        for (col_index, cell) in enumerate(row):

            if not isinstance(cell, Clue): 
                continue
            
            # create a coll
            if cell.sumCol != None:
                col_list = ColList(
                    sum_value = cell.sumCol, 
                    remained_value=cell.sumCol,
                    pos_x=row_index,
                    start_pos_y=col_index,
                    length=0,
                    list_od_nodes=[])
                
                # define the length, and get nodes for it
                array = [row[col_index] for row in node_matrix[row_index + 1:]]
                nodes = list(takewhile(lambda x: isinstance(x, Node), array))
                [setattr(node, 'column', col_list) for node in nodes]
                col_list.length = len(nodes)
                col_list.list_od_nodes = nodes
                all_clues.append(col_list)

            # create a row
            if cell.sumRow != None:
                row_list = RowList(
                    sum_value = cell.sumRow,
                    remained_value=cell.sumCol,
                    pos_y=col_index,
                    start_pos_x=row_index,
                    length=0,
                    list_od_nodes=[])
                
                # define the length, and get nodes for it
                array = node_matrix[row_index][col_index + 1:]
                nodes = list(takewhile(lambda x: isinstance(x, Node), array))
                [setattr(node, 'row', row_list) for node in nodes]
                row_list.length = len(nodes)
                row_list.list_od_nodes = nodes
                all_clues.append(row_list)    

    return [node for row in node_matrix for node in row if isinstance(node, Node) ], all_clues

