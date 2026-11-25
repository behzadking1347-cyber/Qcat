"""Qcat: ابزارهای بازی‌سازی، محاسبات و داده برای پایتون."""

from .data import load_csv, moving_average, summarize
from .game import Entity, QcatGame
from .mathx import clamp, distance, lerp, normalize

__version__ = "0.1.0"

__all__ = [
    "Entity",
    "QcatGame",
    "clamp",
    "distance",
    "lerp",
    "load_csv",
    "moving_average",
    "normalize",
    "summarize",
    "__version__",
]
