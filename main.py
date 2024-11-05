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
    print('Nodes were received:')

    for node in nodes:
        print(node, '\n\n')


    print('-------------------------------\n')
    
    print('Clues were received:\n')



    # [print(clue) for clue in clues ]



if __name__ == "__main__":
    main()
