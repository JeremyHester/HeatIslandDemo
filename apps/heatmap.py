import os 
import streamlit as st
import pandas as pd
import folium.plugins as plugins
from folium.plugins import HeatMap


def app():

   st.title("Heatmap")
   filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata.csv"
   data = pd.read_csv(filepath, header= None)
   map_center = [data['latitude'][0], data['longitude'][0]]
   heat_map = folium.Map(location=map_center, zoom_start=12)

   # Create a HeatMap object and add it to the map
   heatmap_data = data[['latitude', 'longitude', 'temperature']]
   heatmap_data = heatmap_data.dropna()  # Remove rows with missing data
   heatmap_data = heatmap_data.values.tolist()
   HeatMap(heatmap_data, name='Temperature Heatmap').add_to(heat_map)

   # Add layer control to the map
   folium.LayerControl().add_to(heat_map)

   # Display the map using Streamlit
   st.write(heat_map._repr_html_(), unsafe_allow_html=True)
   
   #m = leafmap.Map(tiles="stamentoner")
   #m = leafmap.Map()
   #m.add_basemap("Stamen.Toner")
   #m.add_heatmap(
    #   filepath,
     #  latitude="latitude",
      # longitude='longitude',
       #value="temperature",
      # name="Heat map",
      # radius=20,
    #)
   #m.to_streamlit(height=700)

    
    
    
    
    
    
    
    
    
    
    
  #     filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
   # m = leafmap.Map(tiles="stamentoner")
    #m.add_heatmap(
     #   filepath,
      #  latitude="latitude",
       # longitude="longitude",
        #value="pop_max",
        #name="Heat map",
        #radius=20,
    #)
