import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

def animate(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50)
plt.title("Animated Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()