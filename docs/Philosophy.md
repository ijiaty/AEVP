# AEVP Philosophy

AEVP is based on a simple idea:

> A predicted baseline can become a reference for measuring energy-saving value.

Energy-saving actions are often difficult to evaluate because the counterfactual
baseline is not directly observed.  AEVP therefore estimates an expected value
from historical time-series data, compares the estimate with the actual value,
and converts the difference into a point-like value.

This repository starts from very small predictors so that the full flow can be
understood easily:

1. predict,
2. compare,
3. score,
4. test.

The first implementation is not intended to be the final research model.  It is
a clean skeleton into which more advanced prediction methods can be inserted.
