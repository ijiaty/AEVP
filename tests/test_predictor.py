import pytest

from aevp import ExponentialSmoothingPredictor, MovingAveragePredictor


def test_moving_average_predicts_recent_mean():
    predictor = MovingAveragePredictor(window=3)
    assert predictor.predict_next([10.0, 20.0, 30.0, 40.0]) == pytest.approx(30.0)


def test_moving_average_rejects_empty_values():
    predictor = MovingAveragePredictor(window=3)
    with pytest.raises(ValueError):
        predictor.predict_next([])


def test_moving_average_rejects_invalid_window():
    with pytest.raises(ValueError):
        MovingAveragePredictor(window=0)


def test_exponential_smoothing_predicts_value():
    predictor = ExponentialSmoothingPredictor(alpha=0.5)
    assert predictor.predict_next([10.0, 20.0, 30.0]) == pytest.approx(22.5)


def test_exponential_smoothing_rejects_invalid_alpha():
    with pytest.raises(ValueError):
        ExponentialSmoothingPredictor(alpha=0.0)
