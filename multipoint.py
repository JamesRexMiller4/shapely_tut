from shapely.geometry import MultiPoint
import matplotlib.pyplot as plt
import numpy as np

multipoint = MultiPoint([[0,1], [0, 2]])


print("area", multipoint.area)
print("length", multipoint.length)
print("bounds", multipoint.bounds)

plt.scatter([geom.x for geom in multipoint.geoms],
            [geom.y for geom in multipoint.geoms],
            s=500, edgecolor="black")
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(-2, 3, 1))
plt.yticks(np.arange(-1, 5, 1))
plt.show()
