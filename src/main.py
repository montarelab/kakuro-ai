from pathlib import Path
from typing import Any
from src.ui.kakuro_game_ui import KakuroGameUI


def load_map(file_path: Path) -> Any:
    ...


def is_valid_map(game_map: Any) -> bool:
    ...


def main():
    ui = KakuroGameUI()
    ui.start()


if __name__ == "__main__":
    main()
