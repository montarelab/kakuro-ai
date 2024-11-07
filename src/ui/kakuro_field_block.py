from pygame import Surface, draw

from src.ui.kakuro_field_cell import KakuroFieldCell
from src.ui.position import Position


class KakuroFieldBlock(KakuroFieldCell):
    background_color = (0, 0, 0)
    border_color = (215, 225, 244)
    block_size = 50
    border_thickness = 2

    def __init__(self, screen: Surface, position: Position):
        self._screen = screen
        self._position = position

    def update(self):
        self._update_background()

    def _update_background(self):
        border_properties = (self._position.x, self._position.y, self.block_size, self.block_size)
        draw.rect(self._screen, self.border_color, border_properties)

        inner_properties = (
            self._position.x + self.border_thickness,
            self._position.y + self.border_thickness,
            self.block_size - 2 * self.border_thickness,
            self.block_size - 2 * self.border_thickness
        )
        draw.rect(self._screen, self.background_color, inner_properties)
