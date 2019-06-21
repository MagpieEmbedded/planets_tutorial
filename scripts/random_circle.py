import matplotlib.pyplot as plt
import random

x = [random.random() for x in range(1000)]
y = [random.random() for y in range(1000)]

plt.plot(x, y, "bx")

x = [random.random() - 1 for x in range(1000)]
y = [random.random() for y in range(1000)]

plt.plot(x, y, "bx")

x = [random.random() for x in range(1000)]
y = [random.random() - 1 for y in range(1000)]

plt.plot(x, y, "bx")

x = [random.random() - 1 for x in range(1000)]
y = [random.random() - 1 for y in range(1000)]

plt.plot(x, y, "bx")

plt.show()
