import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar(label="Intensity")
plt.title("Heatmap")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()