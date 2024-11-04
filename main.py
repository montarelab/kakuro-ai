from pathlib import Path
from typing import Any


def load_map(file_path: Path) -> Any:
    ...


def is_valid_map(game_map: Any) -> bool:
    ...


def main():
    game_map = load_map(Path("maps/map1.json"))
    if not is_valid_map(game_map):
        print("Invalid map!")
        return


if __name__ == "__main__":
    main()
