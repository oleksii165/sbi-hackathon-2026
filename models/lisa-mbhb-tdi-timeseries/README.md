# Louis — LISA Massive Black Hole Binaries inference (TDI time series simulator)

## Short description
Simulator for estimating parameters of Massive Black Hole Binaries (MBHB) using LISA data.
LISA is a space-based gravitational-wave detector. The simulator produces 3 time-series channels (TDI channels)
that serve as observations for SBI / parameter inference.

## Parameters of interest
- Number of parameters to infer: **8**
- Examples include: sky position, black hole masses, etc.

## Simulator output
- 3-channel time series (TDI channels)
- Output shape: **(n, 3)**
  - where **n** is the size of the time grid
- Current setup: **n ≈ 16,000** time points

## Simulation runtime
- Approximately **0.5 s** per simulation

## Code availability
- Repository (used for the hackathon): https://github.com/aleph-group/lisajax_sbi
- LISA instrument response implementation will be added there