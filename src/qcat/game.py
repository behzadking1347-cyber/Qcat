"""ابزارهای پایهٔ بازی دوبعدی بر اساس Pygame."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import pygame


@dataclass
class Entity:
    """موجودیت مستطیلی با موقعیت، اندازه، رنگ و سرعت بر حسب پیکسل/ثانیه."""

    x: float
    y: float
    width: int
    height: int
    color: tuple[int, int, int] = (240, 240, 240)
    vx: float = 0.0
    vy: float = 0.0
    speed: float = 0.0

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("عرض و ارتفاع Entity باید بزرگ‌تر از صفر باشند.")
        if len(self.color) != 3 or any(not 0 <= channel <= 255 for channel in self.color):
            raise ValueError("color باید یک RGB معتبر با کانال‌های ۰ تا ۲۵۵ باشد.")

    @property
    def rect(self) -> pygame.Rect:
        """مستطیل Pygame متناظر با موقعیت فعلی."""
        return pygame.Rect(round(self.x), round(self.y), self.width, self.height)

    def update(self, dt: float) -> None:
        """موقعیت را بر اساس سرعت و زمان سپری‌شده به‌روزرسانی می‌کند."""
        if dt < 0:
            raise ValueError("dt نمی‌تواند منفی باشد.")
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, surface: pygame.Surface) -> None:
        """موجودیت را روی سطح Pygame رسم می‌کند."""
        pygame.draw.rect(surface, self.color, self.rect)

    def collides_with(self, other: Entity) -> bool:
        """بررسی برخورد مستطیلی با یک موجودیت دیگر."""
        return self.rect.colliderect(other.rect)


class QcatGame:
    """حلقهٔ بازی ساده با callbackهای اختیاری برای به‌روزرسانی و رسم."""

    def __init__(
        self,
        title: str = "Qcat Game",
        size: tuple[int, int] = (800, 600),
        fps: int = 60,
        background: tuple[int, int, int] = (25, 25, 35),
    ) -> None:
        if len(size) != 2 or any(dimension <= 0 for dimension in size):
            raise ValueError("size باید شامل عرض و ارتفاع مثبت باشد.")
        if fps <= 0:
            raise ValueError("fps باید بزرگ‌تر از صفر باشد.")
        self.title = title
        self.size = size
        self.fps = fps
        self.background = background
        self.entities: list[Entity] = []
        self.running = False

    def add(self, entity: Entity) -> Entity:
        """موجودیت را به بازی اضافه کرده و همان را برمی‌گرداند."""
        self.entities.append(entity)
        return entity

    def remove(self, entity: Entity) -> None:
        """موجودیت را از بازی حذف می‌کند."""
        self.entities.remove(entity)

    def run(
        self,
        on_update: Callable[[QcatGame, float], None] | None = None,
        on_draw: Callable[[QcatGame, pygame.Surface], None] | None = None,
    ) -> None:
        """حلقه را تا خروج کاربر اجرا می‌کند. Escape پنجره را می‌بندد."""
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()
        self.running = True

        try:
            while self.running:
                dt = clock.tick(self.fps) / 1000.0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (
                        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                    ):
                        self.running = False

                if not self.running:
                    break

                for entity in tuple(self.entities):
                    entity.update(dt)
                if on_update is not None:
                    on_update(self, dt)

                screen.fill(self.background)
                for entity in tuple(self.entities):
                    entity.draw(screen)
                if on_draw is not None:
                    on_draw(self, screen)
                pygame.display.flip()
        finally:
            self.running = False
            pygame.quit()
