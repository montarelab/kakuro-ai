from typing import Callable

from src.parsing_validation.data_structure import get_data_structure
from src.parsing_validation.entities import Map


class Algorithm:
    def __init__(self, game_map: Map) -> None:
        self._map = game_map
        self._lambda = None
        self._blank_nodes, self._clues = get_data_structure(game_map)

    def is_succeed(self):
        for node in self._blank_nodes:
            if node.value != 0 or len(node.get_possible_values(self._clues)) > 0:
                return True
        return False

    def solve(self) -> bool:
        print('Solving algorithm...')
        return False

    def bind(self, lambda_function: Callable[[Map], None]) -> None:
        self._lambda = lambda_function
