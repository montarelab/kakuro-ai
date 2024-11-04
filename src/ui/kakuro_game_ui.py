import pygame

from src.ui.button import Button
from src.ui.position import Position


class KakuroGameUI:
    background_color = (247, 255, 246)
    _instance = None

    def __new__(cls) -> "KakuroGameUI":
        if cls._instance is None:
            cls._instance = super(KakuroGameUI, cls).__new__(cls)
        return cls._instance

    def _init_ui_components(self) -> None:
        self.canvas = pygame.display.set_mode((500, 500))
        self.canvas.fill(self.background_color)

        pygame.display.set_caption("Kakuro")

        self.start_button = Button(self.canvas, "Start".upper(), Position(100, 100))

    def __init__(self) -> None:
        if hasattr(self, '_initialized'):
            return

        pygame.init()
        self._init_ui_components()
        self._initialized = True

    def _update(self) -> None:
        self.start_button.update()
        pygame.display.update()

    def start(self) -> None:
        exit = False
        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
            self._update()
