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
    
@st.cache_data
def load_geojson2():
    with open('ndvi.geojson') as f:
        return json.load(f)

# Function to display the map
def display_map(geojson_data):
    gdf = gpd.read_file('output.geojson')
    centroid = gdf.geometry.unary_union.centroid

    # Create a Kepler.gl map
    map_1 = KeplerGl(height=500)

    # Set the map's initial view to focus on the centroid of the area of interest
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

# Function to display LST image
def display_lst_image():
    st.image('Figure_1.png', caption='LST Image')

# Function to display NDVI image
def display_ndvi_image():
    st.image('Figure_1.png', caption='NDVI Image')

def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Choose a view", ("Home", "LST", "NDVI"))

    if choice == "Home":
        st.title("Welcome to My Streamlit App")
        st.write("Navigate using the sidebar.")

        # Using markdown for formatted text
        st.markdown("""
            ## Explore Geospatial Data
            This application allows you to interact with different types of geospatial data. 
            You can view maps and images related to **Land Surface Temperature (LST)** and **Normalized Difference Vegetation Index (NDVI)**.
            
            ### How to Use:
            - Use the sidebar to navigate between different views.
            - Choose **LST** to explore land surface temperature data.
            - Choose **NDVI** to view vegetation index data.
            - You can select to view either maps or images for each data type.
        """)

        # Adding a visual element - e.g., an image or graph
        st.image('Figure_1.png', caption='Visualization Example')
        # Other introductory content

    elif choice == "LST":
        st.title("LST Data")
        lst_option = st.selectbox("Choose format for LST", ("Image", "Map"))
        if lst_option == "Image":
            display_lst_image()
        else:
            geojson_data = load_geojson()
            display_map(geojson_data)

    elif choice == "NDVI":
        st.title("NDVI Data")
        ndvi_option = st.selectbox("Choose format for NDVI", ("Image", "Map"))
        if ndvi_option == "Image":
            display_ndvi_image()
        else:
            geojson_data = load_geojson2()
            display_map(geojson_data)

if __name__ == "__main__":
    main()



