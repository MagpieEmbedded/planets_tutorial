import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.animation as animation


class Planet:
    # scalar to increase general size
    scalar = 1

    def __init__(self, name, days_in_year, size=0.1, color="red"):
        self.name = name
        self.days_in_year = days_in_year
        self.size = size
        self.color = color

        # Polar parameters
        self.a = 0
        self.b = 0
        self.c = 0

        self.graph_obj = None

    def set_size(self, size):
        self.size = size

    def set_radius(self, radius):
        self.radius = radius

    def angle(self, day):
        return day_to_angle(day, self.days_in_year)

    def get_position(self, day):
        """Return x and y for days from 0 position"""
        angle = self.angle(day)
        # Implementation of polar equation
        radius = Planet.scalar * (self.b ** 2) / (self.a - self.c * np.cos(angle))
        (x, y) = polar_to_cartesian(radius, angle)
        return (x, y)

    def set_polar_parameters(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def create_graph_obj(self, ax):
        self.graph_obj = ax.plot(
            [self.get_position(0)[0]],
            [self.get_position(0)[1]],
            0.0,
            "o",
            markersize=self.size,
            color=self.color,
        )[0]

    def update_graph_obj(self, day):
        """Update the position of the graph to be correct to a day from 0"""
        self.graph_obj.set_data(self.get_position(day)[0], self.get_position(day)[1])
        self.graph_obj.set_3d_properties(0.0)

    def get_orbit(self):
        orbit = [self.get_position(d) for d in range(int(self.days_in_year))]
        orbit_x = [x[0] for x in orbit]
        orbit_y = [y[1] for y in orbit]
        return (orbit_x, orbit_y, [0.0 for x in range(len(orbit_x))])


def update(num):
    print(f"Updating day {num}")
    for planet in planets:
        planet.update_graph_obj(num)


def polar_to_cartesian(radius, theta):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return (x, y)


def day_to_angle(day, days_in_year):
    return ((day % days_in_year) / days_in_year) * 2 * np.pi


if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    astro_unit = 1495.98  # 149,598,000 km

    ax.set_xlim3d([-2.0, 2.0])
    ax.set_ylim3d([-2.0, 2.0])
    ax.set_zlim3d([-0.5, 0.5])
    ax.set_autoscale_on(False)

    planets = []

    print("Size of earth: {}".format(12756 / astro_unit))

    earth = Planet("Earth", 365.25, 12756 / astro_unit, "blue")
    earth.set_polar_parameters(1.0027, 1.0025, 0.0167)
    earth.create_graph_obj(ax)

    planets.append(earth)

    mercury = Planet("Mercury", 88, 4879 / astro_unit, "orange")
    mercury.set_polar_parameters(0.3870, 0.3788, -0.0796)
    mercury.create_graph_obj(ax)

    planets.append(mercury)

    venus = Planet("Venus", 224.7, 12104 / astro_unit, "brown")
    venus.set_polar_parameters(0.7219, 0.7219, -0.0049)
    venus.create_graph_obj(ax)

    planets.append(venus)

    mars = Planet("Mars", 687, 6792 / astro_unit, "red")
    mars.set_polar_parameters(1.5241, 1.5173, -0.1424)
    mars.create_graph_obj(ax)

    planets.append(mars)

    # jupiter = Planet("Jupiter", 4331, 50, 180.0, "orange")
    # jupiter.create_graph_obj(ax)

    for planet in planets:
        orbit = planet.get_orbit()
        ax.plot(orbit[0], orbit[1], orbit[2], "-", color=planet.color, linewidth=0.5)

    ani = animation.FuncAnimation(fig, update, frames=10000, interval=10)

    plt.show()
