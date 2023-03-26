import geopandas as gpd
from shapely.geometry import Point
import folium
import os
import webbrowser
import tempfile

def plot_on_map(location_list: list):

    # # Create the GeoDataFrame
    gdf = gpd.GeoDataFrame(geometry=[Point(lat, lon) for lon, lat, ip in location_list])

    # Convert to EPSG 4326
    gdf.crs = 'EPSG:4326'

    # Create a Folium map object
    map = folium.Map(location=[location_list[0][0], location_list[0][1]], zoom_start=13)

    # Add the LineString and Point geometries to the map
    folium.GeoJson(gdf.geometry).add_to(map)
    for lat, lon, ip in location_list:
        folium.Marker(location=[lat, lon]).add_to(map)

    # Display the map
    tempdir = tempfile.mkdtemp()
    map_file = os.path.join(tempdir, 'map.html')
    map.save(map_file)

    webbrowser.open(map_file)

    return None