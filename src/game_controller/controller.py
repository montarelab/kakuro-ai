from pathlib import Path

import pygame

from src.parsing_validation.data_structure import get_data_structure
from src.parsing_validation.parse import parse_map
from src.parsing_validation.validation import validate_map
from src.ui.kakuro_game_ui import KakuroGameUI


class KakuroGameController:
    def __init__(self, ui: KakuroGameUI, game_map_path: Path):
        self._ui = ui
        self._game_map_path = game_map_path

    def start(self) -> None:
        game_map = parse_map(str(self._game_map_path))
        validate_map(game_map)
        self._ui.set_map(game_map)

        exit_ui = False
        while not exit_ui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_ui = True
            self._ui.update()
