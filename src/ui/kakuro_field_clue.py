from pygame import Surface, freetype as py_freetype, draw
from src.ui.kakuro_field_cell import KakuroFieldCell
from src.ui.position import Position


class KakuroFieldClue(KakuroFieldCell):
    background_color = (255, 255, 255)
    default_color = (48, 125, 246)
    border_color = (215, 225, 244)
    block_size = 60
    border_thickness = 4
    font_size = 16
    font_family = 'Inter'
    text_offset = 3

    def __init__(self, screen: Surface, position: Position, sum_row: int | None, sum_column: int | None):
        self._screen = screen
        self._position = position
        self._top_right_text = str(sum_row) if sum_row is not None else None
        self._bottom_left_text = str(sum_column) if sum_column is not None else None
        self._font = py_freetype.Font(None, self.font_size)

    def update(self) -> None:
        self._update_background()
        self._update_triangles()
        self._update_top_right_text()
        self._update_bottom_left_text()
        self._update_border()

    def _update_background(self):
        inner_properties = (
            self._position.x + self.border_thickness,
            self._position.y + self.border_thickness,
            self.block_size - 2 * self.border_thickness,
            self.block_size - 2 * self.border_thickness
        )
        draw.rect(self._screen, self.background_color, inner_properties)

    def _update_triangles(self) -> None:
        if self._top_right_text is None:
            top_right_triangle = [
                (self._position.x + self.border_thickness, self._position.y + self.border_thickness),
                (self._position.x + self.block_size - self.border_thickness, self._position.y + self.border_thickness),
                (self._position.x + self.block_size - self.border_thickness,
                 self._position.y + self.block_size - self.border_thickness)
            ]
            draw.polygon(self._screen, self.default_color, top_right_triangle)

        if self._bottom_left_text is None:
            bottom_left_triangle = [
                (self._position.x + self.border_thickness, self._position.y + self.border_thickness),
                (self._position.x + self.border_thickness, self._position.y + self.block_size - self.border_thickness),
                (self._position.x + self.block_size - self.border_thickness,
                 self._position.y + self.block_size - self.border_thickness)
            ]
            draw.polygon(self._screen, self.default_color, bottom_left_triangle)

    def _update_top_right_text(self) -> None:
        if self._top_right_text is None:
            return

        text_height, text_width = self._get_text_size(self._top_right_text)
        top_right_text_position = (
            self._position.x + self.block_size - text_width - self.text_offset - self.border_thickness,
            self._position.y + self.text_offset + self.border_thickness
        )

        self._font.render_to(self._screen, top_right_text_position, self._top_right_text, self.default_color)

    def _update_bottom_left_text(self) -> None:
        if self._bottom_left_text is None:
            return

        text_height, text_width = self._get_text_size(self._bottom_left_text)
        bottom_left_text_position = (
            self._position.x + self.text_offset + self.border_thickness,
            self._position.y + self.block_size - text_height - self.text_offset - self.border_thickness
        )

        self._font.render_to(self._screen, bottom_left_text_position, self._bottom_left_text, self.default_color)

    def _update_border(self) -> None:
        outer_border_rect = (self._position.x, self._position.y, self.block_size, self.block_size)
        draw.rect(self._screen, self.border_color, outer_border_rect, width=self.border_thickness)

        start_point = (self._position.x, self._position.y)
        end_point = (
            self._position.x + self.block_size - self.border_thickness,
            self._position.y + self.block_size - self.border_thickness
        )
        draw.line(self._screen, self.border_color, start_point, end_point, width=self.border_thickness)

    def _get_text_size(self, text: str) -> tuple[int, int]:
        text_rect = self._font.get_rect(text)
        text_width, text_height = text_rect.size
        return text_height, text_width
