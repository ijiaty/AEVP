from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EnergySavingScore:
    """
    Convert predicted-vs-actual energy savings into points.

    If actual consumption is lower than predicted consumption, the difference
    is treated as an energy-saving contribution. If actual consumption is not
    lower, the score is zero.
    """

    point_rate: float = 1.0

    def __post_init__(self) -> None:
        if self.point_rate < 0.0:
            raise ValueError("point_rate must not be negative")

    def score(self, predicted: float, actual: float) -> float:
        saving = predicted - actual
        if saving <= 0.0:
            return 0.0
        return saving * self.point_rate


@dataclass(frozen=True)
class CappedEnergySavingScore:
    """
    Energy-saving scorer with an upper point limit.

    This is useful when a system should prevent extremely large or abnormal
    point awards from a single evaluation.
    """

    point_rate: float = 1.0
    max_points: float = 1000.0

    def __post_init__(self) -> None:
        if self.point_rate < 0.0:
            raise ValueError("point_rate must not be negative")
        if self.max_points < 0.0:
            raise ValueError("max_points must not be negative")

    def score(self, predicted: float, actual: float) -> float:
        raw = EnergySavingScore(point_rate=self.point_rate).score(predicted, actual)
        return min(raw, self.max_points)
