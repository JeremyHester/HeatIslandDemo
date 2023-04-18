import os 
import streamlit as st
import pandas as pd
import numpy as np
import folium
import folium.plugins as plugins
from branca.colormap import LinearColormap
from folium.plugins import HeatMap
import matplotlib.cm as cm


def app():
    st.title("Home")

    st.markdown(
        """
  Use the Heatmap tab to view your map and the Data Set to see the raw data 

    """
    )
    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"
      # Load data
    df = pd.read_csv(filepath)

   # Create map object
    m = folium.Map(location=[df['latitude'].iloc[0], df['longitude'].iloc[0]], zoom_start=15)

   # Create feature group for path walked
    path = folium.FeatureGroup(name='Path Walked')
    locations = list(zip(df['latitude'], df['longitude']))
    path.add_child(folium.PolyLine(locations=locations, color='blue', weight=5))
    m.add_child(path)

   # Create feature group for temperature data
    temp_data = folium.FeatureGroup(name='Temperature Data')
    temperatures = list(df['temperature'])
    cmap = folium.LinearColormap(['blue', 'green', 'yellow', 'red'], vmin=79, vmax=87)
    for location, temp in zip(locations, temperatures):
       temp_data.add_child(folium.Marker(location=location, icon=folium.Icon(color=cmap(temp), icon='info-sign')))
    m.add_child(temp_data)

   # Add layer control
    folium.LayerControl().add_to(m)

   # Save map as HTML file
    m.save('map.html')

   # Load HTML file in Streamlit app
    with open('map.html', 'r') as f:
      html = f.read()
    st.components.v1.html(html, width=700, height=500)
   
    
