import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def random_walk(steps):
    x, y = 0, 0
    x_coords, y_coords = [x], [y]
    
    for _ in range(steps):
        x += np.random.choice([-1, 1])
        y += np.random.choice([-1, 1])
        x_coords.append(x)
        y_coords.append(y)
    
    return x_coords, y_coords

steps = 1000

x_coords, y_coords = random_walk(steps)

axis_limit = 2 * np.sqrt(steps)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-axis_limit, axis_limit)
ax.set_ylim(-axis_limit, axis_limit)
ax.set_title(f'Random Walk in R^2 with {steps} steps')
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.grid(True)
ax.axis('equal')

fig.patch.set_alpha(1)
ax.set_facecolor('none')

line, = ax.plot([], [], marker='o', markersize=5, linestyle='-', color='b', alpha=0.7)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x_coords[:frame], y_coords[:frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(1, steps + 1), init_func=init, blit=True, interval=50)

# This function can be used to save the image of the last step.
def save_last_frame():
    ax.plot(x_coords, y_coords, marker='o', markersize=5, linestyle='-', color='b', alpha=0.7)
    plt.savefig('random_walk_last_step.png', transparent=False)

#save_last_frame()

plt.show()
