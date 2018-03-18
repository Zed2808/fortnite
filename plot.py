#!/usr/local/bin/python3.6

import numpy as np
from matplotlib import pyplot as plt
from fortnite import point_in_circle

N = 1000

points = [point_in_circle() for n in range(N)]
x = [point[0] for point in points]
y = [point[1] for point in points]

circle = plt.Circle((0, 0), 2, color='r',  fill=False)
new_center = plt.Circle((0, 0), 1, color='r', fill=False)

ax = plt.gca()
ax.cla()
ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-2.1, 2.1)

for i in range(N):
    ax.add_artist(plt.Circle(points[i], 1, color='black', linewidth=0.1, fill=False, zorder=0))

ax.set_aspect('equal')
ax.scatter(x, y, s=2, color='yellow')
ax.add_artist(circle)
ax.add_artist(new_center)
plt.show()

