import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load a sample shapefile (Natural Earth data: World countries)
@st.cache_data
def load_data():
    url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
    gdf = gpd.read_file(url)
    return gdf

# Load the data
gdf = load_data()

# Title
st.title("Interactive Map of World Countries")

# Sidebar for filtering options
continent_options = gdf['CONTINENT'].unique().tolist()
selected_continent = st.sidebar.selectbox("Select Continent", ["All"] + continent_options)

# Filter data based on selection
if selected_continent != "All":
    gdf = gdf[gdf['CONTINENT'] == selected_continent]

# Create a Folium map centered on the world
m = folium.Map(location=[0, 0], zoom_start=2)

# Add country polygons to the map
for _, row in gdf.iterrows():
    # Add country boundary polygons with popup information
    folium.GeoJson(row['geometry'], 
                   tooltip=row['NAME']).add_to(m)

# Display Folium map in Streamlit
st_folium(m, width=700, height=500)

# Display dataframe for inspection
st.write("### Data Table", gdf[['NAME', 'CONTINENT', 'POP_EST']])
