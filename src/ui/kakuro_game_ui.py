import pygame_gui
from pygame_gui.elements import UIButton

from src.parsing_validation.entities import Map
from src.ui.kakuro_game_field import KakuroGameField
from src.ui.position import Position

from typing import Callable
import pygame


def delta_time_decorator(clock: pygame.time.Clock) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            delta = clock.tick(60) / 1000.0
            return func(*args, delta_time=delta, **kwargs)
        return wrapper
    return decorator


class KakuroGameUI:
    background_color = (229, 229, 229)
    _instance = None
    margin_horizontal = 50
    margin_vertical = 50

    clock = pygame.time.Clock()

    def __new__(cls) -> "KakuroGameUI":
        if cls._instance is None:
            cls._instance = super(KakuroGameUI, cls).__new__(cls)
        return cls._instance

    def _init_ui_components(self) -> None:
        self._canvas = pygame.display.set_mode((650, 700))
        self._canvas.fill(self.background_color)
        pygame.display.set_caption("Kakuro")
        self._ui_manager = pygame_gui.UIManager((650, 700), "./src/themes/theme.json")

        self._field = KakuroGameField(self._canvas, Position(self.margin_horizontal, self.margin_vertical))
        start_button_position = self._calculate_start_button_position()

        self._start_button = UIButton(
            relative_rect=pygame.Rect(
                start_button_position.x,
                start_button_position.y,
                100, 50
            ),
            text="START",
            manager=self._ui_manager
        )
        self._start_button.bind(pygame_gui.UI_BUTTON_PRESSED, lambda _: print("Button clicked"))

    def _calculate_start_button_position(self) -> Position:
        return Position(
            self._field.position.x,
            self._field.height + self._field.position.y + 20
        )

    def _calculate_screen_size(self) -> None:
        self._screen_width = (
            self.margin_horizontal * 2 + self._field.width
        )
        self._screen_height = (
            self.margin_vertical * 2 + self._field.height + self._start_button.rect.height + 20
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
        start_button_position = self._calculate_start_button_position()
        self._start_button.set_relative_position(start_button_position)

    @delta_time_decorator(clock)
    def update(self, delta_time: float) -> None:
        for event in pygame.event.get():
            self._ui_manager.process_events(event)
        self._ui_manager.update(delta_time)
        self._ui_manager.draw_ui(self._canvas)
        self._field.update()
        pygame.display.update()
