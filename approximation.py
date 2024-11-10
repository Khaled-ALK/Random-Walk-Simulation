import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import gaussian_kde

step_choices = [-1, 0, 1]
max_steps = 80
num_samples = 1000

def compute_s_n(n):
    steps = np.random.choice(step_choices, size=(num_samples, n, 2))
    sums = steps.sum(axis=1)
    return sums

def update(frame):
    n = 10 + frame
    s_n = compute_s_n(n)
    kde = gaussian_kde(s_n.T, bw_method=0.3)
    x_vals = np.linspace(-n, n, 200)
    y_vals = np.linspace(-n, n, 200)
    X, Y = np.meshgrid(x_vals, y_vals)
    positions = np.vstack([X.ravel(), Y.ravel()])
    density = kde(positions).reshape(X.shape)
    ax.clear()
    ax.contourf(X, Y, density, levels=30, cmap='hot')
    ax.set_title(f"Distribution of S_N (N={n})")
    ax.set_xlabel("X Position (Sum)")
    ax.set_ylabel("Y Position (Sum)")
    ax.set_xlim(-n, n)
    ax.set_ylim(-n, n)

fig, ax = plt.subplots(figsize=(8, 6))

ani = FuncAnimation(fig, update, frames=71, interval=200)

plt.show()
