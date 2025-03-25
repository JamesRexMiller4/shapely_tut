from shapely.geometry import Point
import matplotlib.pyplot as plt
import numpy as np

point = Point(0, 0)

print(point, 'point')
print(point.length, "Length")
print(point.area, "Area")
print(point.bounds, "Bounds")
print(point.x, "Longitude")
print(point.y, "Latitude")


plt.scatter(point.x, point.y, s=500, edgecolor='black')
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(-2, 3, 1))
plt.yticks(np.arange(-2, 3, 1))
plt.show()
