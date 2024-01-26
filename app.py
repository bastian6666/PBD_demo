import streamlit as st
from streamlit_keplergl import keplergl_static
import json
import geopandas as gpd
from keplergl import KeplerGl
import time

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
            'zoom': 8.8  # Adjust zoom level as needed
        }
    }

    # Add the GeoJSON data to the map
    map_1.add_data(data=geojson_data, name='data')

    # Display the map
    keplergl_static(map_1)

# Function to display LST image
def display_lst_image():
    st.image('LST_TCA.png', caption='LST Image')

# Function to display NDVI image
def display_ndvi_image():
    st.image('NDVI_TCA.png', caption='NDVI Image')

# Function to display NDVI image
def display_dem_image():
    st.image('dem_image.png', caption='NDVI Image')

def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Choose a view", ("Home", "LST", "NDVI", "DEM", "Suitability analysis"))

    if choice == "Home":
        st.title("Pale Blue Dot Challenge 2024 - Team: EE Frogs")
        st.text("By: Alice Ni, Sebastian Sanchez, and Trenton Mulick")

        # Using markdown for formatted text
        st.markdown("""
            ## Solar Panel Suitability Analysis for the Turks and Caicos Islands
            The website showcases a comprehensive project focused on assessing the suitability for solar panel installation in the Turks and Caicos Islands. This project is grounded in an analysis of various key geographical and environmental factors that are crucial in determining the optimal locations for solar energy harvesting. The analysis incorporates a detailed examination of the Land Surface Temperature (LST), the Normalized Difference Vegetation Index (NDVI), elevation profiles, and the slope of the terrain across the islands. By evaluating the LST, the project identifies areas with the most suitable temperature conditions for solar panel efficiency (Between 20 and 26 Cº). The NDVI analysis helps in understanding vegetation density, which is vital for selecting areas with minimal shading on the panels. Elevation and slope analyses ensure that areas chosen for solar panel installation are not only accessible but also receive maximum sunlight exposure. This approach ensures that the most strategic and efficient locations are identified for solar panel installation, thereby maximizing energy output and contributing to the sustainable energy goals of the Turks and Caicos Islands.
            
            ### How to Use:
            - Use the sidebar to navigate between different views.
            - Choose **LST** to explore land surface temperature data.
            - Choose **NDVI** to view vegetation index data.
            - Choose **DEM** to view digital elevation model data.
            - Choose **Suitability analysis** to view suitability analysis.
            - You can select to view either maps or images for LST and NDVI.
        """)

        # Adding a visual element - e.g., an image or graph
        st.image('final.png', caption='Turks and Caicos Islands')
        # Other introductory content

    elif choice == "LST":
        st.title("LST Data")
        lst_option = st.selectbox("Choose format for LST", ("Map", "Image"))
        if lst_option == "Map":
            # Start the loading process
            latest_iteration = st.empty()
            bar = st.progress(0)
            # Simulate a loading process
            for i in range(100):
                latest_iteration.text(f'Loading {i+1}%')
                bar.progress(i + 1)
                time.sleep(0.1)  # Simulate a delay

            # Clear the progress bar placeholder after loading is complete
            latest_iteration.empty()
            bar.empty()
            geojson_data = load_geojson()
            display_map(geojson_data)
        else:
            display_lst_image()
            

    elif choice == "NDVI":
        st.title("NDVI Data")
        ndvi_option = st.selectbox("Choose format for NDVI", ("Map", "Image"))
        if ndvi_option == "Map":
            # Start the loading process
            latest_iteration = st.empty()
            bar = st.progress(0)
            # Simulate a loading process
            for i in range(100):
                latest_iteration.text(f'Loading {i+1}%')
                bar.progress(i + 1)
                time.sleep(0.2)  # Simulate a delay

            # Clear the progress bar placeholder after loading is complete
            latest_iteration.empty()
            bar.empty()
            geojson_data = load_geojson2()
            display_map(geojson_data)
        else:
            display_ndvi_image()

    elif choice == "DEM":
        st.title("DEM Data")
        #dem_option = st.selectbox("Choose format for DEM", ("Image"))
        display_dem_image()

    elif choice == "Suitability analysis":
        st.title("Suitability analysis")
        st.image('LST_suitability.png', caption='Surface temperature analysis')
        st.image('NDVI_suitability.png', caption='Vegetation index analysis')
        st.image('DEM_suitability.png', caption='Elevation analysis')
        st.image('Slope_suitability.png', caption='Slope analysis')
        st.image('final.png', caption='Final results')
            

if __name__ == "__main__":
    main()



