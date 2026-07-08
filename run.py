from pathlib import Path
import sys

# Allow running this demo directly from a source checkout.
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from aevp import AEVPPipeline, EnergySavingScore, MovingAveragePredictor


def main() -> None:
    """Run a small AEVP demonstration."""
    history = [100.0, 98.0, 101.0, 99.0, 100.0]
    actual = 94.0

    pipeline = AEVPPipeline(
        predictor=MovingAveragePredictor(window=5),
        scorer=EnergySavingScore(point_rate=10.0),
    )

    result = pipeline.evaluate(history=history, actual=actual)

    print("AEVP demo")
    print("---------")
    print(f"Predicted energy use : {result.predicted:.2f}")
    print(f"Actual energy use    : {result.actual:.2f}")
    print(f"Energy saving        : {result.saving:.2f}")
    print(f"Points               : {result.points:.2f}")


if __name__ == "__main__":
    main()
