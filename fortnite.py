from math import pi, sin, cos, sqrt
from random import random
from matplotlib import pyplot as plt

# Returns normally distributed (x, y) coordinates within a circle of radius 1
def point_in_circle():
    # Random angle from 0 to 2pi
    t = 2 * pi * random()

    # Random radius
    u = random() + random()
    r = 2-u if u>1 else u

    # New circle's center
    x = r * cos(t)
    y = r * sin(t)

    return (x, y)

# Returns the distance from point (x, y) to x2 on the x-axis (x2, 0)
def distance(x, y, x2):
    return sqrt((x-x2)**2 + y**2)

# Number of new circle center points to generate
n = 1000000

# Create a list of (x, y) pairs within a circle r=1
points = [point_in_circle() for i in range(n)]

# List of points to count distances at
intervals = [x/10 for x in range(21)]

# List of lists, where each sublist is a list of distances from each point to that list's interval
distances = [[distance(x, y, x2) for (x, y) in points] for x2 in intervals]

# Filter list of distances only to distances within new radius (1)
distances_in_circle = [[dist for dist in sublist if dist < 1] for sublist in distances]

# Count number of points within radius=1 of point on x-axis
num_points_in_range = [len(sublist) for sublist in distances_in_circle]

# Convert number of points to probability of being in circle at that distance from the center
prob_in_circle = [points/n for points in num_points_in_range]

# Convert intervals to distance from center in terms of r
dist_from_center = [dist/2 for dist in intervals]

# print(dist_from_center)
print(prob_in_circle)

plt.plot(dist_from_center, prob_in_circle)
plt.title('P(being in next circle) vs. Distance from current center')
plt.xlabel('Distance from center of current circle (as fraction of r)')
plt.ylabel('Probability of being within the next circle')
# plt.grid(True)
ax = plt.gca()
# ax.set_facecolor('0.98')
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
plt.show()

