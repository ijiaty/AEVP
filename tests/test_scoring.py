import pytest

from aevp import CappedEnergySavingScore, EnergySavingScore


def test_score_positive_saving():
    scorer = EnergySavingScore(point_rate=10.0)
    assert scorer.score(predicted=100.0, actual=90.0) == pytest.approx(100.0)


def test_score_no_saving():
    scorer = EnergySavingScore(point_rate=10.0)
    assert scorer.score(predicted=100.0, actual=105.0) == pytest.approx(0.0)


def test_score_rejects_negative_point_rate():
    with pytest.raises(ValueError):
        EnergySavingScore(point_rate=-1.0)


def test_capped_score_limits_points():
    scorer = CappedEnergySavingScore(point_rate=10.0, max_points=50.0)
    assert scorer.score(predicted=100.0, actual=80.0) == pytest.approx(50.0)
