from pathlib import Path

from src.game_controller.controller import KakuroGameController
from src.ui.kakuro_game_ui import KakuroGameUI

map_path = "maps/9x9_easy.json"


def main():
    ui = KakuroGameUI()
    controller = KakuroGameController(ui, Path(map_path))
    controller.start()


if __name__ == "__main__":
    main()
