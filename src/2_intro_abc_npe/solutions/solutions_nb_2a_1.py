"""Solutions for Notebook 01: Introduction to SBI with Rejection ABC"""

# Solution for rejection ABC implementation
def rejection_abc(num_simulations: int, epsilon: float) -> tuple[Tensor, Tensor]:
    """Run rejection ABC and return accepted posterior samples."""
    accepted = []
    all_theta = []
    
    for _ in trange(num_simulations):
        theta = prior.sample((1,))
        x = lotka_volterra_simulator(theta, use_autocorrelation=True)
        
        if distance(x, x_o) < epsilon:
            accepted.append(theta)

        all_theta.append(theta)

    if not len(accepted):
        raise ValueError("No parameters were accepted, epsilon likely too small")
    
    return torch.cat(accepted), torch.cat(all_theta)