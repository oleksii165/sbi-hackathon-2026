"""Solutions for Notebook 04: NLE vs NPE Comparison"""

# Solution for sampling from NLE posterior with MCMC
# The key insight: the API is the same as NPE, just slower due to MCMC

print("Sampling from NLE posterior (MCMC)... this takes a moment.")

nle_samples = nle_posterior.sample((10000,), x=x_o)

print(f"NLE samples shape: {nle_samples.shape}")
