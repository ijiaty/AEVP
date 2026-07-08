# Patent-Oriented Mapping Note

This note maps the prototype implementation to patent-style terminology.
It is not a legal opinion and not a patent filing document.

## Functional blocks

| Function | Current implementation |
| --- | --- |
| Time-series data acquisition | Input list passed to `predict_next()` |
| Prediction unit | `MovingAveragePredictor`, `ExponentialSmoothingPredictor` |
| Baseline generation | Predicted expected energy use |
| Actual-result acquisition | `actual` argument of `AEVPPipeline.evaluate()` |
| Energy-saving contribution calculation | `predicted - actual`, clipped at zero |
| Point conversion | `EnergySavingScore.score()` |
| Abnormal award limitation | `CappedEnergySavingScore` |
| Integrated control / processing unit | `AEVPPipeline` |

## Claim-oriented seed expression

A computer-implemented energy-saving evaluation method comprising:

1. receiving historical time-series data relating to energy use;
2. predicting an expected energy-use value from the historical time-series data;
3. receiving an actual energy-use value;
4. calculating an energy-saving contribution based on a difference between the
   predicted expected energy-use value and the actual energy-use value; and
5. assigning a point value corresponding to the energy-saving contribution.

## Notes for future expansion

The present code intentionally uses simple predictors.  Future versions may
replace the prediction unit with:

- state-dependent weighted prediction,
- reservoir computing,
- radial basis function reconstruction,
- compact edge-device forecasting,
- sensor fusion across building or facility sensors.
