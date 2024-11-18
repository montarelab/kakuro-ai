from typing import Callable

from src.parsing_validation.data_structure import get_data_structure
from src.parsing_validation.entities import Map


class Algorithm:
    def __init__(self, game_map: Map) -> None:
        self._map = game_map
        self._lambda = None
        self._blank_nodes, self._clues = get_data_structure(game_map)

    def solve(self) -> bool:
        print('Solving algorithm...')
        return False

    def bind(self, lambda_function: Callable[[Map], None]) -> None:
        self._lambda = lambda_function
