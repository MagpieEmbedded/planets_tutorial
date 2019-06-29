"""Simple script to create a sphere in 3d space"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.scatter(0, 0, 0)

plt.show()
