from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AEVPResult:
    """Result of one prediction-and-scoring evaluation."""

    predicted: float
    actual: float
    saving: float
    points: float

    def as_dict(self) -> dict[str, float]:
        """Return the result as a plain dictionary."""
        return {
            "predicted": self.predicted,
            "actual": self.actual,
            "saving": self.saving,
            "points": self.points,
        }
