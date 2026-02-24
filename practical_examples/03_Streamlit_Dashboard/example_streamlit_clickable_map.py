import folium
import streamlit as st
from streamlit_folium import st_folium

# create map
m = folium.Map(location=[39.949610, -75.150282], zoom_start=11)

# create marker on map
folium.Marker(location=[39.949610, -75.150282], popup='testmarker').add_to(m)

# create polygon
polygon_coords = [
    [39.99, -75.16],  # Point 1
    [39.74, -75.16],  # Point 2
    [39.74, -75.05],  # Point 3
    [39.99, -75.05],  # Point 4
    [39.99, -75.16],  # Closing the polygon (back to Point 1)
]

# Add a polygon to the map
folium.Polygon(
    locations=polygon_coords,
    color="green",           # Border color of the polygon
    weight=2,               # Border width
    fill=True,              # Fill the polygon with color
    fill_color="green",      # Fill color
    fill_opacity=0.3,        # Fill transparency
    popup='test polygon'
).add_to(m)

# create streamlit folium map
map = st_folium(m,width=620, height=580,key="folium_map")

# check if there is a click event on the map
if map.get("last_object_clicked_popup"):
    data = map['last_object_clicked_popup']
    st.write(data)

# check if there is a click event on the map when plotting geodataframe on a map (NA)
# if map.get('last_active_drawing'):
#     data = map['last_active_drawing']['properties']['Gebied']
#     st.write(data)