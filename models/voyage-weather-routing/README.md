# Nicola Zomer — Voyage simulator for weather routing under uncertainty

## Short description
Simulation tool that evaluates the execution of a proposed maritime route under uncertain weather conditions
and noisy boat speed. Given a set of routing parameters and environmental data, the simulator reconstructs
the weather encountered along the route, checks compliance with operational limits, and estimates the
corresponding arrival time.

The objective is to solve the inverse problem of inferring optimal departure windows that lead to feasible
routes reaching the destination at a prescribed arrival time.

## Parameters of interest
- Number of parameters to infer: **1 to 5**
- Examples include:
  - departure time
  - wind and wave operational limits
  - boat speed factor
  - (other routing parameters)

## Simulator output
- Weather conditions encountered along the route
- Feasibility indicator (respecting or not operational limits)
- Estimated arrival time
- Can be reduced to **1 or 2 scalar metrics of interest**

## Simulation runtime
- Not benchmarked yet
- Expected runtime: **milliseconds to ~1 second**
  - depending on weather data caching

## Code availability
- Repository not available yet

## References
- None provided