import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ports = pd.read_csv("WPI.csv")
airports = pd.read_csv("airports.csv", delimiter=",", names=['id', 'name', 'country', 'iata', 'icao', 'lat', 'long', 'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

port_geometry = [Point(xy) for xy in zip(ports['Longitude'], ports['Latitude'])]
port_geodata = gpd.GeoDataFrame(ports, crs="EPSG:4326", geometry=port_geometry)

airport_geometry = [Point(xy) for xy in zip(airports['long'], airports['lat'])]
airport_geodata = gpd.GeoDataFrame(airports, crs="EPSG:4326", geometry=airport_geometry)

fig, ax = plt.subplots(facecolor="black", subplot_kw={'projection': ccrs.Robinson()})
ax.patch.set_facecolor('black')
airport_geodata.plot(ax=ax, transform=ccrs.PlateCarree(), markersize=4, alpha=1, color='crimson', edgecolors='none')
port_geodata.plot(ax=ax, transform=ccrs.PlateCarree(), markersize=3, alpha=1, edgecolors='none', color='lightblue')
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
plt.show()
