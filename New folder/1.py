import numpy as np
import matplotlib.pyplot as plt

# Generate mathematical mesh
theta = np.linspace(0, 8 * np.pi, 1000)
z = np.linspace(-2, 2, 1000)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# Set up 3D plot
fig = plt.figure(figsize=(10, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Plot continuous multi-color gradient
for i in range(len(x) - 1):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=plt.cm.plasma(i / len(x)), linewidth=1.5)

# Style setup
ax.set_axis_off()
plt.title("3D Neon Vortex", color="white", fontsize=16)
plt.show()