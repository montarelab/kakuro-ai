from pygame import Surface

from src.parsing_validation.entities import Map, Block, Clue, Input
from src.ui.kakuro_field_block import KakuroFieldBlock
from src.ui.kakuro_field_cell import KakuroFieldCell
from src.ui.kakuro_field_clue import KakuroFieldClue
from src.ui.kakuro_field_input import KakuroFieldInput
from src.ui.position import Position


class KakuroGameField:
    def _row_column_to_position(self, row: int, column: int):
        x = self._position.x + column * (KakuroFieldBlock.block_size - KakuroFieldBlock.border_thickness)
        y = self._position.y + row * (KakuroFieldBlock.block_size - KakuroFieldBlock.border_thickness)
        return Position(x, y)

    def __init__(self, screen: Surface, position: Position):
        self._screen = screen
        self._position = position
        self._map = None
        self._ui_cells: list[KakuroFieldCell] = []

    def set_game_map(self, game_map: Map) -> None:
        self._map = game_map
        self._ui_cells = []

        current_row = 0
        current_column = 0
        for map_cell in self._map.cells:
            position = self._row_column_to_position(current_row, current_column)
            match map_cell:
                case Block():
                    self._ui_cells.append(KakuroFieldBlock(self._screen, position))
                case Clue(sumRow=sum_row, sumCol=sum_col):
                    self._ui_cells.append(KakuroFieldClue(self._screen, position, sum_row, sum_col))
                case Input():
                    self._ui_cells.append(KakuroFieldInput(self._screen, position, ""))
            current_column += 1
            if current_column == self._map.dimensions['columns']:
                current_column = 0
                current_row += 1

    @property
    def position(self) -> Position:
        return self._position

    @property
    def width(self) -> int:
        if self._map is None:
            return 0
        return (
            KakuroFieldBlock.block_size * self._map.dimensions['columns'] -
            KakuroFieldBlock.border_thickness * (self._map.dimensions['columns'] - 1)
        )

    @property
    def height(self) -> int:
        if self._map is None:
            return 0
        return (
            KakuroFieldBlock.block_size * self._map.dimensions['rows'] -
            KakuroFieldBlock.border_thickness * (self._map.dimensions['rows'] - 1)
        )

    def update(self):
        for block in self._ui_cells:
            block.update()
