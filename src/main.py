from pathlib import Path

from src.game_controller.controller import KakuroGameController
from src.ui.kakuro_game_ui import KakuroGameUI

initial_map = "maps/9x9_easy.json"

def main():
    ui = KakuroGameUI()
    controller = KakuroGameController(ui, initial_map)
    controller.start()


if __name__ == "__main__":
    main()
