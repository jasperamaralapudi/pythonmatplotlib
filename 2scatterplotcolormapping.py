import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar(label="Color Intensity")
plt.title("Scatter Plot with Color Mapping")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()