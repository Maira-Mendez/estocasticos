import numpy as np # type: ignore # for numerical operations and generating random steps
import matplotlib.pyplot as plt # type: ignore # for plotting and visualizing the random walks

# Parameters
n_steps = 100  # Number of steps

# Generate random steps: +1 or -1
steps = np.random.choice([-1, 1], size=n_steps)

# Calculate positions
positions = np.cumsum(steps)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(positions, marker='o', linestyle='-', markersize=4)
plt.title("1D Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.grid(True)
plt.show()