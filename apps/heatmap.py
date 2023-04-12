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

   # Create a heatmap using Plotly
   fig = px.imshow(corr_matrix, x=corr_matrix.columns, y=corr_matrix.columns)

   # Add hover information
   fig.update_layout(title='Correlation Matrix Heatmap', xaxis_title='Columns', yaxis_title='Columns')
   fig.update_traces(hovertemplate='Column X: %{x}<br>Column Y: %{y}<br>Correlation: %{z:.2f}')

   # Display the plot in Streamlit
   st.plotly_chart(fig, use_container_width=True)
   
   
   
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
