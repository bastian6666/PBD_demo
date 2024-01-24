import streamlit as st
from streamlit_keplergl import keplergl_static
import json
import geopandas as gpd
from keplergl import KeplerGl

# Load the GeoJSON data directly
@st.cache_data
def load_geojson():
    with open('output.geojson') as f:
        return json.load(f)

geojson_data = load_geojson()

# Load GeoJSON into a GeoDataFrame to calculate the centroid and bounds
gdf = gpd.read_file('output.geojson')
centroid = gdf.geometry.unary_union.centroid
minx, miny, maxx, maxy = gdf.geometry.total_bounds

# Calculate the midpoint coordinates for the initial map view
midpoint = [(minx + maxx) / 2, (miny + maxy) / 2]

# Create a Kepler.gl map
map_1 = KeplerGl(height=500)

# Set the map's initial view to focus on the centroid of the AOI
map_1.config = {
    'mapState': {
        'latitude': centroid.y,
        'longitude': centroid.x,
        'zoom': 10  # Adjust zoom level as needed
    }
}

# Add the GeoJSON data to the map
map_1.add_data(data=geojson_data, name='data')

# Display the map
keplergl_static(map_1)

