# AEVP Roadmap

AEVP currently provides a minimal working prototype:

1. predict expected energy use,
2. compare predicted and actual energy use,
3. calculate energy-saving contribution,
4. convert the contribution into points.

## Phase 1: Minimal Prototype

- Moving average predictor
- Energy saving score
- AEVP pipeline
- Unit tests

This phase is complete.

## Phase 2: Better Baselines

Add alternative lightweight predictors suitable for small PCs or embedded computers.

Candidate predictors:

- moving average
- weighted moving average
- exponential smoothing
- day-of-week or time-of-day baseline
- state-dependent baseline

## Phase 3: Energy Value Scoring

Extend the scoring model so that points can reflect not only simple energy saving,
but also the value of the saving.

Candidate factors:

- amount of energy saved
- peak-time reduction
- stability of operation
- prediction confidence
- user or facility category
- fairness constraints
- upper and lower point limits

## Phase 4: Patent-Oriented Prototype

Map software components to patent-oriented functional blocks.

Candidate blocks:

- time-series acquisition unit
- prediction unit
- baseline generation unit
- energy-saving contribution calculation unit
- point conversion unit
- reward or settlement interface
- embedded execution unit

## Phase 5: Embedded Demonstration

Prepare a small-PC demonstration.

Candidate environments:

- Raspberry Pi class computer
- mini PC
- edge gateway
- offline local execution
- periodic batch execution
