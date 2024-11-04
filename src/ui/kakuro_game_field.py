from pygame import Surface

from src.ui.kakuro_field_block import KakuroFieldBlock
from src.ui.kakuro_field_input import KakuroFieldInput
from src.ui.position import Position


class KakuroGameField:
    def _row_column_to_position(self, row: int, column: int):
        x = self._position.x + column * KakuroFieldBlock.block_size
        y = self._position.y + row * KakuroFieldBlock.block_size
        return Position(x, y)

    def __init__(self, screen: Surface, position: Position):
        self._screen = screen
        self._position = position
        self.blocks = [
            KakuroFieldInput(self._screen, self._row_column_to_position(row, column), "test")
            for row in range(9)
            for column in range(9)
        ]

    @property
    def position(self) -> Position:
        return self._position

    @property
    def width(self) -> int:
        return KakuroFieldBlock.block_size * 9

    @property
    def height(self) -> int:
        return KakuroFieldBlock.block_size * 9

    def update(self):
        for block in self.blocks:
            block.update()
