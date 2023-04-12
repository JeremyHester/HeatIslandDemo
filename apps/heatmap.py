import os 
import streamlit as st
import matplotlib as mp
#import leafmap.leafmap as leafmap
import pandas as pd
import seaborn as sns

def app():

    st.title("Heatmap")

    #file_path = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata.csv"
  # Read the CSV file into a DataFrame, while ignoring columns 1, 2, and 6
#df = pd.read_csv(file_path, usecols=lambda column : column not in [0,1,5])

# Generate a correlation matrix for the DataFrame
#corr_matrix = df.corr()

# Create a heatmap of the correlation matrix using Seaborn
#fig, ax = plt.subplots(figsize=(10,10))
#sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)

# Display the heatmap in the app
#st.pyplot(fig)



   # m = leafmap.Map(tiles="stamentoner")
   # m = leafmap.Map()
   # m.add_basemap("Stamen.Toner")
   # m.add_heatmap(
   # filepath,
   # latitude="latitude",
   # longitude='longitude',
   # value="pop_max",
   # name="Heat map",
   # radius=20,
   # )
   # m.to_streamlit(height=700)

    
    
    
    
    
    
    
    
    
    
    
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
