"""Solutions for Notebook 01: Introduction to SBI with Rejection ABC"""

# Solution for smart rejection ABC implementation
def rejection_abc_smart(theta: Tensor, x: Tensor, epsilon: float) -> tuple[Tensor, Tensor]:
    """Run rejection ABC and return accepted posterior samples."""
    accepted = []

    for theta_i, x_i in zip(theta, x):
        if distance(x_i, x_o) < epsilon:
            accepted.append(theta_i)

    if not len(accepted):
        raise ValueError("No parameters were accepted, epsilon likely too small")
    
    return torch.stack(accepted)