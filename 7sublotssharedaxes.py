import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(x, y1, color='blue', label='sin(x)')
ax2.plot(x, y2, color='red', label='cos(x)')

ax1.set_title("Sine and Cosine Waves")
ax2.set_xlabel("X-axis")
ax1.set_ylabel("sin(x)")
ax2.set_ylabel("cos(x)")
ax1.legend()
ax2.legend()
plt.tight_layout()
plt.show()