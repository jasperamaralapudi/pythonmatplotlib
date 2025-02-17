import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.contourf(X, Y, Z, levels=20, cmap='coolwarm')
plt.colorbar(label="Z-value")
plt.title("Contour Plot of sin(sqrt(x^2 + y^2))")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()