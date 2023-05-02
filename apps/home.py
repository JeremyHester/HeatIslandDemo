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
  Here is the path that you walked as you were taking samples! To see the overall heat map, use the "Heatmap" tab, and to see the raw dataset, use the "Data Set" tab

    """
    )
    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"
    # Read CSV data
    df = pd.read_csv(filepath)

    # Create map object
    m = folium.Map(location=[df['latitude'].iloc[0], df['longitude'].iloc[0]], zoom_start=15)

    # Create feature group for path walked
    path = folium.FeatureGroup(name='Path Walked')
    locations = list(zip(df['latitude'], df['longitude']))
    path.add_child(folium.PolyLine(locations=locations, color='blue', weight=5))
    m.add_child(path)

    # Create feature group for data markers
    data = folium.FeatureGroup(name='Data')
    cmap = folium.LinearColormap(['blue', 'green', 'orange', 'red'], vmin=5, vmax=120)
    for i, row in df.iterrows():
     location = (row['latitude'], row['longitude'])
     temp = row['temperature']
     humidity = row['humidity']
     time = row['time']
     popup_html = f'Temperature: {temp:.2f}°F<br>Humidity: {humidity:.2f}%<br>Time: {time}'
     marker = folium.Marker(location=location, icon=folium.Icon(color=cmap(temp), icon='location-pin'), popup=popup_html)
     data.add_child(marker)
    m.add_child(data)

    # Add layer control
    folium.LayerControl().add_to(m)

    # Save map as HTML file
    m.save('map.html')

    # Load HTML file in Streamlit app
    with open('map.html', 'r') as f:
      html = f.read()
    st.components.v1.html(html, width=700, height=500)
    
