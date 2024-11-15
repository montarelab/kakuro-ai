from typing import Any, Callable

import pygame

from src.parsing_validation.entities import Map
from src.ui.button import Button
from src.ui.kakuro_game_field import KakuroGameField
from src.ui.position import Position


class KakuroGameUI:
    background_color = (229, 229, 229)
    _instance = None
    margin_horizontal = 50
    margin_vertical = 50

    def __new__(cls) -> "KakuroGameUI":
        if cls._instance is None:
            cls._instance = super(KakuroGameUI, cls).__new__(cls)
        return cls._instance

    def _init_ui_components(self) -> None:
        self._canvas = pygame.display.set_mode((650, 700))
        self._canvas.fill(self.background_color)

        pygame.display.set_caption("Kakuro")

        self._field = KakuroGameField(self._canvas, Position(self.margin_horizontal, self.margin_vertical))
        start_button_position_1 = self._calculate_start_button_position_1()
        start_button_position_2 = self._calculate_start_button_position_2()
        start_button_position_3 = self._calculate_start_button_position_3()

        self._start_button_1 = Button(self._canvas, "Start 1".upper(), start_button_position_1)
        self._start_button_2 = Button(self._canvas, "Start 2".upper(), start_button_position_2)
        self._start_button_3 = Button(self._canvas, "Start 3".upper(), start_button_position_3)

    def _calculate_start_button_position_1(self) -> Position:
        return Position(
            self._field.position.x,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_start_button_position_2(self) -> Position:
        return Position(
            self._field.position.x + 150,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_start_button_position_3(self) -> Position:
        return Position(
            self._field.position.x + 300,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_screen_size(self) -> None:
        self._screen_width = (
            self.margin_horizontal * 2 + self._field.width
        )
        self._screen_height = (
            self.margin_vertical * 2 + self._field.height + self._start_button_1.height + 20
        )
        self._screen_size = (self._screen_width, self._screen_height)

    def __init__(self) -> None:
        if hasattr(self, '_initialized'):
            return

        pygame.init()
        self._init_ui_components()
        self._initialized = True

    def set_map(self, game_map: Map) -> None:
        self._field.set_game_map(game_map)
        self._update_map_set_related_components()
        self.update()

    def _update_map_set_related_components(self):
        self._calculate_screen_size()
        self._canvas = pygame.display.set_mode(self._screen_size)
        self._canvas.fill(self.background_color)

        start_button_position_1 = self._calculate_start_button_position_1()
        start_button_position_2 = self._calculate_start_button_position_2()
        start_button_position_3 = self._calculate_start_button_position_3()

        self._start_button_1.set_position(start_button_position_1)
        self._start_button_2.set_position(start_button_position_2)
        self._start_button_3.set_position(start_button_position_3)

    def update(self) -> None:
        self._start_button_1.update()
        self._start_button_2.update()
        self._start_button_3.update()
        self._field.update()
        pygame.display.update()

    def bind_start_button_1(self, action: Callable[[], Any]) -> None:
        self._start_button_1.bind(action)

    def bind_start_button_2(self, action: Callable[[], Any]) -> None:
        self._start_button_2.bind(action)

    def bind_start_button_3(self, action: Callable[[], Any]) -> None:
        self.bind_start_button_3(action)
