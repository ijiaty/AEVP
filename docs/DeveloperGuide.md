# Developer Guide

## Local execution

```bash
python3 run.py
```

## Running tests

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest
```

## Adding a new predictor

A predictor only needs to provide this method:

```python
def predict_next(self, values: list[float]) -> float:
    ...
```

It can then be passed to `AEVPPipeline`.

## Adding a new scorer

A scorer only needs to provide this method:

```python
def score(self, predicted: float, actual: float) -> float:
    ...
```

It can then be passed to `AEVPPipeline`.

## Design policy

- Keep the core package small.
- Keep the pipeline testable.
- Prefer clear interfaces over clever code.
- Treat the current predictors as placeholders for future research models.
