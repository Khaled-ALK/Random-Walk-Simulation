import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_walks = 100
num_steps = 500
grid_size = 100
step_choices = [-1, 0, 1]

heatmap = np.zeros((grid_size, grid_size))

center = grid_size // 2

def random_walk():
    x, y = center, center
    for _ in range(num_steps):
        dx, dy = np.random.choice(step_choices, size=2)
        x, y = x + dx, y + dy
        x = np.clip(x, 0, grid_size - 1)
        y = np.clip(y, 0, grid_size - 1)
        yield x, y

def update(frame):
    global heatmap
    for _ in range(5):
        for x, y in random_walk():
            heatmap[x, y] += 1
    ax.clear()
    ax.imshow(heatmap, cmap='hot', origin='lower')
    ax.set_title(f"Random Walk Heatmap - Frame {frame}")

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Random Walk Heatmap")

ani = FuncAnimation(fig, update, frames=200, interval=100)

plt.show()
