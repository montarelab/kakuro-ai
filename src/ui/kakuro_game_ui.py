from typing import Any, Callable

import pygame
from pygame import RESIZABLE

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
        pygame.init()

        self._canvas = pygame.display.set_mode((650, 700), RESIZABLE)
        self._canvas.fill(self.background_color)

        pygame.display.set_caption("Kakuro")

        self._field = KakuroGameField(self._canvas, Position(self.margin_horizontal, self.margin_vertical))

        start_backtracking_button_position = self._calculate_start_backtracking_button_position()
        start_dfs_button_position = self._calculate_start_dfs_button_position()
        start_forward_button_position = self._calculate_start_forward_button_position()

        self._start_backtracking_button = Button(self._canvas, "backtracking".upper(), start_backtracking_button_position)
        self._start_dfs_button = Button(self._canvas, "dfs".upper(), start_dfs_button_position)
        self._start_forward_button = Button(self._canvas, "forward control".upper(), start_forward_button_position)

    def _calculate_start_backtracking_button_position(self) -> Position:
        return Position(
            self._field.position.x - 15,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_start_dfs_button_position(self) -> Position:
        return Position(
            self._field.position.x + 190,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_start_forward_button_position(self) -> Position:
        return Position(
            self._field.position.x + 295,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_window_size(self) -> tuple[int, int]:
        screen_width = int(max(
            self.margin_horizontal * 2 + self._field.width,
            self.margin_horizontal * 2 + self._calculate_start_forward_button_position().x + self._start_forward_button.width
        ))
        screen_height = int(
            self.margin_vertical * 2 + self._field.height + self._start_backtracking_button.height + 20
        )
        return screen_width, screen_height

    def __init__(self) -> None:
        if hasattr(self, '_initialized'):
            return

        self._init_ui_components()
        self._initialized = True

    def set_map(self, game_map: Map) -> None:
        self._field.set_game_map(game_map)
        self._update_buttons_positions()
        self.update()

    def _update_buttons_positions(self):
        start_backtracking_button_position = self._calculate_start_backtracking_button_position()
        start_dfs_button_position = self._calculate_start_dfs_button_position()
        start_forward_button_position = self._calculate_start_forward_button_position()

        self._start_backtracking_button.set_position(start_backtracking_button_position)
        self._start_dfs_button.set_position(start_dfs_button_position)
        self._start_forward_button.set_position(start_forward_button_position)

    def update(self) -> None:
        self._canvas.fill(self.background_color)
        self._start_backtracking_button.update()
        self._start_dfs_button.update()
        self._start_forward_button.update()
        self._field.update()
        pygame.display.update()

    def bind_start_backtracking(self, action: Callable[[], Any]) -> None:
        self._start_backtracking_button.bind(action)

    def bind_start_dfs(self, action: Callable[[], Any]) -> None:
        self._start_dfs_button.bind(action)

    def bind_start_forward_control(self, action: Callable[[], Any]) -> None:
        self._start_forward_button.bind(action)
