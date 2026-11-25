"""محاسبات کاربردی و عملیات برداری مبتنی بر NumPy."""

from __future__ import annotations

import numpy as np


def clamp(value: float, minimum: float, maximum: float) -> float:
    """مقدار را در بازهٔ بستهٔ minimum تا maximum محدود می‌کند."""
    if minimum > maximum:
        raise ValueError("minimum نباید از maximum بزرگ‌تر باشد.")
    return max(minimum, min(value, maximum))


def distance(a, b) -> float:
    """فاصلهٔ اقلیدسی دو نقطه یا بردار هم‌اندازه را برمی‌گرداند."""
    first = np.asarray(a, dtype=float)
    second = np.asarray(b, dtype=float)
    if first.shape != second.shape:
        raise ValueError("دو ورودی باید شکل یکسانی داشته باشند.")
    return float(np.linalg.norm(first - second))


def normalize(vector) -> np.ndarray:
    """بردار را واحد می‌کند؛ برای بردار صفر، آرایهٔ صفر برمی‌گرداند."""
    values = np.asarray(vector, dtype=float)
    magnitude = np.linalg.norm(values)
    if magnitude == 0:
        return np.zeros_like(values, dtype=float)
    return values / magnitude


def lerp(start: float, end: float, amount: float) -> float:
    """درون‌یابی خطی؛ amount خارج از بازهٔ صفر تا یک نیز مجاز است."""
    return start + (end - start) * amount
