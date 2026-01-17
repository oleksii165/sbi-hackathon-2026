"""Solution for SNPE multi-round inference exercise"""

# Initialize
trainer = SNPE(prior)
proposal = prior  # Start sampling from the prior
posteriors = []   # Store posteriors from each round

for round_idx in range(NUM_ROUNDS):
    print(f"\n=== Round {round_idx + 1} ===")

    # Step 1: Generate training data by sampling from the proposal
    print(f"Simulating {NUM_SIMS_PER_ROUND} samples...")
    theta, x = simulate_for_sbi(simulator, proposal, NUM_SIMS_PER_ROUND, num_workers=NUM_WORKERS)

    # Step 2: Append simulations (pass proposal for SNPE correction)
    trainer.append_simulations(theta, x, proposal=proposal)

    # Step 3: Train
    print("Training...")
    trainer.train(show_train_summary=True)

    # Step 4: Build posterior
    posterior = trainer.build_posterior()
    posteriors.append(posterior)

    # Step 5: Set posterior as proposal for next round (focused on x_o)
    proposal = posterior.set_default_x(x_o)

    # Quick check
    samples = posterior.sample((1000,), x=x_o)
    print(f"Posterior mean: {samples.mean(dim=0).numpy()}")
    print(f"Posterior std:  {samples.std(dim=0).numpy()}")

print("\n=== Done ===")
