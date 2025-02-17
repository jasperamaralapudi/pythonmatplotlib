import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(5, 2, 1000)

plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.title("Histogram with Multiple Distributions")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()