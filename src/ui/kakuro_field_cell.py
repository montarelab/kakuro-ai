from typing import Protocol


class KakuroFieldCell(Protocol):
    def update(self) -> None:
        pass
