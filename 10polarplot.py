import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(5 * theta))

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_title("Polar Plot of a 5-Petal Flower")
plt.show()