import pygame

from src.parsing_validation.entities import Map
from src.ui.button import Button
from src.ui.kakuro_game_field import KakuroGameField
from src.ui.position import Position


class KakuroGameUI:
    background_color = (229, 229, 229)
    _instance = None

    def __new__(cls) -> "KakuroGameUI":
        if cls._instance is None:
            cls._instance = super(KakuroGameUI, cls).__new__(cls)
        return cls._instance

    def _init_ui_components(self) -> None:
        self._canvas = pygame.display.set_mode((650, 700))
        self._canvas.fill(self.background_color)

        pygame.display.set_caption("Kakuro")

        self._field = KakuroGameField(self._canvas, Position(100, 100))
        start_button_position = self._calculate_start_button_position()
        self._start_button = Button(self._canvas, "Start".upper(), start_button_position)

    def _calculate_start_button_position(self):
        return Position(
            self._field.position.x,
            self._field.height + self._field.position.y + 20
        )

    def __init__(self) -> None:
        if hasattr(self, '_initialized'):
            return

        pygame.init()
        self._init_ui_components()
        self._initialized = True

    def set_map(self, game_map: Map) -> None:
        self._field.set_game_map(game_map)

    def update(self) -> None:
        start_button_position = self._calculate_start_button_position()
        self._start_button.set_position(start_button_position)
        self._start_button.update()
        self._field.update()
        pygame.display.update()
