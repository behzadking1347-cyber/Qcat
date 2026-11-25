import numpy as np
import pandas as pd
import pytest

from qcat import clamp, distance, lerp, load_csv, moving_average, normalize, summarize


def test_math_helpers():
    assert clamp(12, 0, 10) == 10
    assert distance((0, 0), (3, 4)) == 5
    assert np.allclose(normalize((3, 4)), (0.6, 0.8))
    assert np.array_equal(normalize((0, 0)), (0, 0))
    assert lerp(10, 20, 0.25) == 12.5


def test_invalid_math_inputs():
    with pytest.raises(ValueError):
        clamp(1, 2, 0)
    with pytest.raises(ValueError):
        distance((0, 0), (1,))


def test_data_helpers(tmp_path):
    csv_path = tmp_path / "scores.csv"
    csv_path.write_text("score\n10\n20\n", encoding="utf-8")
    frame = load_csv(csv_path)
    assert frame["score"].tolist() == [10, 20]
    assert moving_average([1, 2, 3], 2).tolist() == [1.0, 1.5, 2.5]
    assert isinstance(summarize(frame), pd.DataFrame)


def test_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1, 2], 0)
