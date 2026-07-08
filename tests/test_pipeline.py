from aevp import AEVPPipeline, EnergySavingScore, MovingAveragePredictor


def test_pipeline_evaluate():
    pipeline = AEVPPipeline(
        predictor=MovingAveragePredictor(window=3),
        scorer=EnergySavingScore(point_rate=2.0),
    )

    result = pipeline.evaluate(
        history=[10.0, 20.0, 30.0],
        actual=15.0,
    )

    assert result.predicted == 20.0
    assert result.actual == 15.0
    assert result.saving == 5.0
    assert result.points == 10.0
    assert result.as_dict() == {
        "predicted": 20.0,
        "actual": 15.0,
        "saving": 5.0,
        "points": 10.0,
    }
