"""Solutions for Notebook 02: Neural Posterior Estimation"""

# Solution for PosteriorNet output dimension
# The key insight: we need TWO numbers per parameter dimension
# - mu (mean of the Gaussian)
# - log_var (log variance for numerical stability)
#
# So output_dim = theta_dim * 2

class PosteriorNet(nn.Module):
    """Network that predicts posterior distribution parameters.

    Input: observation x (shape: batch_size x x_dim)
    Output: parameters (mu, log_var) of Gaussian q(theta|x)
    """

    def __init__(self, x_dim, theta_dim, hidden_dim=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(x_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, theta_dim * 2),  # <- KEY: output mu AND log_var
        )
        self.theta_dim = theta_dim

    def forward(self, x):
        """Returns (mu, log_var) for the predicted posterior."""
        out = self.net(x)
        mu = out[:, :self.theta_dim]
        log_var = out[:, self.theta_dim:]
        return mu, log_var

    def log_prob(self, theta, x):
        """Compute log q(theta | x) under the predicted Gaussian."""
        mu, log_var = self.forward(x)
        log_prob = -0.5 * (math.log(2 * math.pi) + log_var + (theta - mu)**2 / torch.exp(log_var))
        return log_prob.sum(dim=-1)
