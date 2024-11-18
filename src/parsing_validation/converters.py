from copy import deepcopy
from src.parsing_validation.entities import Map, Node, Input


def graph_to_map(game_map: Map, node_list: list[Node]) -> Map:
    node_index = 0
    new_map = deepcopy(game_map)
    for (cell_index, cell) in enumerate(game_map.cells):
        if isinstance(cell, Input):
            # print('Cell index is', cell_index, 'len is',len(new_map.cells), 'node index is', node_index, 'len is', len(node_list))
            new_map.cells[cell_index] = Input(value = node_list[node_index].value)
            node_index += 1

    return new_map