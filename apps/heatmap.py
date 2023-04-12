import os 
import streamlit as st
#import leafmap.leafmap as leafmap
import pandas as pd
import plotly.express as px

def app():

   st.title("Heatmap")
   filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata.csv"
   data = pd.read_csv(filepath)

   # Create a correlation matrix from the data
   corr_matrix = data.corr()

  # Create a Plotly scattermapbox object
   map_fig = px.scatter_mapbox(data, lat='latitude', lon='longitude', color=corr_matrix)

   # Add hover information
   map_fig.update_layout(title='Correlation Matrix Heatmap on Map', mapbox_style='open-street-map')
   map_fig.update_traces(hovertemplate='Latitude: %{lat}<br>Longitude: %{lon}<br>Correlation: %{marker.color:.2f}')

   # Display the plot in Streamlit
   st.plotly_chart(map_fig, use_container_width=True)
   
   
   
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
