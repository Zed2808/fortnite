import numpy as np
from matplotlib import pyplot as plt
from fortnite import point_in_circle

N = 1000

points = [point_in_circle() for n in range(N)]
x = [point[0] for point in points]
y = [point[1] for point in points]

circle = plt.Circle((0, 0), 2, color='r',  fill=False)

ax = plt.gca()
ax.cla()
ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-2.1, 2.1)

ax.set_aspect('equal')
ax.scatter(x, y, s=1)
ax.add_artist(circle)
plt.show()

