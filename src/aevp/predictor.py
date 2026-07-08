from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Protocol


class Predictor(Protocol):
    """Protocol for predictors used by the AEVP pipeline."""

    def predict_next(self, values: list[float]) -> float:
        """Predict the next value from the given history."""
        ...


@dataclass(frozen=True)
class MovingAveragePredictor:
    """
    A compact baseline predictor using the recent moving average.

    This is intentionally simple so that the package first demonstrates
    the AEVP concept: prediction, comparison, and energy-saving scoring.
    More advanced predictors can be added later while keeping the same
    pipeline interface.
    """

    window: int = 5

    def __post_init__(self) -> None:
        if self.window <= 0:
            raise ValueError("window must be a positive integer")

    def predict_next(self, values: list[float]) -> float:
        if not values:
            raise ValueError("values must not be empty")

        recent = values[-self.window :]
        return float(mean(recent))


@dataclass(frozen=True)
class ExponentialSmoothingPredictor:
    """
    Lightweight exponential smoothing predictor.

    alpha controls how strongly the latest observation affects the result.
    This predictor is still small enough for embedded or edge-computing
    demonstrations.
    """

    alpha: float = 0.3

    def __post_init__(self) -> None:
        if not 0.0 < self.alpha <= 1.0:
            raise ValueError("alpha must satisfy 0 < alpha <= 1")

    def predict_next(self, values: list[float]) -> float:
        if not values:
            raise ValueError("values must not be empty")

        estimate = float(values[0])
        for value in values[1:]:
            estimate = self.alpha * float(value) + (1.0 - self.alpha) * estimate
        return estimate
