import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.axes3d import Axes3D


def update(num):
    plot_obj._offsets3d = (x[num : num + 1], y[num : num + 1], z[num : num + 1])
    plot_obj2._offsets3d = (x2[num : num + 1], y2[num : num + 1], z[num : num + 1])
    print(x[num : num + 1])
    return plot_obj


def polar_to_cartesian(radius, theta):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return (x, y)


if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlim3d([-25.0, 25.0])
    ax.set_ylim3d([-25.0, 25.0])
    ax.set_zlim3d([-25.0, 25.0])
    ax.set_autoscale_on(False)

    angles = np.linspace(0, 2 * np.pi, 100)
    x = [polar_to_cartesian(20.0, angle)[0] for angle in angles]
    print(x)
    y = [polar_to_cartesian(20.0, angle)[1] for angle in angles]
    print(y)

    x2 = [polar_to_cartesian(15.0, angle)[0] for angle in angles]
    print(x)
    y2 = [polar_to_cartesian(15.0, angle)[1] for angle in angles]
    print(y)

    z = np.zeros(len(x))
    print(z)

    plot_obj = ax.scatter(x, y, z, s=300.0, c="red", marker="o")
    ax.plot(x, y, z, "b-")
    ani = animation.FuncAnimation(fig, update, frames=len(x), interval=1000)

    plot_obj2 = ax.scatter(x2, y2, z, s=100.0, c="green", marker="o")
    ax.plot(x2, y2, z, "b-")
    ani2 = animation.FuncAnimation(fig, update, frames=len(x), interval=1000)

    plt.show()
