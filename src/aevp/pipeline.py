from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .predictor import Predictor
from .scoring import EnergySavingScore
from .types import AEVPResult


class Scorer(Protocol):
    """Protocol for scoring components used by the AEVP pipeline."""

    def score(self, predicted: float, actual: float) -> float:
        """Return points from predicted and actual energy values."""
        ...


@dataclass(frozen=True)
class AEVPPipeline:
    """
    Minimal pipeline for Adaptive Energy Value Prediction.

    Steps:
      1. Predict expected energy use from historical values.
      2. Compare the prediction with the actual value.
      3. Convert the saving into points.
    """

    predictor: Predictor
    scorer: Scorer = EnergySavingScore()

    def evaluate(self, history: list[float], actual: float) -> AEVPResult:
        predicted = self.predictor.predict_next(history)
        saving = max(predicted - actual, 0.0)
        points = self.scorer.score(predicted=predicted, actual=actual)

        return AEVPResult(
            predicted=predicted,
            actual=actual,
            saving=saving,
            points=points,
        )
