from typing import Callable

import pygame
from pygame import Surface, mouse, freetype as py_freetype, draw
from src.ui.position import Position


class Button:
    background_color = (48, 125, 246)
    default_color = (255, 255, 255)
    hover_color = (100, 100, 100)
    paddings = (16, 32, 16, 32)
    font_size = 16
    font_family = 'Inter'
    border_radius = 24

    def __init__(self, screen: Surface, text: str, position: Position):
        self._screen = screen
        self._text = text
        self._font = py_freetype.Font(None, self.font_size)
        self._position = position
        self._action = lambda: None
        self._rectangle = None
        self._clicked = False

    def set_position(self, position: Position) -> None:
        self._position = position

    def update(self) -> None:
        self._update_background()
        self._update_text()
        self._handle_action()

    def _update_background(self) -> None:
        button_width, button_height = self._get_button_size()
        rectangle_properties = (self._position.x, self._position.y, button_width, button_height)

        if self._is_hovered():
            self._rectangle = draw.rect(self._screen, self.hover_color, rectangle_properties, border_radius=self.border_radius)
        else:
            self._rectangle = draw.rect(self._screen, self.background_color, rectangle_properties, border_radius=self.border_radius)

    def _update_text(self) -> None:
        padding_top, _, _, padding_left = self.paddings

        text_position = (
            self._position.x + padding_left,
            self._position.y + padding_top
        )

        self._font.render_to(self._screen, text_position, self._text, self.default_color)

    def _get_button_size(self):
        padding_top, padding_right, padding_bottom, padding_left = self.paddings
        text_width, text_height = self._font.get_rect(self._text).size

        button_width = text_width + padding_left + padding_right
        button_height = text_height + padding_top + padding_bottom

        return button_width, button_height

    @property
    def height(self) -> int:
        _, button_height = self._get_button_size()
        return button_height

    @property
    def width(self) -> int:
        button_width, _ = self._get_button_size()
        return button_width

    def _is_hovered(self):
        mouse_x, mouse_y = mouse.get_pos()
        button_width, button_height = self._get_button_size()

        x_hovered = self._position.x <= mouse_x <= self._position.x + button_width
        y_hovered = self._position.y <= mouse_y <= self._position.y + button_height

        return x_hovered and y_hovered

    def bind(self, action: Callable) -> None:
        self._action = action

    def _handle_action(self):
        if self._rectangle is None or self._action is None:
            return

        mouse_position = mouse.get_pos()

        if self._rectangle.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self._clicked is False:
                self._clicked = True
                self._action()

        if pygame.mouse.get_pressed()[0] == 0:
            self._clicked = False
