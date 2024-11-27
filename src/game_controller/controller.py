from pathlib import Path
from typing import NoReturn

import pygame

from src.game_controller.backtracking import Backtracking
from src.game_controller.dfs import Dfs
from src.game_controller.forward_checking import ForwardChecking
from src.game_controller.unknownAlgorithmError import UnknownAlgorithmError
from src.parsing_validation.entities import Map
from src.parsing_validation.parse import parse_map
from src.parsing_validation.validation import validate_map
from src.ui.kakuro_game_ui import KakuroGameUI


def load_map(path: Path) -> Map:
    game_map = parse_map(path.absolute())
    validate_map(game_map)
    return game_map


class KakuroGameController:
    def __init__(self, ui: KakuroGameUI, map_path: Path) -> None:
        self._ui = ui
        self._algorithm = None
        self._map_path = map_path
        self._map = load_map(map_path)
        self._ui.set_map(self._map)
        self.set_buttons_bindings()

    def start(self) -> NoReturn:
        exit_ui = False

        while not exit_ui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_ui = True
            self._ui.update()

    def reload_map(self) -> None:
        self._map = load_map(self._map_path)
        self._ui.set_map(self._map)

    def set_map(self, map_path: str) -> None:
        self._map_path = map_path
        self.reload_map()

    def update_ui(self, game_map: Map) -> None:
        self._ui.set_map(game_map)
        self._ui.update()
        time.sleep(0.1)

    def start_algorithm(self, algorithm_name: str) -> None:
        self.reload_map()
        match algorithm_name:
            case 'backtracking':
                self._algorithm = Backtracking(self._map)
            case 'dfs':
                self._algorithm = Dfs(self._map)
            case 'forward_control':
                self._algorithm = ForwardChecking(self._map)
            case _:
                raise UnknownAlgorithmError(f'Algorithm {algorithm_name} is not supported')

        self._algorithm.bind(self.update_ui)
        self._algorithm.solve()

    def set_buttons_bindings(self) -> None:
        self._ui.bind_start_dfs(lambda: self.start_algorithm('dfs'))
        self._ui.bind_start_backtracking(lambda: self.start_algorithm('backtracking'))
        self._ui.bind_start_forward_control(lambda: self.start_algorithm('forward_control'))