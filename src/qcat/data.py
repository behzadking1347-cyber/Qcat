"""ابزارهای سبک برای خواندن و تحلیل داده با Pandas."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def load_csv(path: str | Path, **kwargs: Any) -> pd.DataFrame:
    """فایل CSV را می‌خواند و یک DataFrame برمی‌گرداند.

    آرگومان‌های کلیدی اضافی مستقیماً به ``pandas.read_csv`` فرستاده می‌شوند.
    """
    return pd.read_csv(path, **kwargs)


def moving_average(values, window: int) -> pd.Series:
    """میانگین متحرک را به شکل Series محاسبه می‌کند."""
    if not isinstance(window, int) or isinstance(window, bool) or window < 1:
        raise ValueError("window باید عدد صحیحی بزرگ‌تر از صفر باشد.")
    return pd.Series(values, dtype="float64").rolling(window=window, min_periods=1).mean()


def summarize(data) -> pd.DataFrame:
    """خلاصهٔ آماری داده‌ها را با Pandas تولید می‌کند."""
    frame = data if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    return frame.describe(include="all")
