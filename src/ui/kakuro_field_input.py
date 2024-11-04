from pygame import Surface, draw, freetype as py_freetype

from src.ui.position import Position


class KakuroFieldInput:
    background_color = (0, 0, 0)
    default_color = (255, 255, 255)
    border_color = (215, 225, 244)
    block_size = 50
    border_thickness = 2
    font_size = 16
    font_family = 'Inter'

    def __init__(self, screen: Surface, position: Position, text: str):
        self._screen = screen
        self._position = position
        self._text = text
        self._font = py_freetype.Font(None, self.font_size)

    def update(self):
        self._update_background()
        self._update_text()

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

    def _update_text(self) -> None:
        text_rect = self._font.get_rect(self._text)
        text_width, text_height = text_rect.size

        text_position = (
            self._position.x + (self.block_size - text_width) / 2,
            self._position.y + (self.block_size - text_height) / 2
        )

        self._font.render_to(self._screen, text_position, self._text, self.default_color)