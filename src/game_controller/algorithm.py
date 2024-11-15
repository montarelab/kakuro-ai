from typing import Callable

from src.parsing_validation.data_structure import get_data_structure
from src.parsing_validation.entities import Map


class Algorithm:
    def __init__(self, game_map: Map) -> None:
        self._map = game_map
        self._lambda = None

    def solve(self) -> None:
        print('Solving algorithm...')
        pass

    def bind(self, lambda_function: Callable[[Map], None]) -> None:
        self._lambda = lambda_function
