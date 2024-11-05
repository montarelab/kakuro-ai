from pathlib import Path
from typing import Any
from parse import parse_map
from validation import validate_map
from data_structure import get_data_structure

map_path = "maps/map1.json"

def main():
    game_map = parse_map(map_path)
    validate_map(game_map)
    nodes, clues = get_data_structure(game_map)
    print('\nNodes were received:')

    for node in nodes:
        print(node, '\n')


    print('-------------------------------\n')
    
    print('Clues were received:\n')

    node = nodes[0]

    print(node.change_value(9, clues))
    clue = clues[node.column]
    print('Current sum is', clue.current_sum)
    print('Is valid:', clue.is_valid())


if __name__ == "__main__":
    main()
