import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

ports = pd.read_csv("WPI.csv")
portgeometry = [Point(xy) for xy in zip(ports['Longitude'], ports['Latitude'])]
portgeodata = gpd.GeoDataFrame(ports, crs="EPSG:4326", geometry=portgeometry)
portgeodata = portgeodata.to_crs("EPSG:3395")

fig, ax = plt.subplots()
portgeodata.plot(ax=ax, markersize=1, alpha=1, marker='*', color="green", linewidth=0.1)
plt.show()


portgeodata.plot()
