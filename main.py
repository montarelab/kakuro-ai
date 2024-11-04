from pathlib import Path
from typing import Any
from parse import parse_map
from validation import validate_map

map_path = "maps/map1.json"

def main():
    game_map = parse_map(map_path)
    validate_map(game_map)
    




if __name__ == "__main__":
    main()
