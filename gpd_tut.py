import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

print("Purrrr")

points_df = pd.DataFrame({
    "lat": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "long": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "points": ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
})

geometry = [Point(lat, long) for lat, long in zip(points_df.lat, points_df.long)]
points_gdf = gpd.GeoDataFrame(points_df, crs="EPSG:4326", geometry=geometry)

print(points_gdf)
