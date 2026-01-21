# Alexandre Loret — Matérn Gaussian Process spatiotemporal simulator (advection / separability)

## Short description
Spatiotemporal simulator based on Matérn Gaussian Process models producing 1D space + 1D time data.
Two variants are currently considered:
- **Model 1: Advection**
- **Model 2: Separability / non-separable spatiotemporal covariance**

The goal is to infer the GP / covariance parameters from simulated (possibly partially observed) spatiotemporal data.
Future work may include **non-stationary** extensions (potentially increasing the number of parameters).

## Parameters of interest
Currently **4 parameters**, including:
- Spatial range
- Temporal range
- Sill
- (one additional model-dependent parameter)

## Simulator output
- Spatiotemporal data (1D space + 1D time), represented as an "image" of shape:
  - **[Time, Space]**
- The simulation pipeline supports missing data:
  - output includes both the data and a missing-data mask

### Data format used in the notebook
- Output tensor shape:
  - **[Deepset, 2, Time shape, Space shape]**
- `2` corresponds to:
  - simulated image
  - mask of missing data
- Notebook parameters:
  - `missing_ratio`: proportion of hidden data (`0` = full observation)
  - `deepset_size`: number of simulations per parameter set

## Simulation scale / speed (recent experiments)
- Training dataset example: **20,000 images of size 30×30**
- Generation time:
  - Model 1 (Advection): ~**2 minutes**
  - Model 2 (Separability): ~**50 minutes**
  - (for the same dataset size)

## References (simulation models)
- Clarotto, L., Allard, D., Romary, T., & Desassis, N. (2024).
  *The SPDE approach for spatio-temporal datasets with advection and diffusion.*
  Spatial Statistics, 62, 100847.
- Allard, Emery, Lacaux and Lantéjoul (2020).
  *Simulating space-time random fields with nonseparable Gneiting-type covariance functions.*
  Statistics and Computing, 30, 1479–1495.

## References (inference methods)
- Sainsbury-Dale, M., Zammit-Mangion, A., & Huser, R. (2024).
  *Likelihood-free parameter estimation with neural Bayes estimators.*
  The American Statistician, 78(1), 1–14.
- Zammit-Mangion, A., Sainsbury-Dale, M., & Huser, R. (2025).
  *Neural Methods for Amortized Inference.*
  Annual Review of Statistics and Its Application, 12, 311–335.
  https://doi.org/10.1146/annurev-statistics-112723-034123