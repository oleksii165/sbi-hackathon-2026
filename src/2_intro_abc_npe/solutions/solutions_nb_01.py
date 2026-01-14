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
    
    print(f"Acceptance rate: {len(accepted)}/{num_simulations} = {100*len(accepted)/num_simulations:.1f}%")
    return torch.cat(accepted), torch.cat(all_theta)