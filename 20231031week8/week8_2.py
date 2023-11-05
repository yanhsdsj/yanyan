#matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = np.random.rand(10)
plt.plot(x, y)
plt.show()

plt.bar(x, y)
plt.show()

plt.scatter(x, y)
plt.show()
