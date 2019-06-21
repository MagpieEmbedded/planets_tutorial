import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.animation as animation


def update(num):
    print(f"Updating step {num}")
    print("Angle: {:.2f}".format(angles[num]))
    plot_obj.set_data(
        polar_to_cartesian(20.0, angles[num])[0],
        polar_to_cartesian(20.0, angles[num])[1],
    )
    plot_obj.set_3d_properties(0.0)
    # plot_obj._offsets3d = [0.0, 0.0, 0.0]
    return plot_obj


def polar_to_cartesian(radius, theta):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return (x, y)


def day_to_angle(day, days_in_year):
    return ((day % days_in_year) / days_in_year) * 2 * np.pi


if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlim3d([-25.0, 25.0])
    ax.set_ylim3d([-25.0, 25.0])
    ax.set_zlim3d([-25.0, 25.0])
    ax.set_autoscale_on(False)

    angles = [day_to_angle(d, 365) for d in range(365)]

    x = polar_to_cartesian(20.0, angles[0])[0]
    print(x)
    y = polar_to_cartesian(20.0, angles[0])[1]
    print(y)
    z = 0.0
    print(z)

    orbit_x = [polar_to_cartesian(20.0, angle)[0] for angle in angles]
    orbit_y = [polar_to_cartesian(20.0, angle)[1] for angle in angles]
    orbit_z = np.zeros(len(orbit_x))

    ax.plot(orbit_x, orbit_y, orbit_z, "b-")
    plot_obj = ax.plot([x], [y], z, "ro", markersize=20)[0]

    ani = animation.FuncAnimation(fig, update, frames=len(angles), interval=10)

    plt.show()
