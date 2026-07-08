# AEVP

AEVP stands for **Adaptive Energy Value Prediction**.

This repository is a small Python prototype for connecting:

1. time-series prediction,
2. energy-saving evaluation, and
3. point / value scoring.

The first version intentionally uses lightweight baseline predictors.  The aim
is to keep the structure simple and testable, while leaving room for more
advanced forecasting methods later.

## Concept

AEVP evaluates energy-saving contribution as follows:

```text
historical energy data
        ↓
forecast expected energy use
        ↓
compare with actual energy use
        ↓
calculate energy saving
        ↓
convert saving into points
```

For example, if a system predicts that energy use should be `99.6`, but the
actual value is `94.0`, the difference `5.6` can be regarded as an
energy-saving contribution.  A point rate can then convert the saving into
points.

## Quick start

```bash
python3 run.py
```

Expected output:

```text
AEVP demo
---------
Predicted energy use : 99.60
Actual energy use    : 94.00
Energy saving        : 5.60
Points               : 56.00
```

## Tests

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest
```

## Repository layout

```text
src/aevp/
  predictor.py   # lightweight time-series predictors
  scoring.py     # energy-saving-to-points conversion
  pipeline.py    # prediction + scoring pipeline
  types.py       # result data structure

tests/           # pytest tests
docs/            # design notes and patent-oriented mapping
run.py           # small demonstration script
```

## Patent-oriented mapping

This repository is not a patent document.  However, the software components can
be mapped to patent-style functional blocks:

| Patent-style function | Software component |
| --- | --- |
| Time-series prediction unit | `MovingAveragePredictor`, `ExponentialSmoothingPredictor` |
| Energy-saving contribution calculation unit | `EnergySavingScore` |
| Point / value assignment unit | `EnergySavingScore`, `CappedEnergySavingScore` |
| Integrated processing unit | `AEVPPipeline` |

## Future directions

Possible future extensions include:

- state-dependent weighted forecasting,
- reservoir computing,
- RBF-based reconstruction,
- edge-device deployment,
- sensor fusion,
- anomaly-aware scoring,
- user / building / facility level point aggregation.

## Documents

- [Philosophy](docs/Philosophy.md)
- [Developer Guide](docs/DeveloperGuide.md)
- [Patent Mapping](docs/PatentMapping.md)
- [Patent Memo Japanese](docs/PatentMemo-ja.md)
- [Claim Draft Japanese](docs/ClaimDraft-ja.md)
- [Roadmap](docs/Roadmap.md)

- [Use Cases Japanese](docs/UseCases-ja.md)
- [Architecture Japanese](docs/Architecture-ja.md)
